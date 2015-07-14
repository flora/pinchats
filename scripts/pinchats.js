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
            <div className="heading formHeading">Join PinChats!</div>
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

var Nav = React.createClass({
    render: function() {
        var navStyle = {
            alignItems: 'center',
            display: 'flex',
            justifyContent: 'space-between',
            height: '20px',
            borderBottom: '1px solid #eee',
            padding: '16px',
            fontSize: '20px',
            fontWeight: 'bold',
            color: '#565656'
        };
        return (
            <div className="nav" style={navStyle}>
                <div className="logo">PinChats</div>
                <div className="settings">Settings</div>
            </div>
        );
    }
});

var About = React.createClass({
    render: function() {
        var imgUrl = 'images/mainImage.png';
        var aboutStyle = {
            alignItems: 'center',
            display: 'flex',
            color: 'white',
            padding: '40px',
            flexDirection: 'column',
            backgroundImage: 'url(' + imgUrl + ')',
            backgroundSize: 'cover',
            marginBottom: '30px'
        };

        return (
            <div className="about" style={aboutStyle}>
                <div className="mainHeading">Welcome to PinChat!</div>
                <ul>
                    <li>Blah blah blah blah blah</li>
                    <li>Blah blah blah blah blah</li>
                    <li>Blah blah blah blah blah</li>
                </ul>
            </div>
        );
    }
});

var Trends = React.createClass({
    render: function() {
        var statStyle = {
            mainSection: {
                display: 'flex'
            },
            signedUp: {
                color: 'white',
                width: '80px',
                height: '80px',
                borderRadius: '100%',
                margin: '20px 50px 10px 50px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                fontSize: '30px',

                backgroundColor: '#DB9E27'
            },
            scheduled: {
                color: 'white',
                width: '80px',
                height: '80px',
                borderRadius: '100%',
                margin: '20px 50px 10px 50px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                fontSize: '30px',

                backgroundColor: '#0A909B'
            },
            remaining: {
                color: 'white',
                width: '80px',
                height: '80px',
                borderRadius: '100%',
                margin: '20px 50px 10px 50px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                fontSize: '30px',

                backgroundColor: '#C24A41'
            },
            text: {
                fontSize: '14px',
                textAlign: 'center',
                marginBottom: '35px'
            }
        };

        return (
            <div className="trends">
                <div className="heading">Trending stats:</div>
                <div className="stats" style={statStyle.mainSection}>
                    <div className="signedUp">
                        <div style={statStyle.signedUp}>140</div>
                        <div style={statStyle.text}>Pinployees signed up</div>
                    </div>
                    <div className="scheduled">
                        <div style={statStyle.scheduled}>243</div>
                        <div style={statStyle.text}>PinChats scheduled</div>
                    </div>
                    <div className="remaining">
                        <div style={statStyle.remaining}>200</div>
                        <div style={statStyle.text}>Pinployees to go</div>
                    </div>
                </div>
            </div>
        );
    }
});

var Help = React.createClass({
    render: function() {
        return (
            <div className="help">
                <div className="heading">Helpful resources:</div>
                <ul>
                    <li>Blah blah blah blah blah</li>
                    <li>Blah blah blah blah blah</li>
                    <li>Blah blah blah blah blah</li>
                </ul>
            </div>
        );
    }
});


var PinChats = React.createClass({
    render: function() {
        var mainStyle = {
            display: 'flex',
            justifyContent: 'center'
        };

        var trendsAndHelp = {
            marginLeft: '70px',
            padding: '20px',
            backgroundColor: '#eee'
        }

        return (
            <div className="content">
                <Nav />
                <About />
                <div className="main" style={mainStyle}>
                    <div className="form">
                        <UserForm />
                    </div>
                    <div className="trendsAndHelp" style={trendsAndHelp}>
                        <Trends />
                        <Help />
                    </div>
                </div>
            </div>
        );
    }
});

React.render(
  <PinChats />,
  document.getElementById('content')
);
