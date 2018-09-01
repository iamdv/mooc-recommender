import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import MUIDataTable from "mui-datatables";

const styles = theme => ({});

class MoocCourseTable extends React.Component {
  //   state = { expanded: false };

  //   handleExpandClick = () => {
  //     this.setState(state => ({ expanded: !state.expanded }));
  //   };

  render() {
    const { classes,theme, title, data, columns, options } = this.props;

    return (
      <div>
        <MUIDataTable
          title={title}
          data={data}
          columns={columns}
          options={options}
        />
      </div>
    );
  }
}

MoocCourseTable.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired
};

export default withStyles(styles, { withTheme: true })(MoocCourseTable);
