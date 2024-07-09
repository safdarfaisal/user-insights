import './App.css';

function App() {
  return (
    <div className='App'>
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
          <button className='LoginBoxButton'>Submit</button>
        </div>
      </div>
    </div>
  );
}

export default App;
