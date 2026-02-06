import os
import geopandas as gpd


def dissolve_shp_to_single_geojson(input_path, output_path):
    """
    Dissolve all geometries into one and optionally keep a single field.
    """
    try:
        gdf = gpd.read_file(input_path)
        print("Original data:")
        print(gdf.head())

        dissolved_shp = gdf.dissolve()
        dissolved_shp.to_file(output_path, driver="geojson")

        print("Successfully dissolved the file")
    except Exception as e:
        print("An error occurred:", e)
        raise


# dissolve_shp_to_single_geojson("data/boundary.shp", "data_process/dissolved.geojson")


def clip_data_to_area_study(boundary_path, data_path, output_folder="data_process"):
    """Clip the input data to the area study boundary and save it with the same name in output folder."""
    try:
        boundary_name = os.path.basename(boundary_path)
        data_name = os.path.basename(data_path)
        output_name = data_name.replace(" ", "_")
        output_path = os.path.join(output_folder, output_name)

        print("Boundary file:", boundary_name)
        print("Data file:", data_name)
        print("Output file:", output_path)

        boundary = gpd.read_file(boundary_path)
        data = gpd.read_file(data_path)

        if data.crs != boundary.crs:
            print("CRS mismatch, reprojecting data to match boundary CRS...")
            data = data.to_crs(boundary.crs)

        clipped_data = gpd.clip(data, boundary.geometry)
        clipped_data.to_file(output_path)
        print("Successfully clipped the data!")

    except Exception as e:
        print("An error occurred:", e)


# List of shapefiles in the "data" folder
shp_files = [
    "litology.shp",
    # "land_management.shp",
    # "land_classification.shp",
    # "geological.shp",
    # "soil_type.shp",
    # "slope.shp",
]

for shp_file in shp_files:
    file_path = os.path.join("data", shp_file)
    clip_data_to_area_study(
        boundary_path="data_process/dissolved.geojson", data_path=file_path
    )
