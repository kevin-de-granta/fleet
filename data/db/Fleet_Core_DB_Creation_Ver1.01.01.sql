/*
File name:    Fleet_Core_DB_Creation.sql
Function:     To create user, database, and grant privilege(s)
Created by:   W. Wang (Kevin), ww288@cantab.net
Created on:   2017/10/01
*/

-- K2K: I have finished database creation in my development enviroment.

-- variables
-- please assign values to these variables firstly
DECLARE @userName VARCHAR(50), @userPasswd VARCHAR(50)
SET @userName='xxxxx'
SET @userPasswd='xxxxx'

-- create user
CREATE USER @userName@'%' IDENTIFIED BY @userPasswd;

-- create database
CREATE DATABASE FleetCore;

-- grant privilege
GRANT ALL PRIVILEGES ON FleetCore.* TO @userName;

--flush
FLUSH PRIVILEGES;


