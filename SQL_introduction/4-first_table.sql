-- creates a table called first_table in the current database in your MySQL server
-- id (INT) - must be a number that acts as a unique identifier for the record
-- name (VARCHAR) - must be a string that stores the name of the record
CREATE TABLE IF NOT EXISTS first_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);
