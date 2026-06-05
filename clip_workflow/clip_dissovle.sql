DROP TABLE IF EXISTS output;

CREATE TABLE output AS
WITH
layer_4326 AS (
    SELECT id, column_dissolve,
           ST_Transform(geom, 4326) AS geom
    FROM layer
),
border_4326 AS (
    SELECT ST_Transform(geom, 4326) AS geom
    FROM border
)

SELECT
    l.column_dissolve,
    ST_Union(
        ST_Intersection(l.geom, b.geom)
    ) AS geom
FROM layer_4326 l
CROSS JOIN border_4326 b
WHERE ST_Intersects(l.geom, b.geom)
GROUP BY l.column_dissolve;