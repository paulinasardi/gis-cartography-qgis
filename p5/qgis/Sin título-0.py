from osgeo import gdal
import numpy as np

src = gdal.Open(r'C:/Users/Usuario/OneDrive/Escritorio/paulina_sardi/PHASE 1/data/p5/data_raw/lulc_final.tif')
arr = src.GetRasterBand(1).ReadAsArray()
pixel_size = 10
pixel_area_ha = (pixel_size * pixel_size) / 10000

clases = {
    0: "Sin datos",
    1: "Viñedos / Cultivos",
    2: "Suelo árido",
    3: "Nieve / Urbano",
    4: "Agua / Canales",
    5: "Nubes / Sombras"
}

print(f"{'Valor':<8} {'Clase':<25} {'Píxeles':<12} {'Hectáreas':<12}")
print("-" * 57)
for val, nombre in clases.items():
    count = np.sum(arr == val)
    ha = count * pixel_area_ha
    print(f"{val:<8} {nombre:<25} {count:<12} {ha:.1f}")

src = None

print("Total píxeles:", arr.size)
print("Total hectáreas:", arr.size * 100 / 10000)
