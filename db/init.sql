# db/init.sql
CREATE TABLE co2_data (
  id SERIAL PRIMARY KEY,
  lat DOUBLE PRECISION,
  lon DOUBLE PRECISION,
  taux_co2 DOUBLE PRECISION
);

ALTER TABLE co2_data ADD COLUMN geom GEOGRAPHY(Point, 4326);
UPDATE co2_data SET geom = ST_SetSRID(ST_MakePoint(lon, lat), 4326);