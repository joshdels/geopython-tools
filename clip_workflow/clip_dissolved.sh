#!/bin/bash

set -e

# CONFIGS
LAYER="input.shp"
BORDER="border.shp"
TMP_LAYER="layer_4326.gpkg"
TMP_BORDER="border_4326.gpkg"
CLIPPED="clipped.gpkg"
OUTPUT="output.gpkg"


echo "Reprojecting inputs to EPSG:4326..."

ogr2ogr -t_srs EPSG:4326 "$TMP_LAYER" "$LAYER"
ogr2ogr -t_srs EPSG:4326 "$TMP_BORDER" "$BORDER"


echo "Clipping layer..."

ogr2ogr -f GPKG "$CLIPPED" "$TMP_LAYER" \
  -clipsrc "$TMP_BORDER"


echo "Dissolving..."

ogr2ogr -f GPKG "$OUTPUT" "$CLIPPED" \
  -dialect SQLITE \
  -sql "
    SELECT
      $column_dissolve,
      ST_Union(geometry) AS geometry
    FROM clipped
    GROUP BY $column_dissolve
  "


echo "Done -> $OUTPUT"