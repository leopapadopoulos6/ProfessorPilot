import './navebar.css';
import {useEffect} from "react";
import axios from "axios";
const Navbar= () => {
  return (
      <nav className="navbar">
          <h2> ProfessorPilot</h2>
          <div className="page-nav">
              <a href="/home">Home</a>
              <a href="/courses">Course Reviews</a>
              <a href="/professors">Professor Reviews</a>
          </div>
          <div className='links'>
              <a href='#' onClick={login}>Login</a>

          </div>
      </nav>
  );
}

function login() {
    axios({
       method: "GET",
       url:"/login",
      mode: 'no-cors',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      },
    })
    .then((response) => {

    });
}

export default Navbar