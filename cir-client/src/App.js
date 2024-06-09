import React from 'react';
import Login from './pages/login';
import Signup from './pages/signup';
import Landing from './pages/landing';
import Myposts from './pages/myposts';
import Createpost from './pages/createpost';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path = "/landing" element = {<Landing />} />
        <Route path = '/' element = {<Login />} />
        <Route path = '/signup' element = {<Signup />} />
        <Route path = '/myposts' element = {<Myposts />} />
        <Route path = '/createpost' element = {<Createpost />} />
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
