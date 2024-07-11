INSERT INTO movies 
(movie_id, movie_name, movie_description, movie_image) VALUES
(1, 'The Matrix', 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.', 'matrix.jpg'),
(2, 'Inception', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.', 'inception.jpg'),
(3, 'Interstellar', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.', 'interstellar.jpg'),
(4, 'The Dark Knight', 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.', 'dark_knight.jpg'),
(5, 'Pulp Fiction', 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 'pulp_fiction.jpg');

INSERT INTO movies_user_review (user_id, movie_id, rating, review) VALUES
(1, 1, 4.5, 'Amazing movie with a unique concept.'),
(2, 2, 4.8, 'A mind-bending experience.'),
(3, 3, 4.7, 'Visually stunning and thought-provoking.'),
(4, 4, 4.9, 'The best superhero movie ever.'),
(5, 5, 4.6, 'A classic with great storytelling.');

