"""
Cleaning a bounday adm4
"""

from pathlib import Path
import geopandas as gpd

BASE_DIR = Path(__file__).resolve().parent.parent


def clean_ph_adm4_boundaries():
    """
    Removes all the null of the shapefile
    """

    # path
    gdf = gpd.read_file(
        "/home/joshua/Documents/03-Resources/GIS/boundary/phl_admin4.shp"
    )

    # Dropping tables
    gdf = gdf.drop(
        columns=[
            "center_lon",
            "center_lat",
            "lang3",
            "lang2",
            "lang1",
            "lang",
            "version",
            "adm4_name1",
            "adm3_name1",
            "adm2_name1",
            "adm4_name2",
            "adm4_name3",
            "valid_on",
            "valid_to",
            "area_sqkm",
            "adm3_name3",
            "adm0_name2",
            "adm0_name3",
            "adm0_pcode",
            "adm3_name2",
            "adm0_name1",
            "adm0_name",
            "adm4_ref_n",
        ]
    )
    gdf = gdf.dropna(axis=1, how="all")

    # Renames
    gdf = gdf.rename(
        columns={
            "adm4_name": "barangay_name",
            "adm3_name": "city_name",
            "adm2_name": "province_name",
            "adm1_name": "region_name",
            "adm4_pcode": "barangay_code",
            "adm3_pcode": "city_code",
            "adm2_pcode": "province_code",
            "adm1_pcode": "region_code",
            "geometry": "geom",
        }
    )

    print(gdf.columns)
    print(gdf.head())

    output_path = BASE_DIR / "data" / "output.gpkg"
    gdf.to_file(output_path, driver="GPKG")


clean_ph_adm4_boundaries()
