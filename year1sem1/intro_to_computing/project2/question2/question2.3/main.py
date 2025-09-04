import numpy as np
import matplotlib.pyplot as plt


data = np.load("quaterly_ocean_temps_1875_2025.npy")
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

co2_raw = np.genfromtxt("co2_mm_mlo.csv", delimiter=",", skip_header=1)
co2_years = co2_raw[:, 0].astype(int)
co2_months = co2_raw[:, 1].astype(int)
co2_ppm = co2_raw[:, 2]

co2_time = co2_years + (co2_months - 1) / 12


fig, ax1 = plt.subplots(figsize=(13, 7))

# Plot CO2 on second y-axis
ax2 = ax1.twinx()
ax2.plot(co2_time, co2_ppm, color='gray', linewidth=1.5, label="CO₂ (ppm)")
ax2.set_ylabel("CO₂ Concentration (ppm)", color='gray')
ax2.tick_params(axis='y', labelcolor='gray')

for region, info in regions.items():
    lat_start, lat_end = sorted([convert_latitude_to_index(info["lat_range"][0]), convert_latitude_to_index(info["lat_range"][1])])
    lon_start, lon_end = sorted([convert_longitude_to_index(info["lon_range"][0]), convert_longitude_to_index(info["lon_range"][1])])
    
    # Extract 1960–2025: index 85–150 (inclusive)
    region_data = data[85:151, :, lat_start:lat_end, lon_start:lon_end]
    region_avg = np.nanmean(region_data, axis=(2, 3)).flatten()
    sst_time = np.linspace(1960, 2025, len(region_avg))

    ax1.plot(sst_time, region_avg, label=region + " SST", color=info["color"], linestyle=info["linestyle"])

ax1.set_xlabel("Year")
ax1.set_ylabel("Sea Surface Temperature (°C)")
ax1.set_title("Sea Surface Temperature and Atmospheric CO₂ (1960–2025)")
ax1.grid()
ax1.legend(loc="upper left")

plt.tight_layout()
plt.savefig("SST_CO2_Twinx.png")

#question 2
def compute_corr(x, y):
    x_bar = np.mean(x)
    y_bar = np.mean(y)
    numerator = np.sum((x - x_bar) * (y - y_bar))
    denominator = np.sqrt(np.sum((x - x_bar)**2) * np.sum((y - y_bar)**2))
    return numerator / denominator

# define 5-year chunks from 1960 to 2025
start_years = np.arange(1960, 2026, 5)
corr_results = {
    "Oceania": [],
    "Antarctica": [],
    "Atlantic": []
}
region_avgs = {}

# get average SSTs for each region (same as before)
for region, info in regions.items():
    lat1 = convert_latitude_to_index(info["lat_range"][0])
    lat2 = convert_latitude_to_index(info["lat_range"][1])
    lon1 = convert_longitude_to_index(info["lon_range"][0])
    lon2 = convert_longitude_to_index(info["lon_range"][1])
    lat_start, lat_end = sorted([lat1, lat2])
    lon_start, lon_end = sorted([lon1, lon2])

    region_data = data[85:151, :, lat_start:lat_end, lon_start:lon_end]
    avg_temp = np.nanmean(region_data, axis=(2, 3)).flatten()  # quarterly
    region_avgs[region] = avg_temp

# turn CO2 monthly data into a clean array
co2_months_full = co2_years + (co2_months - 1) / 12
co2_full = co2_ppm

# loop through each period and compute correlation
years_mid = []
for start in start_years[:-1]:
    end = start + 5
    years_mid.append((start + end) / 2)

    # get co2 values in that range
    co2_mask = (co2_months_full >= start) & (co2_months_full < end)
    co2_range = co2_full[co2_mask]

    for region in regions.keys():
        # match SST to 5-year period
        sst_index_start = (start - 1960) * 4
        sst_index_end = (end - 1960) * 4
        sst_range = region_avgs[region][sst_index_start:sst_index_end]

        # resample SST to monthly (4 quarters -> 12 months per year)
        if len(sst_range) == 20:  # 5 years of quarterly
            sst_monthly = np.repeat(sst_range, 3)  # 3 months per quarter
        else:
            corr_results[region].append(np.nan)
            continue

        if len(sst_monthly) != len(co2_range):
            corr_results[region].append(np.nan)
            continue

        # calculate correlation
        corr = compute_corr(sst_monthly, co2_range)
        corr_results[region].append(corr)

# plot results
plt.figure(figsize=(12,6))
for region in regions.keys():
    plt.plot(years_mid, corr_results[region], label=region, color=regions[region]["color"], linestyle=regions[region]["linestyle"])

plt.xlabel("Mid-Year of 5-Year Period")
plt.ylabel("Sample Correlation Coefficient")
plt.title("5-Year Correlation between SST and CO₂ (1960–2025)")
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("correlation_coefficients_over_time.png")


#question 3


atlantic_info = regions["Atlantic"]
lat1 = convert_latitude_to_index(atlantic_info["lat_range"][0])
lat2 = convert_latitude_to_index(atlantic_info["lat_range"][1])
lon1 = convert_longitude_to_index(atlantic_info["lon_range"][0])
lon2 = convert_longitude_to_index(atlantic_info["lon_range"][1])
lat_start, lat_end = sorted([lat1, lat2])
lon_start, lon_end = sorted([lon1, lon2])

atlantic_data = data[85:151, :, lat_start:lat_end, lon_start:lon_end]  # 1960–2025

# prep coords
atlantic_lats = latitudes[lat_start:lat_end]
atlantic_lons = longitudes[lon_start:lon_end]

# get 5-year ranges
start_years = np.arange(1960, 2026, 5)
co2_months_full = co2_years + (co2_months - 1) / 12
co2_full = co2_ppm

corr_maps = []
years_mid = []

for start in start_years[:-1]:
    end = start + 5
    years_mid.append((start + end) / 2)

    # co2 data slice
    co2_mask = (co2_months_full >= start) & (co2_months_full < end)
    co2_range = co2_full[co2_mask]

    # time indices for sst (quarterly)
    sst_start = (start - 1960) * 4
    sst_end = (end - 1960) * 4
    sst_chunk = atlantic_data[sst_start:sst_end]  # shape: (20, lat, lon)

    h, w = sst_chunk.shape[1:]
    corr_map = np.full((h, w), np.nan)

    for i in range(h):
        for j in range(w):
            ts = sst_chunk[:, i, j]
            if np.isnan(ts).any():
                continue
            ts_monthly = np.repeat(ts, 3)
            if len(ts_monthly) != len(co2_range):
                continue
            corr = compute_corr(ts_monthly, co2_range)
            corr_map[i, j] = corr

    corr_maps.append(corr_map)

# animate
fig, ax = plt.subplots(figsize=(8,6))
img = ax.imshow(corr_maps[0], cmap='jet', vmin=-1, vmax=1, extent=[
    atlantic_lons[0], atlantic_lons[-1], atlantic_lats[-1], atlantic_lats[0]
])
cbar = plt.colorbar(img, ax=ax)
cbar.set_label("Correlation Coefficient")
title = ax.set_title(f"Atlantic Grid-wise Correlation (Mid-Year: {years_mid[0]})")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

def update(frame):
    img.set_data(corr_maps[frame])
    title.set_text(f"Atlantic Grid-wise Correlation (Mid-Year: {years_mid[frame]})")
    return img, title

ani = animation.FuncAnimation(fig, update, frames=len(corr_maps), interval=800, blit=False)
ani.save("atlantic_correlation_heatmap.mp4", writer="ffmpeg")
plt.show()

