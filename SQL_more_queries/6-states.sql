-- Creates the Database hbtn_0d_usa on MySQL server
-- Creates the table states in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use database hbtn_0d_usa
USE hbtn_0d_usa;
-- Creates a tab;e
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
