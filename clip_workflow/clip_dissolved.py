import geopandas as gpd


def process_clip(layer_path, border_path, column_dissolve):
    """
    Clip a vector layer using a border layer and dissolve the result.

    Parameters
    ----------
    layer_path : str
        File path to the input vector layer.
    border_path : str
        File path to the clipping boundary layer.
    column_dissolve : str
        Attribute column used for dissolving features.

    Returns
    -------
    None
        Saves the output file to 'output.shp'.

    Raises
    ------
    RuntimeError
        If input files cannot be read.
    """

    # Only try/except for input reading
    try:
        layer = gpd.read_file(layer_path)
        border = gpd.read_file(border_path)
    except Exception as e:
        raise RuntimeError(f"Failed to read input files: {e}") from e

    # CRS Check
    if layer.crs.to_epsg() != 4326:
        layer = layer.to_crs(epsg=4326)

    if border.crs.to_epsg() != 4326:
        border = border.to_crs(epsg=4326)

    # Fix invalid geometries
    layer["geometry"] = layer.geometry.make_valid()
    border["geometry"] = border.geometry.make_valid()

    # Clip operation
    clipped_layer = gpd.clip(layer, border)

    # Dissove operation
    result = clipped_layer.dissolve(by=column_dissolve)

    result.to_file("output.shp")
