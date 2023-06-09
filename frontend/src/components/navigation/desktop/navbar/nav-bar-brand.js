import React from "react";
import { NavLink } from "react-router-dom";
import IconButton from "@mui/material/IconButton";
// import logo from './../../images/wings.png';
// import logo from "./../../../images/wings.png"
import logo from "../../../images/profpilotminimaltassletransparent.png"
import { Container } from "@mui/material";

export const NavBarBrand = () => {
  return (
    <Container>
      <NavLink to="/">
        <IconButton>
          <img
            src={logo}
            alt="ProfessorPilot logo"
            width="175"
            height="100"
          />
        </IconButton>
      </NavLink>
    </Container>
  );
};