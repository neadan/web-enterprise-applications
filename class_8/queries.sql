CREATE TABLE webapp2.country(
	id SERIAL PRIMARY KEY,
	country_name varchar(128),
	country_name_eng varchar(128),
	country_code char(3)
)

INSERT INTO webapp2.country(country_name, country_name_eng, country_code) VALUES ('Espana', 'Spain', 'ESP')
INSERT INTO webapp2.country(country_name, country_name_eng, country_code) VALUES ('Deutsche', 'Germany', 'GER')
SELECT * FROM webapp2.country

CREATE TABLE webapp2.city(
	id SERIAL PRIMARY KEY,
	city_name varchar(128),
	lat decimal(9,6),
	long decimal(9,6),
	country_id int references webapp2.country(id)
)

SELECT * FROM webapp2.country

INSERT INTO webapp2.city(city_name, lat, long, country_id) VALUES(
	'Barcelona',
	41.3851,
	2.1734,
	1
)

INSERT INTO webapp2.city(city_name, lat, long, country_id) VALUES(
	'Berlin',
	52.5200,
	13.4050,
	(SELECT id from webapp2.country WHERE country_name='Deutsche')
)

SELECT * FROM webapp2.city

SELECT * FROM webapp2.country ct
INNER JOIN webapp2.city ci
ON ct.id = ci.country_id