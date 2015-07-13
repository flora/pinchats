var UserForm = React.createClass({displayName: "UserForm",
  handleSubmit: function(e) {
    e.preventDefault();
    var name = React.findDOMNode(this.refs.name).value.trim();
    var team = React.findDOMNode(this.refs.team).value.trim();
    var role = React.findDOMNode(this.refs.role).value.trim();
    var frequency = React.findDOMNode(this.refs.frequency).value.trim();
    var timeAtCompany = React.findDOMNode(this.refs.timeAtCompany).value.trim();
    if (!name) {
      return;
    }
    //this.props.onUserSubmit({name: name, team: team, role: role, frequency: frequency, timeAtCompany: timeAtCompany});
    React.findDOMNode(this.refs.name).value = '';
    React.findDOMNode(this.refs.team).value = '';
    React.findDOMNode(this.refs.role).value = '';
    React.findDOMNode(this.refs.frequency).value = '';
    React.findDOMNode(this.refs.timeAtCompany).value = '';
  },
  render: function() {
    return (
	      React.createElement("form", {className: "userForm", onSubmit: this.handleSubmit}, 
            React.createElement("div", {className: "formElement"}, 
                React.createElement("label", null, "What is your prefered name?"), 
                React.createElement("input", {type: "text", placeholder: "Your name", ref: "name"})
            ), 
            React.createElement("div", {className: "formElement"}, 
            React.createElement("label", null, "What team are you on?"), 
                React.createElement("input", {type: "text", placeholder: "Team name", ref: "team"})
            ), 
            React.createElement("div", {className: "formElement"}, 
            React.createElement("label", null, "What is your role?"), 
                React.createElement("input", {type: "text", placeholder: "Role", ref: "role"})
            ), 
            React.createElement("div", {className: "formElement"}, 
                React.createElement("label", null, "How often would you like to be matched with a Pinployee?"), 
                React.createElement("select", {value: "biweekly", ref: "frequency"}, 
                    React.createElement("option", {value: "weekly"}, "Weekly"), 
                    React.createElement("option", {value: "biweekly"}, "Bi-weekly"), 
                    React.createElement("option", {value: "monthly"}, "Monthly")
                )
            ), 
            React.createElement("div", {className: "formElement"}, 
	        React.createElement("label", null, "How long have you been at the company?"), 
                React.createElement("select", {ref: "timeAtCompany"}, 
                    React.createElement("option", {value: "lessThan6Months"}, "Less than 6 months"), 
                    React.createElement("option", {value: "6To12Months"}, "6 to 12 months"), 
                    React.createElement("option", {value: "1to2Years"}, "1 to 2 years"), 
                    React.createElement("option", {value: "moreThan2Years"}, "More than 2 years")
                )
	        ), 
            React.createElement("div", {className: "formElement"}, 
	        	React.createElement("input", {type: "submit", value: "Submit"})
	        )
	      )
    );
  }
});

React.render(
  React.createElement(UserForm, null),
  document.getElementById('content')
);
