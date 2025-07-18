-- Creates the database hbtn_0d_usa on MySQL server
-- Creates the table cities in database hbtn_0d_usa
CREATES DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use database to create table
USE hbtn_0d_usa;
CREATES TABLES IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
PRIMARY KEY(id), 
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id));
