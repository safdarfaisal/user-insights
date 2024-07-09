import React, { useState } from 'react';
import Home from './home/index.js';
import './App.css';

function App() {
  const [user, setUser] = useState('');
  return (
    <div className='App'>
      {!user ? (
        <>
          <h1 style={{ color: 'white' }}>Welcome to Movie Analytics</h1>

          <div className='Loginbox'>
            <p className='LoginBoxHeader'>Login</p>
            <div className='LoginBoxContainer'>
              <p>User Name:</p>
              <input
                type='text'
                id='uname'
                name='uname'
                className='LoginBoxInput'
              ></input>
              <p>Password:</p>
              <input
                type='password'
                id='uname'
                name='uname'
                className='LoginBoxInput'
              ></input>
              <button
                className='LoginBoxButton'
                onClick={() => setUser('Rohan')}
              >
                Submit
              </button>
            </div>
          </div>
        </>
      ) : (
        <Home user={user} />
      )}
    </div>
  );
}

export default App;
