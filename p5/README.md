# TP5 — Advanced Spectral Indexes & K-means Classification
## Valle de Uco, Mendoza, Argentina | Sentinel-2 L2A | February 2026

### Overview
Unsupervised land cover classification of Valle de Uco (Mendoza, Argentina) 
using K-means clustering and advanced spectral indexes. The study area covers 
the departments of Tunuyán, Tupungato, and San Carlos — one of Argentina's 
most important wine-producing regions.

---

### Study Area
- **Zone:** Valle de Uco, Mendoza, Argentina
- **Departments:** Tunuyán, Tupungato, San Carlos
- **Sensor:** Sentinel-2 L2A (S2C)
- **Tile:** T19HDC
- **Date:** February 28, 2026
- **CRS:** EPSG:32719 (WGS 84 / UTM Zone 19S)

---

### Workflow

1. **Band download & resampling** — 7 bands downloaded from Copernicus Browser (.SAFE format). Bands B8A, B11, B12 resampled from 20m to 10m using Warp (Nearest Neighbor) in QGIS.
2. **AOI clip** — All bands clipped to Tunuyán department boundary (GADM level 2).
3. **Multiband stack** — 7-band composite created with QGIS Raster → Miscellaneous → Merge.
4. **K-means clustering** — Ran with SCP plugin: 5 classes and 20 classes, 50 iterations, distance threshold 0.0001.
5. **LULC reclassification** — 20 spectral classes reclassified to 5 land cover classes using GDAL/Python (r.reclass + manual Python script).
6. **Spectral indexes** — EVI, SAVI, NBR, NDWI calculated with QGIS Raster Calculator.
7. **Cross-validation** — Mean index values per LULC class e
