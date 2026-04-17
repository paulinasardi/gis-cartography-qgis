# TP5 — Advanced Spectral Indexes & K-means Classification 🛰️
## Valle de Uco, Mendoza, Argentina | Sentinel-2 L2A | February 2026

### 🌍 Overview
Unsupervised land cover classification of Valle de Uco (Mendoza, Argentina) 
using K-means clustering and advanced spectral indexes. The study area covers 
the departments of Tunuyán, Tupungato, and San Carlos — one of Argentina's 
most important wine-producing regions.

---

### 📍 Study Area
- **Zone:** Valle de Uco, Mendoza, Argentina
- **Departments:** Tunuyán, Tupungato, San Carlos
- **Sensor:** Sentinel-2 L2A (S2C)
- **Tile:** T19HDC
- **Date:** February 28, 2026
- **CRS:** EPSG:32719 (WGS 84 / UTM Zone 19S)

---

### ⚙️ Workflow

1. **Band download & resampling** — 7 bands downloaded from Copernicus Browser (.SAFE format). Bands B8A, B11, B12 resampled from 20m to 10m using Warp (Nearest Neighbor) in QGIS.
2. **AOI clip** — All bands clipped to Tunuyán department boundary (GADM level 2).
3. **Multiband stack** — 7-band composite created with QGIS Raster → Miscellaneous → Merge.
4. **K-means clustering** — Ran with SCP plugin: 5 classes and 20 classes, 50 iterations, distance threshold 0.0001.
5. **LULC reclassification** — 20 spectral classes reclassified to 5 land cover classes using GDAL/Python.
6. **Spectral indexes** — EVI, SAVI, NBR, NDWI calculated with QGIS Raster Calculator.
7. **Cross-validation** — Mean index values per LULC class extracted with Python/GDAL.

---

### 🛰️ Bands Used
| Band | Resolution | Description |
|------|-----------|-------------|
| B02 | 10m | Blue |
| B03 | 10m | Green |
| B04 | 10m | Red |
| B08 | 10m | NIR |
| B8A | 20m → 10m | Narrow NIR |
| B11 | 20m → 10m | SWIR 1 |
| B12 | 20m → 10m | SWIR 2 |

---

### 🗺️ LULC Classes & Colors
| Value | Class | HEX |
|-------|-------|-----|
| 1 | Vineyards / Crops | #4E9B47 |
| 2 | Arid Soil | #C8A96E |
| 3 | Snow / Urban / High Reflective | #E8E8E8 |
| 4 | Water / Canals | #2E86AB |
| 5 | Clouds / Shadows | #B0B7C3 |
| 0 | No Data | #1A1A1A |

---

### 📊 Area by Class
| Class | Pixels | Hectares |
|-------|--------|----------|
| Vineyards / Crops | 12,802,668 | 128,026 ha |
| Arid Soil | 70,616 | 706 ha |
| Snow / Urban | 18,040,860 | 180,408 ha |
| Water / Canals | 99,740 | 997 ha |
| Clouds / Shadows | 292,476 | 2,924 ha |
| No Data | 65,376,490 | 653,764 ha |
| **Total** | **96,682,850** | **966,828 ha** |

---

### 🔢 Reclassification Table
| Min | Max | New Value | Class |
|-----|-----|-----------|-------|
| 0 | 1 | 0 | No Data |
| 2 | 2 | 1 | Vineyards / Crops |
| 3 | 4 | 3 | Snow / Urban |
| 5 | 5 | 0 | No Data |
| 6 | 6 | 5 | Clouds / Shadows |
| 7 | 7 | 0 | No Data |
| 8 | 8 | 4 | Water / Canals |
| 9 | 15 | 2 | Arid Soil |
| 16 | 19 | 0 | No Data |

---

### 📐 Spectral Indexes
| Index | Formula |
|-------|---------|
| EVI | 2.5 × (B08 - B04) / (B08 + 6×B04 - 7.5×B02 + 1) |
| SAVI | ((B08 - B04) / (B08 + B04 + 0.5)) × 1.5 |
| NBR | (B08 - B12) / (B08 + B12) |
| NDWI | (B03 - B08) / (B03 + B08) |

---

### ✅ Cross-Validation — K-means vs Spectral Indexes
| Class | EVI | SAVI | NBR | NDWI |
|-------|-----|------|-----|------|
| Vineyards / Crops | 0.354 | 0.217 | 0.084 | -0.188 |
| Arid Soil | -0.042 | 0.016 | 0.133 | -0.015 |
| Snow / Urban | 0.351 | 0.218 | 0.067 | -0.203 |
| Water / Canals | -0.003 | 0.007 | 0.148 | -0.005 |
| Clouds / Shadows | -0.040 | 0.032 | 0.102 | -0.034 |

**Key findings:**
- 🌿 Vineyards/Crops show high EVI (0.354), confirming dense active vegetation
- 🏜️ Arid Soil shows negative EVI (-0.042), confirming bare soil with no vegetation
- 💧 Water/Canals show near-zero NDWI, consistent with limited water presence in the AOI
- ⚠️ Snow/Urban spectral confusion with Vineyards is documented — inherent limitation of February imagery at this elevation

---

### ⚠️ Known Limitations
- Vineyards and Arid Soil share similar spectral signatures in February — EVI/SAVI cross-validation helps distinguish them
- Snow/Urban shows spectral confusion with Vineyards due to high reflectance values
- Urban areas are distributed across multiple K-means classes — inherent limitation of unsupervised classification
- Clouds and shadows are classified as a single class

---

### 📁 Outputs
- `lulc_final.tif` — LULC reclassified raster (5 classes)
- `EVI.tif` — Enhanced Vegetation Index
- `SAVI.tif` — Soil Adjusted Vegetation Index
- `NBR.tif` — Normalized Burn Ratio
- `NDWI.tif` — Normalized Difference Water Index
- `TP5_LULC_Classification_ValleDeUco.png` — LULC vs K-means comparison map
- `TP5_Spectral_Indexes_ValleDeUco.png` — Spectral indexes comparison map
- `cross_validation_indexes.csv` — Mean index values per LULC class

---

### 🛠️ Tools & Plugins
- QGIS 3.x
- SCP (Semi-Automatic Classification Plugin)
- GDAL / Python

### 📡 Data Sources
- ESA Sentinel-2 L2A — Copernicus Browser
- AOI boundary — GADM Argentina level 2