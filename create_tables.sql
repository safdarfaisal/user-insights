CREATE TABLE user_info (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
  password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE movies (
    user_id INTEGER,
    movie_name TEXT NOT NULL,
    movie_id INTEGER PRIMARY KEY,
    genre TEXT,
    average_rating REAL,
    main_actor1 TEXT,
    main_actor2 TEXT,
    director TEXT,
    year INTEGER,
    review TEXT,
    FOREIGN KEY(user_id) REFERENCES user_info(user_id)
);
