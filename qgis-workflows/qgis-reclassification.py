from pathlib import Path
import processing


input_folder = Path(r"D:\1. PROJECT\landscaping-sensitivity\analysis\clipped")
output_folder = Path(r"D:\1. PROJECT\landscaping-sensitivity\analysis\reclassified")

output_folder.mkdir(parents=True, exist_ok=True)


def process_reclassification(input_folder, output_folder):
    """Uses qgis console to batch reclassify raster data"""

    rasters = list(input_folder.glob("clipped_*tif"))

    if not rasters:
        print("No raster files fount in the folder.")
        return

    for raster in input_folder.glob("clipped_*.tif"):
        output = output_folder / f"reclass_{raster.name}"

        params = {
            "INPUT_RASTER": str(raster),
            "RASTER_BAND": 1,
            "TABLE": [
                1.0,
                1.8,
                1,
                1.8,
                2.6,
                2,
                2.6,
                3.4,
                3,
                3.4,
                4.2,
                4,
                4.2,
                5.0,
                5,
            ],
            "NO_DATA": -9999,
            "RANGE_BOUNDARIES": 1,
            "NODATA_FOR_MISSING": False,
            "DATA_TYPE": 5,
            "CREATE_OPTIONS": None,
            "OUTPUT": str(output),
        }

        processing.run("native:reclassifybytable", params)

    print("reclassification completed")


process_reclassification(input_folder, output_folder)
