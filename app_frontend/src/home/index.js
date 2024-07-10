import React from 'react';
import './home.css';
import { useState } from 'react';
import Movies from './movies.js';
import Reviews from './reviews.js';
import Analytics from './analytics.js';

const Home = ({ user }) => {
  const [navTab, setNavTab] = useState('movies');
  return (
    <div className='homeContainer'>
      <div className='navbar'>
        <div
          className='navItem navItemFirst'
          onClick={() => setNavTab('movies')}
        >
          Hi {user}!
        </div>
        <div className='navItem' onClick={() => setNavTab('movies')}>
          Movies
        </div>
        <div className='navItem' onClick={() => setNavTab('reviews')}>
          Reviews
        </div>
        <div className='navItem' onClick={() => setNavTab('analytics')}>
          Analytics
        </div>
      </div>
      {navTab === 'movies' ? (
        <Movies />
      ) : navTab === 'reviews' ? (
        <Reviews />
      ) : (
        <Analytics />
      )}
    </div>
  );
};

export default Home;
