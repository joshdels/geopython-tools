from pathlib import Path
import processing


input_folder = Path(r"D:\1. PROJECT\landscaping-sensitivity\analysis\files")
output_folder = Path(r"D:\1. PROJECT\landscaping-sensitivity\analysis\clipped")
mask_layer = r"D:\1. PROJECT\landscaping-sensitivity\processdata_2026_2_5\boundary_basco.shp"


def raster_clip_qgis(input_folder, output_folder, mask_layer):
  ''' Uses qgis console to bacth clip a file folder path'''
    for raster in input_folder.glob("idw2_*.tif"):
        output = output_folder / f"clipped_{raster.name}"
        print(f"Processing: {raster.name}")
        processing.run(
            "gdal:cliprasterbymasklayer",
            {
                'INPUT': str(raster),
                'MASK': mask_layer,
                'CROP_TO_CUTLINE': True,
                'OUTPUT': str(output)
            }
        )

    print("Finished batch clipping.")
    
raster_clip_qgis(input_folder, output_folder, mask_layer)
