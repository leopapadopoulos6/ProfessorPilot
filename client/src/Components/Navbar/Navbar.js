import axios from "axios";
import { Home } from "../../Pages/Home.js";
import { Link } from "react-router-dom";

const Navbar= () => {
  return (
      <nav className="navbar">
          <h2>ProfessorPilot</h2>
          <div className="routes">
              <li><Link to="/home">Home</Link></li>
              <li><Link to="/courses">Courses</Link></li>
              <li><Link to="/professors">Home</Link></li>
              {/* <a href="/home">Home</a>
              <a href="/courses">Course Reviews</a>
              <a href="/professors">Professor Reviews</a> */}
          </div>
          <div className='login'>
              {/* <a href='#' onClick={login}>Login</a> */}
              <li onClick={login}>Login</li>
          </div>
      </nav>
  );
};

function login() {
    axios({
      method: "GET",
      url:"/login",
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      if(response.ok){
        return response
      }
    });
};

export default Navbar;