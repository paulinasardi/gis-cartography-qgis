# TP04 — NDVI Comparison: Sentinel-2 vs Landsat 9 | Anguil, La Pampa

## Project Goal
Compare NDVI calculated from Sentinel-2 (10m resolution) and Landsat 9 (30m resolution) 
over an active agricultural zone in La Pampa, Argentina, to analyze the spatial detail 
differences between both sensors.

## Study Area
Agricultural zone between Anguil, Catriló and Trenel, La Pampa, Argentina.
Presence of INTA EEA Anguil. Crops: soy, sunflower, wheat and maize.
Parcel sizes of 50–200 ha make resolution differences meaningful.

## Tools Used
- QGIS 3.x
- Copernicus Browser (Sentinel-2 L2A)
- USGS Earth Explorer (Landsat 9 C2 L2)
- Raster Calculator (NDVI formula)
- SCP Plugin

## Data
| Sensor | Date | Resolution | Bands |
|---|---|---|---|
| Sentinel-2 L2A | 14/03/2025 | 10m | B04, B08 |
| Landsat 9 C2 L2 | 17/03/2025 | 30m | SR_B4, SR_B5 |

## Outputs
- NDVI map Sentinel-2 (RdYlGn, range -0.2 to 0.8)
- NDVI map Landsat 9 (RdYlGn, range -0.2 to 0.8)
- Vegetation Stress mask (NDVI < 0.3) for both sensors
- NDVI histograms for both sensors

## PNG Preview
![NDVI Sentinel](outputs/NDVI_Sentinel_Anguil.png)
![NDVI Landsat](outputs/NDVI_Landsat_Anguil.png)

## Key Finding
Landsat 30m pixels mix vegetation and bare soil within the same pixel, 
lowering average NDVI values and generating more vegetation stress detections 
than Sentinel-2. Sentinel resolves individual parcel boundaries clearly, 
while Landsat generalizes them.

## What I Learned
- Downloading and processing Sentinel-2 and Landsat 9 imagery
- Reprojecting rasters to UTM Zone 20S (EPSG:32720)
- Calculating NDVI with Raster Calculator in QGIS
- Creating vegetation stress masks
- Comparing spatial resolution effects on index values
- Professional cartographic layout design in QGIS Print Layout