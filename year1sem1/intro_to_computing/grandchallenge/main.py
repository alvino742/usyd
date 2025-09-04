import h5py
import pandas as pd
import numpy as np

# Path to the HDF5 file
file_path = 'SMAP_L2_SM_P_NRT_54911_D_20250513T035531_N17701_002.h5'

# Open the file and access data
with h5py.File(file_path, 'r') as f:
    group = f['Soil_Moisture_Retrieval_Data']
    
    # Load selected datasets
    lat = group['latitude'][:]
    lon = group['longitude'][:]
    sm = group['soil_moisture'][:]
    temp = group['surface_temperature'][:]
    
# Convert to DataFrame (flattened)
df = pd.DataFrame({
    'latitude': lat.flatten(),
    'longitude': lon.flatten(),
    'soil_moisture': sm.flatten(),
    'surface_temperature': temp.flatten()
})

# Clean invalid values
df.replace(-9999, np.nan, inplace=True)
df.dropna(inplace=True)

# Show a sample
print(df.sample(10))
