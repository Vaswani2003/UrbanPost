import React from 'react';
import Login from './pages/login';
import Signup from './pages/signup';
import Landing from './pages/landing';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Landing />} />
        <Route path = '/login' element = {<Login />} />
        <Route path = '/signup' element = {<Signup />} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
