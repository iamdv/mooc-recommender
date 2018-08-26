import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import classnames from "classnames";
import Grid from "@material-ui/core/Grid";
import Slide from "@material-ui/core/Slide";

import MoocHeader from "./MoocHeader";
import SkillThemer from "./SkillThemer";



const styles = theme => ({
  root: {
    flexGrow: 1
  },
  flex: {
    flexGrow: 1
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20
  },
  moocRecommenderContainer: {
    //textAlign: "center",
    margin: "30px 100px",
    [theme.breakpoints.down("sm")]: {
      margin: "30px 10px"
    }
  },
  skillThemeSelection: {
    padding: 50
  }
});

class MoocRecommender extends React.Component {
  state = { expanded: false };

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <Slide direction="down" in={true} mountOnEnter unmountOnExit>
          <MoocHeader />
        </Slide>
        
        <Grid container spacing={0}>
          <Grid item xs={12} className={classes.moocRecommenderContainer}>
            <Slide
              direction="down"
              in={true}
              timeout={500}
              mountOnEnter
              unmountOnExit
            >
              <SkillThemer />
            </Slide>
          </Grid>
        </Grid>
      </div>
    );
  }
}

MoocRecommender.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired
};

export default withStyles(styles, { withTheme: true })(MoocRecommender);
