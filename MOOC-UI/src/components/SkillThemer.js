import React from "react";
import PropTypes from "prop-types";
import Select from "react-select";
import { withStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import NoSsr from "@material-ui/core/NoSsr";
import TextField from "@material-ui/core/TextField";
import MenuItem from "@material-ui/core/MenuItem";
import { emphasize } from "@material-ui/core/styles/colorManipulator";
import Grid from "@material-ui/core/Grid";
import Chip from "@material-ui/core/Chip";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import Button from "@material-ui/core/Button";
import Grow from "@material-ui/core/Grow";
import Fade from "@material-ui/core/Fade";
import Slide from "@material-ui/core/Slide";
import IconButton from "@material-ui/core/IconButton";
import TableChartIcon from "@material-ui/icons/TableChart";
import ViewStreamIcon from "@material-ui/icons/ViewStream";

import skillsData from "../data/skillListing.json";
import coursesData from "../data/courses.json";

import MoocCourse from "./MoocCourse";
import MoocCourseTable from "./MoocCourseTable";

const suggestions = skillsData.skillListing.map(suggestion => ({
  value: suggestion.skillTheme,
  label: suggestion.skillTheme
}));

const styles = theme => ({
  root: {
    flexGrow: 1
    //height: 250,
  },
  input: {
    display: "flex",
    padding: 0
  },
  valueContainer: {
    display: "flex",
    flex: 1,
    alignItems: "center"
  },
  chip: {
    margin: `${theme.spacing.unit}px ${theme.spacing.unit}px`
  },
  chipFocused: {
    backgroundColor: emphasize(
      theme.palette.type === "light"
        ? theme.palette.grey[300]
        : theme.palette.grey[700],
      0.08
    )
  },
  noOptionsMessage: {
    fontSize: 16,
    padding: `${theme.spacing.unit}px ${theme.spacing.unit * 2}px`
  },
  singleValue: {
    fontSize: "1.5rem"
  },
  placeholder: {
    position: "absolute",
    left: 2,
    fontSize: 16
  },
  formControl: {
    margin: theme.spacing.unit
  },
  group: {
    margin: `${theme.spacing.unit}px 0`
  },
  skillThemeTitleText: {
    float: "right",
    [theme.breakpoints.down("sm")]: {
      float: "none"
    }
  },
  fetchMoocRecommendationsBtn: {
    padding: "20px 50px",
    textAlign: "center"
  },
  courseCard: {
    margin: 10
  },
  centerAligned: {
    textAlign: "center"
  },
  viewChangeButton: {
    float: "right"
  }
});

function NoOptionsMessage(props) {
  return (
    <Typography
      color="textSecondary"
      className={props.selectProps.classes.noOptionsMessage}
      {...props.innerProps}
    >
      {props.children}
    </Typography>
  );
}

function inputComponent({ inputRef, ...props }) {
  return <div ref={inputRef} {...props} />;
}

function Control(props) {
  return (
    <TextField
      fullWidth
      InputProps={{
        inputComponent,
        inputProps: {
          className: props.selectProps.classes.input,
          ref: props.innerRef,
          children: props.children,
          ...props.innerProps
        }
      }}
    />
  );
}

function Option(props) {
  return (
    <MenuItem
      buttonRef={props.innerRef}
      selected={props.isFocused}
      component="div"
      style={{
        fontWeight: props.isSelected ? 500 : 400
      }}
      {...props.innerProps}
    >
      {props.children}
    </MenuItem>
  );
}

function Placeholder(props) {
  return (
    <Typography
      color="textSecondary"
      className={props.selectProps.classes.placeholder}
      {...props.innerProps}
    >
      {props.children}
    </Typography>
  );
}

function SingleValue(props) {
  return (
    <Typography
      className={props.selectProps.classes.singleValue}
      {...props.innerProps}
    >
      {props.children}
    </Typography>
  );
}

function ValueContainer(props) {
  return (
    <div className={props.selectProps.classes.valueContainer}>
      {props.children}
    </div>
  );
}

const components = {
  Option,
  Control,
  NoOptionsMessage,
  Placeholder,
  SingleValue,
  ValueContainer
};

const columns = [
  "Course Name",
  "Provider",
  "Universities/Institutions",
  "Parent Subject",
  "Child Subject",
  "Duration (Weeks)",
  "Workload"
];

const options = {
  filter: false,
  responsive: "scroll",
  selectableRows: false,
  viewColumns: false
};

class SkillThemer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      single: null,
      selectedSkill: null,
      skillTags: [],
      coursesCardData: [],
      coursesTableData: [],
      skillFiltervalue: "all",
      isTableView: false
    };
  }

  handleFilterChange = event => {
    this.setState({
      skillFiltervalue: event.target.value,
      skillTags:
        this.state.selectedSkill &&
        this.state.selectedSkill.length > 0 &&
        event.target.value === "all"
          ? this.state.selectedSkill[0].skillTags
          : this.state.selectedSkill[0].skillTagsRecommended,
      coursesCardData: [],
      coursesTableData: [],
      isTableView: false
    });
  };

  handleSkillThemeChange = name => value => {
    const selectedSkill = skillsData.skillListing.filter(item => {
      return item.skillTheme === value.label;
    });

    this.setState({
      [name]: value,
      skillFiltervalue: "all",
      selectedSkill: selectedSkill,
      skillTags:
        selectedSkill && selectedSkill.length > 0
          ? selectedSkill[0].skillTags
          : [],
      coursesCardData: [],
      coursesTableData: [],
      isTableView: false
    });
  };

  handleClick = () => {
    console.log("You clicked the Skill Tag.");
  };

  changeToTableView = () => {
    this.setState({
      isTableView: true
    });
  };

  changeToCardView = () => {
    this.setState({
      isTableView: false
    });
  };

  prepareCoursesTableData = data => {
    const _data = [];
    data.map(item => {
      const rowData = [];
      rowData.push(item.courseName);
      rowData.push(item.provider);
      rowData.push(item.universitiesInstitutions);
      rowData.push(item.parentSubject);
      rowData.push(item.childSubject);
      rowData.push(item.length);
      rowData.push(item.workload);
      _data.push(rowData);
    });
    return _data;
  };

  fetchMoocRecommendations = () => {
    const _coursesData = coursesData.sort(
      (a, b) =>
        a.skillRankMap[this.state.selectedSkill[0].skillID][
          this.state.skillFiltervalue
        ] -
        b.skillRankMap[this.state.selectedSkill[0].skillID][
          this.state.skillFiltervalue
        ]
    );

    this.setState({
      coursesCardData: _coursesData,
      coursesTableData: this.prepareCoursesTableData(_coursesData),
      isTableView: true
    });
  };

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <Grid container spacing={40}>
          <Grid item xs={12}>
            <Grid container spacing={16}>
              <Grid item sm={4} xs={12}>
                <Typography
                  variant="headline"
                  component="h2"
                  className={classes.skillThemeTitleText}
                >
                  I want to become
                </Typography>
              </Grid>
              <Grid item sm={6} xs={12}>
                <NoSsr>
                  <Select
                    classes={classes}
                    options={suggestions}
                    components={components}
                    value={this.state.single}
                    onChange={this.handleSkillThemeChange("single")}
                    placeholder="Super Man"
                  />
                </NoSsr>
              </Grid>
            </Grid>
          </Grid>
          {this.state.skillTags.length > 0 && (
            <Grid item xs={12}>
              <Grid container spacing={24} className={classes.centerAligned}>
                <Grid item xs={12}>
                  <div className={classes.filterBox}>
                    <Grow in={true} timeout={300} mountOnEnter unmountOnExit>
                      <FormControl
                        component="fieldset"
                        className={classes.formControl}
                      >
                        <RadioGroup
                          aria-label="Filter"
                          name="filter"
                          value={this.state.skillFiltervalue}
                          onChange={this.handleFilterChange}
                          row={true}
                        >
                          <FormControlLabel
                            value="all"
                            control={<Radio color="primary" />}
                            label="All"
                          />
                          <FormControlLabel
                            value="recommended"
                            control={<Radio color="primary" />}
                            label="Recommended"
                          />
                        </RadioGroup>
                      </FormControl>
                    </Grow>
                  </div>
                </Grid>
                <Grid item xs={12}>
                  {this.state.skillTags.map(item => {
                    return (
                      <Grow
                        key={item}
                        in={true}
                        timeout={600}
                        mountOnEnter
                        unmountOnExit
                      >
                        <Chip
                          label={item}
                          onClick={this.handleClick}
                          className={classes.chip}
                        />
                      </Grow>
                    );
                  })}
                </Grid>
                <Grow in={true} timeout={700} mountOnEnter unmountOnExit>
                  <Grid item xs={12}>
                    <Button
                      variant="outlined"
                      size="large"
                      color="primary"
                      className={classes.fetchMoocRecommendationsBtn}
                      onClick={this.fetchMoocRecommendations}
                    >
                      Fetch MOOC Recommendations
                    </Button>
                  </Grid>
                </Grow>
                {this.state.coursesCardData.length > 0 && (
                  <Grow in={true} timeout={800} mountOnEnter unmountOnExit>
                    <Grid item xs={12}>
                      <IconButton
                        className={classes.viewChangeButton}
                        aria-label="Table Chart"
                        //disabled={this.state.isTableView}
                        color={!this.state.isTableView ? "default" : "primary"}
                        onClick={this.changeToTableView}
                      >
                        <TableChartIcon />
                      </IconButton>
                      <IconButton
                        className={classes.viewChangeButton}
                        aria-label="View Stream"
                        //disabled={!this.state.isTableView}
                        color={this.state.isTableView ? "default" : "primary"}
                        onClick={this.changeToCardView}
                      >
                        <ViewStreamIcon />
                      </IconButton>
                    </Grid>
                  </Grow>
                )}
              </Grid>
            </Grid>
          )}
          {this.state.skillTags.length > 0 && (
            <div>
              {!this.state.isTableView && (
                <Grid item xs={12}>
                  <Grid container spacing={16}>
                    {this.state.coursesCardData.map((item, index) => {
                      return (
                        <Grow
                          in={true}
                          timeout={400 * (index + 1)}
                          key={item.courseId}
                          mountOnEnter
                          unmountOnExit
                        >
                          <Grid item xs={12}>
                            <MoocCourse data={item} />
                          </Grid>
                        </Grow>
                      );
                    })}
                  </Grid>
                </Grid>
              )}

              {this.state.isTableView && (
                <Grid item xs={12}>
                  <Slide
                    direction="up"
                    in={this.state.isTableView}
                    timeout={400}
                    mountOnEnter
                    unmountOnExit
                  >
                    <MoocCourseTable
                      title={"MOOC Recommendations"}
                      data={this.state.coursesTableData}
                      columns={columns}
                      options={options}
                    />
                  </Slide>
                </Grid>
              )}
            </div>
          )}
        </Grid>
      </div>
    );
  }
}

SkillThemer.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired
};

export default withStyles(styles, { withTheme: true })(SkillThemer);
