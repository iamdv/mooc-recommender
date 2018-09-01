import React, { Component } from "react";
import "./App.css";
import MoocRecommender from "./components/MoocRecommender";
import { MuiThemeProvider, createMuiTheme } from "@material-ui/core/styles";
import themePrimaryColor from "@material-ui/core/colors/amber";
import themeSecondaryColor from "@material-ui/core/colors/blueGrey";

// All the following keys are optional.
// We try our best to provide a great default value.
const theme = createMuiTheme({
  palette: {
    type: "light",
    primary: themePrimaryColor,
    secondary: themeSecondaryColor
  }
});

class App extends Component {
  render() {
    return (
      <MuiThemeProvider theme={theme}>
        <div className="App">
          <MoocRecommender />
        </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
