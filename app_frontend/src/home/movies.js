import { useState, useEffect } from 'react';
import Reviews from '../reusable/Reviews.js';
import './movies.css';

const MovieShowcaser = ({ setShowMovie, movie }) => {
  return (
    <div className='movieShowcaserBackground'>
      <div>
        <div className='movieShowcaser'>
          <div className='movieShowcaserContent'>
            <p
              className='movieShowcaserClose'
              onClick={() => {
                setShowMovie(false);
              }}
            >
              X
            </p>
            <h2>{movie.movie_name}</h2>
            <p style={{ textAlign: 'left' }}>
              {movie.movie_description}
            </p>
            <p>Write your review</p>
            <textarea className='movieShowcaserReviewArea'></textarea>
            <button
              onClick={() => {
                setShowMovie(false);
              }}
            >
              Submit
            </button>
            <div className='movieShowcaserReviews'>
              <h3>Other movie reviews</h3>
              <Reviews />
              <Reviews />
              <Reviews />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

const Movies = () => {
  const [showMovie, setShowMovie] = useState(false);
  const [movies, setMovies] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);

  useEffect(() => {
    getMovieList();
  }, []);

  const getMovieList = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/movies/", {
        method: "GET",
        headers : {
          'Content-Type' : 'application/json',
          'Accept' : 'application/json',
        },
      });
      const data = await response.json();

      if (response.status === 200){
        setMovies(data);      
      }
    } catch (error) {
      console.log(error);
    }
  }
  return (
    <>
      {showMovie && selectedMovie && <MovieShowcaser setShowMovie={setShowMovie} movie={selectedMovie} />}
      <div className='movies'>
        <h3>Movies</h3>
        <div className='moviesContainer'>
          {movies.map((movie) => {
            return (<div 
              key={movie.movie_id}
              className='moveisItem'
              onClick={() => {
                setShowMovie(true);
                setSelectedMovie(movie);
              }}
            > 
            <img
              src={movie.movie_image}
              alt={movie.movie_name}
              className='moviesImage'
            ></img>
            <p>{movie.movie_name}</p>
            </div> 
          )})}
        </div>
      </div>
    </>
  );
};
export default Movies;
