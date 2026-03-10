# GmE 221 – Laboratory Exercise 3

## Overview
This laboratory performs a 3D computational modeling workflow by integrating vector road data and raster elevation data using Python. Road geometries are retrieved from PostGIS, while a Digital Elevation Model (DEM) is loaded from a GeoTIFF file. The road lines are densified to create sample points, and elevation values from the DEM are sampled at each vertex. The final output is exported as a GeoJSON file containing 3D road geometries for visualization in QGIS.

---

## How to Run 
1. Activate the virtual environment 
2. Run `analysis.py` to execute 3D geometry construction
3. Load the generated files in QGIS 

---

## Outputs 
- road_sample_points.shp
- roads_3d.geojson

---

## Reflection

**Hybrid IO**

Roads are retrieved from PostGIS because spatial databases are designed to store and manage large vector datasets efficiently while supporting querying and indexing.

In contrast, the DEM is loaded directly from a raster file. This is because raster datasets such as elevation models are typically stored as grid-based formats like GeoTIFF.

Because of this difference, the workflow uses a hybrid IO approach. Hybrid IO reflects real-world GIS architecture because spatial systems often store different types of data in different storage environments depending on their structure and use. Vector data like roads are usually kept in databases such as PostGIS for better management and querying, while raster data like satellite images or DEMs are stored as files because they have a gridded structure. Python then acts as the tool that brings these different data sources together so they can be processed together in a single workflow.

At this point in the exercise, no spatial analysis is happening yet. This stage only represents the Input part of the Input–Process–Output framework. The datasets are simply being loaded into Python and checked to make sure things like geometry, coordinate systems, and raster properties are correct before any spatial calculations are performed in the next stage.


**3D Geometry Construction**

Densification is necessary because a road LineString may contain only a few vertices, which would result in a very coarse representation of the terrain if elevation were sampled only at those points. By having additional points at regular intervals along the line, the algorithm captures more elevation samples from the DEM. This produces a more accurate 3D representation of the road surface.

Before sampling the elevation, the coordinate systems must match. CRS alignment is important because both the road data and the DEM must use the same coordinate reference system so their locations line up correctly. If they use different CRS definitions, the road points could be matched to the wrong cells in the DEM, which would give incorrect elevation values.

Once the sampling is done, the geometry now includes a Z coordinate, which represents elevation. It now stores height information taken from the DEM, allowing it to represent the terrain in three dimensions.


**3D GeoJSON**

When exporting 3D geometry to GeoJSON, the coordinate structure is kept the same, including the third value that represents elevation. This means the height information from the DEM is saved directly inside the geometry coordinates.

However, even though the elevation values are stored, GeoJSON does not really treat the geometry as a fully 3D object. The format does not have special geometry types for 3D shapes, so the data is still labeled as a normal LineString, even if it contains elevation values.

GeoJSON still labels the geometry as "LineString" even when Z exists because its standard mainly defines geometry types in two dimensions. It allows a third coordinate value, but it does not create a separate type like LineStringZ. This shows the difference between the data content and data standard—the dataset may store 3D information, even though the format’s standard does not explicitly represent it as a true 3D geometry type.

Despite this limitation, QGIS can still visualize the geometry with elevation. This is usually considered 2.5D, meaning the line can appear raised or lowered based on the stored Z values, but the geometry is not treated as a full 3D object with complex spatial relationships.

Because of this, other formats might be better for working with true 3D spatial data. For example, if we wish to represent more complex 3D objects such as buildings with walls and roofs, formats like glTF might be more suitable. This can describe full 3D structures rather than just geometries with a Z coordinate.