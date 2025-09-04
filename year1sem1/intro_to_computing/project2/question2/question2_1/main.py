import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.load("quarterly_ocean_temps_1875_2025.npy")
data = data / 100
data[data == -99.99] = np.nan

fig, ax = plt.subplots()
ax.set_facecolor([54/255, 69/255, 79/255])

frames = []
year_labels = []

for year in range(0, 141, 10):
    decadal_data = data[year:year+10, :, :, :]
    decadal_avg = np.nanmean(decadal_data, axis = (0,1))
    frames.append(decadal_avg)
    year_labels.append(1875 + year)




img = ax.imshow(frames[0], cmap = "jet")
title = ax.set_title(f"Ocean temperature year {year_labels[0]}")
cbar = plt.colorbar(img, ax=ax)
cbar.set_label("Temperature (degrees Celcius)")

def update(i):
    img.set_data(frames[i])
    title.set_text(f"Ocean temperature year {year_labels[i]}")
    return [img, title]

ani = animation.FuncAnimation(fig, update, frames=len(frames), interval = 1000)

ani.save("ocean_temps.gif", writer = "pillow", fps = 1)




#question2
def convert_latitude_to_index(latitude):
    return int((90 - latitude)/2)
def convert_longitude_to_index(longitude):
    if longitude < 0:
        longitude = 360 + longitude # because google maps uses a -180 -> 0 -> 180 system for longitude
    return int(longitude/2)


# 0.07332, 113.42925

#-50.60746, -155.07589

lat_start = convert_latitude_to_index(0.07332)
lat_end = convert_latitude_to_index(-50.60746)

lon_start = convert_longitude_to_index(113.42925)
lon_end = convert_longitude_to_index(-155.07589)

lat_start, lat_end = sorted([lat_start, lat_end])
lon_start, lon_end = sorted([lon_start, lon_end])


oceania_data_5years = data[145:, :, lat_start:lat_end, lon_start:lon_end]
average_temp_5years = np.nanmean(oceania_data_5years, axis=(0,1))

oceania_data_since1875 = data[:, :, lat_start:lat_end, lon_start:lon_end]
average_temp_yearly = np.nanmean(oceania_data_since1875, axis = (1,2,3))

years = np.arange(1875, 2025)



fig1, ax1 = plt.subplots(1,2,figsize=(15,10))
im_ = ax1[0].imshow(average_temp_5years, cmap="jet")
cbar = fig1.colorbar(im_, ax=ax1[0])
cbar.set_label("Temperature (degrees Celsius)")
ax1[0].set_facecolor([54/255, 69/255, 79/255])
ax1[0].set_title("Average Ocean Temperature in Oceania (2019 - 2024)")

ax1[1].plot(years, average_temp_yearly, color='red')
ax1[1].set_title("Average Ocean Temperature in Oceania yearly (1875 - 2024)")
ax1[1].set_xlabel("Year")
ax1[1].set_ylabel("Temperature (Degrees Celcius)")
ax1[1].grid()

plt.tight_layout()
plt.savefig("Oceania_current.png")


#question3: 
num_of_periods = int((2025-1875)/5)

average = []
for year in range(0,146,5):
    data_per_5year_block = data[year: year+5, :, :, :]
    avg_per_5year_block = np.nanmean(data_per_5year_block)
    average.append(avg_per_5year_block)

fig2, ax2 = plt.subplots(figsize=(13,6))

alphas = np.linspace(0.2, 1.0, num_of_periods)

mid_years = [1875+5*k + 2 for k in range(num_of_periods)]

for k in range(num_of_periods):
    ax2.plot(mid_years[k], average[k], marker='o', color="blue", alpha=alphas[k])

ax2.set_title("Average Ocean Temperature in Oceania (1875-2024) in 5 year blocks")
ax2.set_xlabel("Year")
ax2.set_ylabel("Average temperature (Degrees Celcius)")
ax2.grid()

plt.savefig("5year_trends.png")
plt.show()
