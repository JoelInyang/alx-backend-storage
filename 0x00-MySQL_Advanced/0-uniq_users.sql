-- S script that creates a table users following these 
-- i, email, name
CREATE TABLE IF NOT EXISTS users (
        id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email varchar(255) NOT NULL UNIQUE,
        name varchar(255)
);
