import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('locations.csv')
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

ax=world.plot(figsize=(10, 6))
gdf.plot(ax=ax, marker='o', color='red', markersize=15);
plt.savefig("truck locations.png")
