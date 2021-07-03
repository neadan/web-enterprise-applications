CREATE TABLE webapp2.bike(
	id SERIAL PRIMARY KEY,
	bike_type varchar(10),
	color varchar(10)
)

CREATE TABLE webapp2.renter(
	id SERIAL PRIMARY KEY,
	first_name varchar(30),
	last_name varchar(30),
	phone varchar(30),
	vip_num int
)

CREATE TABLE webapp2.rental(
	id SERIAL PRIMARY KEY,
	bike int references webapp2.bike(id),
	renter int references webapp2.renter(id),
	rental_date date,
	price decimal(4,2)
)

INSERT INTO webapp2.bike(bike_type, color) VALUES ('Honda', 'Green')
INSERT INTO webapp2.bike(bike_type, color) VALUES ('BMW', 'Blue')

INSERT INTO webapp2.renter(first_name, last_name, phone, vip_num) VALUES ('John', 'Doe', '5148783453', 123)
INSERT INTO webapp2.renter(first_name, last_name, phone, vip_num) VALUES ('Jane', 'Doe', '5149870980', 456)

SELECT * FROM webapp2.bike
SELECT * FROM webapp2.renter

INSERT INTO webapp2.rental(bike, renter, rental_date, price) VALUES(
	(SELECT id FROM webapp2.bike WHERE bike_type='Honda'),
	(SELECT id FROM webapp2.renter WHERE first_name='Jane'),
	'2021-07-03',
	99.99
)

INSERT INTO webapp2.rental(bike, renter, rental_date, price) VALUES(
	(SELECT id FROM webapp2.bike WHERE bike_type='BMW'),
	(SELECT id FROM webapp2.renter WHERE first_name='John'),
	'2021-07-03',
	89.99
)

SELECT rt.first_name, rt.last_name, rn.rental_date, rn.price, bk.bike_type, bk.color, rt.phone, rt.vip_num FROM webapp2.rental rn
INNER JOIN webapp2.bike bk ON rn.bike = bk.id
INNER JOIN webapp2.renter rt ON rn.renter = rt.id