CREATE TABLE user_info (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
  password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE movies (
  movie_id INTEGER PRIMARY KEY,
  movie_name VARCHAR(50) NOT NULL,
  movie_description TEXT NOT NULL,
  movie_image TEXT NOT NULL  
);

CREATE TABLE movies_user_review (
    user_id INTEGER,
    movie_id INTEGER,
    rating FLOAT NOT NULL,
    review VARCHAR(255),
    FOREIGN KEY(user_id) REFERENCES user_info(user_id),
    FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
);
