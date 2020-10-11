import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";

// import components
import App from "./App";
import Home from "./home";



ReactDOM.render(
  <Router>
    <div className="App">
      <Route exact path="/" component={App} />
      <Route exact path="/home" component={Home} />
    </div>
  </Router>,
  document.getElementById("root")
);