DROP DATABASE imp;
CREATE DATABASE imp;
USE imp;

SET SESSION storage_engine = "InnoDB";
SET SESSION time_zone = "+0:00";
ALTER DATABASE CHARACTER SET "utf8";

CREATE TABLE Organization (
    org_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    acronym VARCHAR(100),
    found_date VARCHAR(100),
    site_url VARCHAR(100),
    _type INT,  
    #0 for "Private sector",1 for "Government Agency",2 for "Multilateral Organization"
    numberOfemployees INT,
    phoneNumber VARCHAR(100),
    country_code VARCHAR(100)
);

CREATE TABLE Users (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    gender INT,  #0 for Male,1 for Female
    mail VARCHAR(100) NOT NULL,
    target_population VARCHAR(100),
    location VARCHAR(100),
    work_field VARCHAR(100),
    language VARCHAR(100),
    street VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    post_code VARCHAR(100),
    country VARCHAR(100),
    mobile VARCHAR(100),
    mobile_code VARCHAR(100),
    skype VARCHAR(100),
    passwd VARCHAR(100),
    register_date TIMESTAMP,
    avatar VARCHAR(1000),
    org_id INT,
	UNIQUE KEY (mail),
 	FOREIGN KEY (org_id) REFERENCES Organization(org_id)
);

CREATE TABLE Admins (
	admin_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    mail VARCHAR(100) NOT NULL,
    passwd VARCHAR(100)
);

CREATE TABLE Activate_Events (
	mail VARCHAR(100) NOT NULL PRIMARY KEY,
	_id   VARCHAR(100),
	create_time VARCHAR(100)
);

CREATE TABLE Active_Users (
    user_id INT NOT NULL PRIMARY KEY,
    time TIMESTAMP 
);

CREATE TABLE Follow_Status (
    mail_from VARCHAR(100) NOT NULL,
    mail_to VARCHAR(100) NOT NULL,
    time TIMESTAMP,
    PRIMARY KEY(mail_from,mail_to),
	FOREIGN KEY (mail_from) REFERENCES Users(mail),
	FOREIGN KEY (mail_to) REFERENCES Users(mail)
);

CREATE TABLE Recent_Events (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    _type VARCHAR(100), #Follow_Status, Offers, Needs, Events
	typeId INT,
    _date TIMESTAMP,
    _from VARCHAR(100),
    _to VARCHAR(100),
	followed INT,
	FOREIGN KEY (_from) REFERENCES Users(mail),	
	FOREIGN KEY (_to) REFERENCES Users(mail)
);

CREATE TABLE Offers (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	mail VARCHAR(100) NOT NULL,
	title VARCHAR(100),
	description VARCHAR(500),
	location VARCHAR(100),
	target_population VARCHAR(100),
    time TIMESTAMP,
	followed INT,
	FOREIGN KEY (mail) REFERENCES Users(mail)
);

CREATE TABLE Needs (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	mail VARCHAR(100) NOT NULL,
	title VARCHAR(100),
	description VARCHAR(500),
	location VARCHAR(100),
	target_population VARCHAR(100),
    time TIMESTAMP,
	followed INT,
	FOREIGN KEY (mail) REFERENCES Users(mail)
);

CREATE TABLE Events (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	mail VARCHAR(100) NOT NULL,
	title VARCHAR(100),
	description VARCHAR(500),
	location VARCHAR(100),
	work_field VARCHAR(100),
	target_population VARCHAR(100),
	start_date VARCHAR(100),
	end_date VARCHAR(100),
    time TIMESTAMP,
	followed INT,
	FOREIGN KEY (mail) REFERENCES Users(mail)
);
