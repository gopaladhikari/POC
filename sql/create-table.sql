CREATE TABLE users (
	id INT PRIMARY KEY,
    email VARCHAR(30) UNIQUE NOT NULL,
    username VARCHAR(20) UNIQUE NOT NULL,
    gender ENUM("MALE", "FEMALE"),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)


-- SELECT * FROM users;