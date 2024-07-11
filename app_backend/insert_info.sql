INSERT INTO app_main_movies 
(movie_id, movie_name, movie_description, movie_image) VALUES
(1, 'The Matrix', 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.', 'matrix.jpg'),
(2, 'Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', 'inception.jpg'),
(3, 'Interstellar', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanitys survival.', 'interstellar.jpg'),
(4, 'The Dark Knight', 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.', 'dark_knight.jpg'),
(5, 'Pulp Fiction', 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 'pulp_fiction.jpg');

INSERT INTO app_main_movieuserreview (rating, review, movie_id, user_id) VALUES
(4.5, 'Amazing movie, loved the concept and execution!', 1, 1),
(4.8, 'Inception is a mind-bending masterpiece!', 2, 2),
(5.0, 'Interstellar is visually stunning and thought-provoking.', 3, 3),
(4.7, 'The Dark Knight is a dark, thrilling experience.', 4, 4),
(4.3, 'Pulp Fiction is a unique and engaging film.', 5, 5),
(4.6, 'The Matrix has aged well, still a great watch.', 1, 2),
(4.9, 'Inception plot is intricate and fascinating.', 2, 3),
(4.8, 'Interstellars soundtrack is mesmerizing.', 3, 4),
(4.7, 'The Dark Knight has unforgettable performances.', 4, 5),
(4.4, 'Pulp Fiction is brilliantly crafted.', 5, 1);

INSERT INTO members_userInfo (user_id, name, email, age, gender, date_of_birth) VALUES
(1, 'John Doe', 'john.doe@gmail.com', 28, 'Male', '1995-04-12'),
(2, 'Jane Smith', 'jane.smith@yahoo.com', 34, 'Female', '1989-07-23'),
(3, 'Alex Johnson', 'alex.johnson@outlook.com', 25, 'Nonbinary', '1998-01-17'),
(4, 'Chris Lee', 'chris.lee@hotmail.com', 31, 'Male', '1992-03-05'),
(5, 'Pat Taylor', 'pat.taylor@icloud.com', 29, 'Female', '1994-08-29');