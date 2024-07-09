import { useState } from 'react';
import './movies.css';

const MovieShowcaser = ({ setShowMovie }) => {
  return (
    <div
      className='movieShowcaserBackground'
      onClick={() => {
        setShowMovie(false);
      }}
    >
      <div>
        <div className='movieShowcaser'>
          <p
            className='movieShowcaserClose'
            onClick={() => {
              setShowMovie(false);
            }}
          >
            X
          </p>
          <h2>Movie Name</h2>
          <p>other details</p>
          <p>Write your review</p>
          <input type='text'></input>
          <button>Submit</button>
        </div>
      </div>
    </div>
  );
};

const Movies = () => {
  const [showMovie, setShowMovie] = useState(false);
  const [movieName, setMovieName] = useState('');
  return (
    <>
      {showMovie && <MovieShowcaser setShowMovie={setShowMovie} />}
      <div className='movies'>
        <h3>Movies</h3>
        <div className='moviesContainer'>
          <div
            className='moviesItem'
            onClick={() => {
              setShowMovie(!showMovie);
              setMovieName('name');
            }}
          >
            <img
              src={require('../images/movie1.jpeg')}
              className='moviesImage'
            />
            <p>name</p>
          </div>
        </div>
      </div>
    </>
  );
};
export default Movies;
