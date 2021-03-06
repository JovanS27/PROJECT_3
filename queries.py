gp_practice_query = """
DROP TABLE IF EXISTS gp_practice;
CREATE TABLE gp_practice (
    index INT PRIMARY KEY,
    gp_practice VARCHAR(50),
    latitude NUMERIC,
    longitude NUMERIC,
	asthma_percentage DECIMAL,
    aqi DECIMAL,
	co DECIMAL,
	no DECIMAL,
	no2 DECIMAL,
	o3 DECIMAL,
	so2 DECIMAL,
	pm2_5 DECIMAL,
	pm10 DECIMAL,
	nh3 DECIMAL
);
"""

air_pollution_query="""
DROP TABLE IF EXISTS air_pollution_data;

CREATE TABLE air_pollution_data (
    index INT PRIMARY KEY,
    date INT,
    air_quality_index DECIMAL,
	carbon_monoxide DECIMAL,
	nitrogen_monoxide DECIMAL,
	nitrogen_dioxide DECIMAL,
	ozone DECIMAL,
	sulphur_dioxide DECIMAL,
	ammonia DECIMAL,
	particultes_pm2_5 DECIMAL,
	particulates_pm_10 DECIMAL,
    practice_name VARCHAR(50)
);
"""

national_gp_query = """
DROP TABLE IF EXISTS national_gp;
CREATE TABLE national_gp (
    index INT PRIMARY KEY,
    gp_practice VARCHAR(50),
    latitude NUMERIC,
    longitude NUMERIC,
	asthma_percentage DECIMAL,
    aqi DECIMAL,
	co DECIMAL,
	no DECIMAL,
	no2 DECIMAL,
	o3 DECIMAL,
	so2 DECIMAL,
	pm2_5 DECIMAL,
	pm10 DECIMAL,
	nh3 DECIMAL
);
"""

national_air_pollution_query="""
DROP TABLE IF EXISTS national_air_pollution;

CREATE TABLE national_air_pollution (
    index INT PRIMARY KEY,
    date INT,
    air_quality_index DECIMAL,
	carbon_monoxide DECIMAL,
	nitrogen_monoxide DECIMAL,
	nitrogen_dioxide DECIMAL,
	ozone DECIMAL,
	sulphur_dioxide DECIMAL,
	ammonia DECIMAL,
	particultes_pm2_5 DECIMAL,
	particulates_pm_10 DECIMAL,
    practice_name VARCHAR(50)
);
"""