import processing
from pathlib import Path

def process_idw(
    first_range: int,
    last_range: int,
    input_path: str,
    output_prefix: str,
    extent: str,
    pixel_size: float = 0.0001,
    power: int = 2
):
    """
    Batch IDW interpolation for multiple attribute fields by index in QGIS console.
    Includes error handling and logging.
    """

    input_file = Path(input_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input dataset not found: {input_path}")

    if first_range >= last_range:
        raise ValueError("first_range must be smaller than last_range")

    output_dir = Path(output_prefix).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Starting IDW batch interpolation...")
    print(f"Input layer: {input_path}")
    print(f"Output directory: {output_dir}")
    print(f"Field index range: {first_range} → {last_range-1}")
    print("-" * 50)

    for i in range(first_range, last_range):

        output_file = f"{output_prefix}_{i}.tif"

        params = {
            'INTERPOLATION_DATA': f'{input_path}::~::0::~::{i}::~::0',
            'DISTANCE_COEFFICIENT': power,
            'EXTENT': extent,
            'PIXEL_SIZE': pixel_size,
            'OUTPUT': output_file
        }

        try:
            processing.run("qgis:idwinterpolation", params)

            if Path(output_file).exists():
                print(f"Finished interpolation for field index {i}")
            else:
                print(f"Processing finished but output missing for field {i}")

        except Exception as e:
            print(f"Failed interpolation for field index {i}")
            print(f"Error: {e}")
            continue

    print("-" * 50)
    print("IDW batch process completed.")


process_idw(
    first_range=4,
    last_range=18,
    input_path="D:/1. PROJECT/landscaping-sensitivity/analysis/assesement1.shp",
    output_prefix="D:/1. PROJECT/landscaping-sensitivity/analysis/files3/idw",
    extent="121.935805233,122.045070598,20.408186889,20.508964125 [EPSG:4326]"
)
