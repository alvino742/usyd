import numpy as np
import scipy
import matplotlib.pyplot as plt


data = np.load("quarterly_ocean_temps_1875_2025.npy")
data = data / 100
data[data == -99.99] = np.nan



def convert_latitude_to_index(latitude):
    return int((90 - latitude)/2)
def convert_longitude_to_index(longitude):
    if longitude < 0:
        longitude = 360 + longitude # because google maps uses a -180 -> 0 -> 180 system for longitude
    return int(longitude/2)
#latitude and longitude extents of each region

regions = {
"Oceania": {
        "lat_range": (-50.6, 0.1),
        "lon_range": (113.4, 205.0),
        "color": [0, 132/255, 61/255],
        "linestyle": "-"
    },
    "Antarctica": {
        "lat_range": (-90.0, -60.0),
        "lon_range": (0.0, 360.0),
        "color": [16/255, 108/255, 172/255],
        "linestyle": "--"
    },
    "Atlantic": {
        "lat_range": (35.0, 85.0),
        "lon_range": (-30.0, 20.0),
        "color": [208/255, 12/255, 51/255],
        "linestyle": "-."
    }
}

def objective(params, t, y):
    a,b, = params
    return np.sum((a*t + b-y)**2)

#generating indices

num_of_years = 2006-1875
num_of_quarters = num_of_years * 4

fig1, ax1 = plt.subplots(figsize=(13,7))

for region, region_info in regions.items():
    lat_start, lat_end = sorted([
        convert_latitude_to_index(region_info["lat_range"][0]),
        convert_latitude_to_index(region_info["lat_range"][1])
    ])

    lon_start, lon_end = sorted([
        convert_longitude_to_index(region_info["lon_range"][0]),
        convert_longitude_to_index(region_info["lon_range"][1])
    ])

    region_quarterly_data = data[:131, :, lat_start:lat_end, lon_start:lon_end]
    region_quarterly_avg = np.nanmean(region_quarterly_data, axis=(2,3))

    y_values = region_quarterly_avg.flatten()

    t_values = np.linspace(1875,2006, num_of_quarters)

    result = scipy.optimize.minimize(objective, x0 = [0,0], args = (t_values, y_values))
    a_test, b_test, = result.x
    y_pred = a_test * t_values + b_test

    #storing these in the dictionary for later use
    region_info["lat slice"] = slice(lat_start, lat_end)
    region_info["lon slice"] = slice(lon_start, lon_end)
    region_info["Linear fit parameters"] = {"a": a_test, "b": b_test}



    ax1.plot(t_values, y_values, label=f"{region} data", color = region_info["color"], linestyle = region_info["linestyle"], alpha = 0.3)
    ax1.plot(t_values, y_pred, color= region_info["color"], linestyle = region_info["linestyle"], linewidth = 2, label = f"{region} fit line")

ax1.set_title("Mean Sea surface temperature quarterly of 3 regions from 1875 to 2025 and linear fit")
ax1.set_xlabel("Time (years)")
ax1.set_ylabel("Temperature (degrees Celcius)")
ax1.grid()

plt.tight_layout()
ax1.legend()
plt.savefig("Quarterly linear line of best fit.png")

#question 2
fig2, ax2 = plt.subplots(figsize = (12,6))

for region, region_info in regions.items():
    region_data_2006_2024 = data[132:, :, region_info["lat slice"], region_info["lon slice"]]
    region_quarterly_avg = np.nanmean(region_data_2006_2024, axis=(2,3))

    y_values = region_quarterly_avg.flatten()
    a,b = region_info["Linear fit parameters"].values()
    
    #time axis:
    num_of_years = 2024-2006+1
    num_of_quarters = num_of_years * 4
    t_values = np.arange(2006,2024,0.25)

    y_pred = a * t_values + b

    error = np.abs(y_pred - y_values)
    ax2.plot(t_values, error, label=f"{region} linear fit error", linestyle = region_info["linestyle"])
   

ax2.set_title("Linear fit absolute difference error according to different regions")
ax2.set_xlabel("Time (years)")
ax2.set_ylabel("Absolute Error (degrees Celsius)")

ax2.grid()
ax2.legend()
plt.savefig("Absolute error from 2006 - 2024")


#question3: 

#appropriate data subset, looking at the graph, from 1940 onwards, the gradient shows a more visable increasing trend. 
fig3, ax3 = plt.subplots(figsize = (13,7))

for region, region_info in regions.items():
    #from 1940 -2024
    region_subset = data[65:, :, region_info["lat slice"], region_info["lon slice"]]
    region_quarterly_avg = np.nanmean(region_subset, axis=(2,3))

    y_values = region_quarterly_avg.flatten()
    t_values = np.arange(1940, 2025, 0.25)

    valid_mask = ~np.isnan(y_values)
    y_values = y_values[valid_mask]
    t_values = t_values[valid_mask]

    #convert to kelvin to avoid negative values
    y_values_kelvin = y_values + 273.15
    logy = np.log(y_values_kelvin)

    def exp_objective(params):
        a,b = params
        return np.sum((a * t_values + b - logy) ** 2)
    
    result = scipy.optimize.minimize(exp_objective, x0 = [0,0])
    a_exp_test, b_exp_test = result.x
    logy_pred = a_exp_test * t_values + b_exp_test
    y_pred_kelvin = np.exp(logy_pred)
    #convert back to celcius
    y_pred_celcius = y_pred_kelvin - 273.15

 


    region_info["Exponential fit parameters"] = {"a": a_exp_test, "b": b_exp_test}

   
    a_lin, b_lin = region_info["Linear fit parameters"].values()
    y_lin_pred = a_lin * t_values + b_lin
    #question 4
    new_rmse = np.sqrt(np.mean((y_values - y_pred_celcius)**2))

    # Calculate RMSE for linear model
    lin_rmse = np.sqrt(np.mean((y_values - y_lin_pred)**2))

    print(f"{region} RMSE:")
    print(f"  Exponential fit RMSE: {new_rmse:.3f} degrees Celcius")
    print(f"  Linear fit RMSE:{lin_rmse:.3f} degrees Celcius\n")

    ax3.plot(t_values, y_values, label=f"{region} actual", color=region_info["color"], linestyle=region_info["linestyle"], alpha=0.3)
    ax3.plot(t_values, y_lin_pred, label=f"{region} linear", color=region_info["color"], linestyle=region_info["linestyle"], linewidth=1.5)
    ax3.plot(t_values, y_pred_celcius, label=f"{region} exponential", color=region_info["color"], linestyle=":", linewidth=2)

ax3.set_title("Improved exponential vs linear fit (1940–2024)")
ax3.set_xlabel("Time (years)")
ax3.set_ylabel("Temperature (°C)")
ax3.grid()
ax3.legend()
plt.tight_layout()
plt.savefig("Exponential_vs_Linear_fit_1940_2024.png")



#question 5
fig4, ax4 = plt.subplots(figsize=(13, 6))

interval = 20  # number of quarters (~5 years)
for region, region_info in regions.items():
    region_subset = data[65:, :, region_info["lat slice"], region_info["lon slice"]]
    region_quarterly_avg = np.nanmean(region_subset, axis=(2, 3))

    y_values = region_quarterly_avg.flatten()
    t_values = np.linspace(1940, 2025, len(y_values))

    valid_mask = ~np.isnan(y_values)
    y_values = y_values[valid_mask]
    t_values = t_values[valid_mask]

    # retrieving a, b values from previous questions
    a_lin, b_lin = region_info["Linear fit parameters"].values()
    a_exp, b_exp = region_info["Exponential fit parameters"].values()

    y_exp = np.exp(a_exp * t_values + b_exp) - 273.15
    y_lin = a_lin * t_values + b_lin

    rmse_lin_list = []
    rmse_exp_list = []
    interval_centers = []

    for i in range(0, len(y_values) - interval + 1, interval):
        y_true = y_values[i:i+interval]
        y_pred_lin = y_lin[i:i+interval]
        y_pred_exp = y_exp[i:i+interval]

        rmse_lin = np.sqrt(np.mean((y_true - y_pred_lin)**2))
        rmse_exp = np.sqrt(np.mean((y_true - y_pred_exp)**2))

        rmse_lin_list.append(rmse_lin)
        rmse_exp_list.append(rmse_exp)
        interval_centers.append(np.mean(t_values[i:i+interval]))

    ax4.plot(interval_centers, rmse_lin_list, label=f"{region} Linear RMSE", linestyle=region_info["linestyle"], color=region_info["color"], alpha=0.6)
    ax4.plot(interval_centers, rmse_exp_list, label=f"{region} Exponential RMSE", linestyle=":", color=region_info["color"], linewidth=2)

ax4.set_title("RMSE over time: Linear vs Exponential Model (1940–2024)")
ax4.set_xlabel("Time (years)")
ax4.set_ylabel("RMSE (°C)")
ax4.grid()
ax4.legend()
plt.tight_layout()
plt.savefig("RMSE_over_time.png")
plt.show()






