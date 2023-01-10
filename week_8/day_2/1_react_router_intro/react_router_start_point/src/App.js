import React , { useState }from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import About from "./components/About"
import Home from "./components/Home"
import Pricing from "./components/Pricing"
import NavBar from "./components/NavBar"
import Intro from "./components/Intro"
import ErrorPage from "./components/ErrorPage"
import Choice from "./components/Choice"

const App = ()=> {
  const pricingData = [
    { level: "Hobby", cost: 0 },
    { level: "Startup", cost: 10},
    { level: "Enterprise", cost: 100 }
  ];

  const [prices, setPrices] = useState(pricingData);
  
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={ <Home /> }/>
        <Route path="/About" element={< About/>}/>
        <Route path="/Pricing" element={<Pricing prices={prices}/>}/>
        <Route path="/intro" element={<Intro/>}/>
        <Route path="/*" element={<ErrorPage />}/>
        <Route path=":choice" element={<Choice />}/>
      </Routes>
    </Router>
  )

}

export default App;
