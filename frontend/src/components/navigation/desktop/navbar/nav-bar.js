import React from "react";
import { NavBarBrand } from "./nav-bar-brand";
import { NavBarButtons } from "./nav-bar-buttons";
import { NavBarTabs } from "./nav-bar-tabs";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Box from "@mui/material/Box";

export const NavBar = () => {
  return (
    <div>
      <AppBar position="static" color="primary">
        <Toolbar>
          <Box display="flex" flexGrow={1}>
            <NavBarBrand />
          </Box >
          <Box display="flex" flexGrow={1}>
            <NavBarTabs />
          </Box>
          
          <NavBarButtons />
        </Toolbar>
      </AppBar>
    </div>
  );
};