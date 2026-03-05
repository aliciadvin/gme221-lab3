Title and overview

How to run analysis.py

Outputs expected in output/

Commit milestones and reflections

Hybrid IO Reflection
- Why are roads retrieved from PostGIS instead of file?
- Why is the DEM loaded directly from a raster file?
- How does hybrid IO reflect real-world GIS architecture?
- Is spatial analysis occurring at this stage?

3D Geometry Construction Reflection
- Why densification is necessary
- Why CRS alignment must happen before sampling
- What it means that geometry now contains Z values (not symbolic extrusion)

3D GeoJSON Reflection
- What is preserved when you export 3D geometry to GeoJSON? (Hint: coordinate structure)
- What is lost or not formally expressed? (Hint: GeoJSON geometry type system)
- Why does GeoJSON still label the geometry as "LineString" even when Z exists? 
What does this tell you about the difference between data content and data standard?
- How does this affect visualization in QGIS 3D View?
Does QGIS treat this as true 3D geometry or as 2.5D visualization?
- If you had to preserve 3D semantics more explicitly, what alternative output formats would you consider?
(Examples: GeoPackage, PostGIS storage, 3D Tiles / glTF pipelines—just name reasonable options)