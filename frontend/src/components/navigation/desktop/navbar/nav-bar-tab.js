import React from "react";
import { NavLink } from "react-router-dom";
import Button  from "@mui/material/Button";

export const NavBarTab = ({ path, label }) => {
  return (
    <NavLink
      to={path}
      end
      // activeClassName="nav-bar__tab--active"
    >
      <Button sx={{margin:2}} size="large" variant="outlined" color="secondary">
        {label}
      </Button>
    </NavLink>
  );
};