-- script that prepares a MYsql server for the project
CREATE DATABASE IF NOT EXISTS boma_dev_db;
CREATE USER IF NOT EXISTS 'boma_dev'@'localhost' IDENTIFIED BY '123';
USE mysql;
GRANT ALL PRIVILEGES ON `boma_dev_db`.* TO 'boma_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'boma_dev'@'localhost';
FLUSH PRIVILEGES;