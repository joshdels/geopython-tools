import processing

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

    Parameters
    ----------
    first_range : int
        Starting field index for interpolation.

    last_range : int
        Ending field index (exclusive).

    input_path : str
        Path to the input vector dataset (e.g., shapefile or geopackage).

    output_prefix : str
        Prefix for the output raster files.

    extent : str
        Interpolation extent formatted as:
        'xmin,xmax,ymin,ymax [EPSG:code]'

    pixel_size : float, optional
        Output raster resolution (default = 0.0001).

    power : int, optional
        Distance coefficient for IDW interpolation (default = 2).

    Example
    -------
    process_idw(
        first_range=3,
        last_range=10,
        input_path="D:/data/points.shp",
        output_prefix="D:/outputs/idw",
        extent="121.9,122.0,20.4,20.5 [EPSG:4326]"
    )
    """

    for i in range(first_range, last_range):

        output_file = f"{output_prefix}_{i}.tif"

        params = {
            'INTERPOLATION_DATA': f'{input_path}::~::0::~::{i}::~::0',
            'DISTANCE_COEFFICIENT': power,
            'EXTENT': extent,
            'PIXEL_SIZE': pixel_size,
            'OUTPUT': output_file
        }

        processing.run("qgis:idwinterpolation", params)

        print(f"Finished interpolation for field index {i}")
