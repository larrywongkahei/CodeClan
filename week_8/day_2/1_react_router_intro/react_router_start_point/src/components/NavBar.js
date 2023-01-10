import React  from "react";
import { Link } from "react-router-dom";

const NavBar = () =>{
    return (
        <ul>
            <li>
                <Link to="/">Home</Link>
            </li>
            <li>
                <Link to="/About">About</Link>
            </li>
            <li>
                <Link to="/Pricing">Pricing</Link>
            </li>
            <li>
                <Link to="/Intro">Intro</Link>
            </li>
        </ul>
    )
}

export default NavBar