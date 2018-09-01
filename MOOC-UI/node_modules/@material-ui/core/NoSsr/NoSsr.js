"use strict";

var _interopRequireDefault = require("@babel/runtime/helpers/builtin/interopRequireDefault");

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _classCallCheck2 = _interopRequireDefault(require("@babel/runtime/helpers/builtin/classCallCheck"));

var _createClass2 = _interopRequireDefault(require("@babel/runtime/helpers/builtin/createClass"));

var _possibleConstructorReturn2 = _interopRequireDefault(require("@babel/runtime/helpers/builtin/possibleConstructorReturn"));

var _inherits2 = _interopRequireDefault(require("@babel/runtime/helpers/builtin/inherits"));

var _react = _interopRequireDefault(require("react"));

var _propTypes = _interopRequireDefault(require("prop-types"));

var _exactProp = _interopRequireDefault(require("../utils/exactProp"));

var Fallback = function Fallback() {
  return null;
};
/**
 * NoSsr purposely removes components from the subject of Server Side Rendering (SSR).
 *
 * This component can be useful in a variety of situations:
 * - Escape hatch for broken dependencies not supporting SSR.
 * - Improve the time-to-first paint on the client by only rendering above the fold.
 * - Reduce the rendering time on the server.
 * - Under too heavy server load, you can turn on service degradation.
 */


var NoSsr =
/*#__PURE__*/
function (_React$Component) {
  (0, _inherits2.default)(NoSsr, _React$Component);

  function NoSsr() {
    var _ref;

    var _temp, _this;

    (0, _classCallCheck2.default)(this, NoSsr);

    for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    return (0, _possibleConstructorReturn2.default)(_this, (_temp = _this = (0, _possibleConstructorReturn2.default)(this, (_ref = NoSsr.__proto__ || Object.getPrototypeOf(NoSsr)).call.apply(_ref, [this].concat(args))), _this.state = {
      mounted: false
    }, _temp));
  }

  (0, _createClass2.default)(NoSsr, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      this.setState({
        mounted: true
      }); // eslint-disable-line react/no-did-mount-set-state
    }
  }, {
    key: "render",
    value: function render() {
      var _props = this.props,
          children = _props.children,
          fallback = _props.fallback;
      return this.state.mounted ? children : fallback;
    }
  }]);
  return NoSsr;
}(_react.default.Component);

NoSsr.propTypes = process.env.NODE_ENV !== "production" ? {
  children: _propTypes.default.node.isRequired,
  fallback: _propTypes.default.node
} : {};
NoSsr.propTypes = process.env.NODE_ENV !== "production" ? (0, _exactProp.default)(NoSsr.propTypes) : {};
NoSsr.defaultProps = {
  fallback: _react.default.createElement(Fallback, null)
};
var _default = NoSsr;
exports.default = _default;