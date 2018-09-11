import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import classnames from "classnames";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Collapse from "@material-ui/core/Collapse";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import red from "@material-ui/core/colors/red";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import LaunchIcon from "@material-ui/icons/Launch";
import StarBorderIcon from "@material-ui/icons/StarBorder";
import StarIcon from "@material-ui/icons/Star";
import Divider from "@material-ui/core/Divider";
import Tooltip from "@material-ui/core/Tooltip";
import Grid from "@material-ui/core/Grid";

import Rating from "react-rating";

const styles = theme => ({
  card: {
    //maxWidth: 400
    //maxHeight:200
  },
  media: {
    // height: 0,
  },
  actions: {
    display: "flex"
  },
  expand: {
    transform: "rotate(0deg)",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest
    }),
    marginLeft: "auto",
    [theme.breakpoints.up("sm")]: {
      marginRight: -8
    }
  },
  expandOpen: {
    transform: "rotate(180deg)"
  },
  avatar: {
    backgroundColor: theme.palette.primary.main
  },
  rate: {
    backgroundColor: red
  }
});

class MoocCourse extends React.Component {
  state = { expanded: false };

  handleExpandClick = () => {
    this.setState(state => ({ expanded: !state.expanded }));
  };

  render() {
    const { classes, data, theme } = this.props;

    return (
      <div>
        <Card className={classes.card}>
          <CardHeader
            avatar={
              <Avatar aria-label="Recipe" className={classes.avatar}>
                MR
              </Avatar>
            }
            action={
              <Rating
                initialRating={data.rating}
                emptySymbol={<StarBorderIcon color="primary" />}
                fullSymbol={<StarIcon color="primary" />}
                readonly
              />
            }
            title={data.courseName}
            subheader={data.provider}
          />
          <CardContent>
            <Grid container spacing={40}>
              <Grid item xs={4}>
                <Typography color="primary" component="p">
                  Provider
                </Typography>
                <Typography component="p">{data.provider}</Typography>
              </Grid>
              <Grid item xs={4}>
                <Typography color="primary" component="p">
                  Universities/Institutions
                </Typography>
                <Typography component="p">
                  {data.universitiesInstitutions}
                </Typography>
              </Grid>
              <Grid item xs={4}>
                <Typography color="primary" component="p">
                  Duraion (Weeks)
                </Typography>
                <Typography component="p">{data.length}</Typography>
              </Grid>

              <Grid item xs={4}>
                <Typography color="primary" component="p">
                  Parent Subject
                </Typography>
                <Typography component="p">{data.parentSubject}</Typography>
              </Grid>
              <Grid item xs={4}>
                <Typography color="primary" component="p">
                  Child Subject
                </Typography>
                <Typography component="p">{data.childSubject}</Typography>
              </Grid>

              <Grid item xs={4}>
                <Typography color="primary" component="p">
                  Workload
                </Typography>
                <Typography component="p">{data.workload}</Typography>
              </Grid>
            </Grid>
          </CardContent>
          <Divider />
          <CardActions className={classes.actions} disableActionSpacing>
            <Tooltip title="Go to course" placement="right">
              <IconButton href={data.url} target="blank" aria-label="Launch">
                <LaunchIcon />
              </IconButton>
            </Tooltip>

            {data.courseDescription.length > 0 && (
              <IconButton
                className={classnames(classes.expand, {
                  [classes.expandOpen]: this.state.expanded
                })}
                onClick={this.handleExpandClick}
                aria-expanded={this.state.expanded}
                aria-label="Show more"
              >
                <ExpandMoreIcon />
              </IconButton>
            )}
          </CardActions>
          <Collapse in={this.state.expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <Typography paragraph>{data.courseDescription}</Typography>
            </CardContent>
          </Collapse>
        </Card>
      </div>
    );
  }
}

MoocCourse.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired
};

export default withStyles(styles, { withTheme: true })(MoocCourse);
