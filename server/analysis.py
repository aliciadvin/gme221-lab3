import geopandas as gpd 
import rasterio
from sqlalchemy import create_engine 

# Database connection parameters 
host = "localhost" 
port = "5432" 
dbname = "gme221_exer3" 
user = "postgres" 
password = "spatialalicia7" 

# Create the connection string 
conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}" 

# Create SQLAlchemy engine 
engine = create_engine(conn_str)

# Minimal SQL queries (no spatial operations) 
sql_roads = "SELECT gid, geom FROM public.roads"

roads = gpd.read_postgis(sql_roads, engine, geom_col="geom")
# IMPORTANT: attach CRS (Geopandas often reads PostGIS geometry without CRS) 
# # Replace 3123 with the SRID from: SELECT ST_SRID(geom) FROM public.roads LIMIT 1;)

roads = roads.set_crs(epsg=3123, allow_override=True)

print(roads.head()) 
print(roads.crs) 
print(roads.geometry.type.unique())

dem = rasterio.open("data/dem.tif")
print("DEM CRS:", dem.crs) 
print("DEM Resolution:", dem.res) 
print("DEM Bounds:", dem.bounds)