var UserForm = React.createClass({
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
	      <form className="userForm" onSubmit={this.handleSubmit}>
            <div className="formElement">
                <label>What is your prefered name?</label>
                <input type="text" placeholder="Your name" ref="name" />
            </div>
            <div className="formElement">
            <label>What team are you on?</label>
                <input type="text" placeholder="Team name" ref="team" />
            </div>
            <div className="formElement">
            <label>What is your role?</label>
                <input type="text" placeholder="Role" ref="role" />
            </div>
            <div className="formElement">
                <label>How often would you like to be matched with a Pinployee?</label>
                <select value="biweekly" ref="frequency">
                    <option value="weekly">Weekly</option>
                    <option value="biweekly">Bi-weekly</option>
                    <option value="monthly">Monthly</option>
                </select>
            </div>
            <div className="formElement">
	        <label>How long have you been at the company?</label>
                <select ref="timeAtCompany">
                    <option value="lessThan6Months">Less than 6 months</option>
                    <option value="6To12Months">6 to 12 months</option>
                    <option value="1to2Years">1 to 2 years</option>
                    <option value="moreThan2Years">More than 2 years</option>
                </select>
	        </div>
            <div className="formElement">
	        	<input type="submit" value="Submit" />
	        </div>
	      </form>
    );
  }
});

React.render(
  <UserForm />,
  document.getElementById('content')
);
