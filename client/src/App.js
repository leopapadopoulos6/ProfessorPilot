import './App.css';
import React from 'react';
import Navbar from './Components/Navbar/Navbar.js';
import { Home } from './Pages/Home.js';
import { Courses } from './Pages/Courses.js';
import { Professors } from './Pages/Professors.js';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Routes>
          <Route path='/' exact component={Home} />
          <Route path='/Courses' exact component={Courses} />
          <Route path='/Professors' exact component={Professors} />
        </Routes>
        <Home/>



      </Router>
    </div>
  );
}

export default App;
