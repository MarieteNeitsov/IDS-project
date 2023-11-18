import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import numpy as np


df = pd.read_csv('Liiklusõnnetused_2011_2021.csv')
columns_to_drop = ['Maja nr (PPA)', 'Ristuv tänav (PPA)', 'Asula','Tee tüüp [1]','Tee nr (PPA)','Tee km (PPA)',]
df.drop(columns=columns_to_drop, inplace=True)
print(df.head())

print(df.columns)

#column_types = df.dtypes
#for column_name, data_type in column_types.items():
#    if data_type == 'object': 
#        unique_values = df[column_name].unique()
#        print(f"Unique values for column '{column_name}': {unique_values}")

#df['Liiklusõnnetuse liik [3]'].value_counts().plot(kind='bar')

#plt.title('Accident Types')
#plt.xlabel('Accident Type')
#plt.ylabel('Count')
#plt.xticks(rotation=45, ha='right')
#plt.tight_layout()


#plt.show()

print(df['Liiklusõnnetuse liik [1]'].unique())

import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

folder_path = 'geop/'
shapefile_path = folder_path + 'ne_10m_admin_1_states_provinces.shp'

boundaries = gpd.read_file(shapefile_path)

estonia = boundaries[boundaries['admin'] == 'Estonia']

X_column = 'GPS X'
Y_column = 'GPS Y'

# drop rows with missing X or Y values
accidents_df = df.dropna(subset=[X_column, Y_column])

geometry = [Point(xy) for xy in zip(accidents_df[Y_column], accidents_df[X_column])]
geo_df = gpd.GeoDataFrame(accidents_df,geometry=geometry)


# Set the current crs of your geodataframe
geo_df.set_crs(epsg=3301, inplace=True)
# convert the geodataframe to the same crs as the boundaries
geo_df = geo_df.to_crs(epsg=4326)

fig, ax = plt.subplots(figsize=(10, 10))

estonia.plot(ax=ax, color='white', edgecolor='black')

# different colors for different accident types
geo_df.plot(ax=ax, alpha=0.5,column='Liiklusõnnetuse liik [1]', legend=True, legend_kwds={'bbox_to_anchor': (1, 1)}, markersize=10)

plt.show()


