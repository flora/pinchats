var script = document.createElement('script');
script.src = 'http://code.jquery.com/jquery-1.11.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

var UserForm = React.createClass({displayName: "UserForm",
  handleSubmit: function(e) {
    e.preventDefault();
    var name = React.findDOMNode(this.refs.name).value.trim();
    var email = React.findDOMNode(this.refs.email).value.trim();
    var team = React.findDOMNode(this.refs.team).value.trim();
    var role = React.findDOMNode(this.refs.role).value.trim();
    var frequency = React.findDOMNode(this.refs.frequency).value.trim();
    var timeAtCompany = React.findDOMNode(this.refs.timeAtCompany).value.trim();
    if (!name) {
      return;
    }
    var json = {}
    json.name = name;
    json.email = email;
    json.team = team;
    json.role = role;
    json.frequency = frequency;
    json.time_at_company = timeAtCompany;
    $.ajax({
      url: '/user',
      type: 'PUT',
      data: JSON.stringify(json),
      success: function(data) {
        alert('Load was performed.');
      }
    });
    //this.props.onUserSubmit({name: name, team: team, role: role, frequency: frequency, timeAtCompany: timeAtCompany});
    React.findDOMNode(this.refs.name).value = '';
    React.findDOMNode(this.refs.email).value = '';
    React.findDOMNode(this.refs.team).value = '';
    React.findDOMNode(this.refs.role).value = '';
    React.findDOMNode(this.refs.frequency).value = '';
    React.findDOMNode(this.refs.timeAtCompany).value = '';
  },
  render: function() {
    return (
	      React.createElement("form", {className: "userForm", onSubmit: this.handleSubmit}, 
            React.createElement("div", {className: "heading formHeading"}, "Join PinChats!"), 
            React.createElement("div", {className: "formElement"}, 
                React.createElement("label", null, "What is your prefered name?"), 
                React.createElement("input", {type: "text", placeholder: "Your name", ref: "name"})
            ), 
            React.createElement("div", {className: "formElement"}, 
                React.createElement("label", null, "What is your pinterest email?"), 
                React.createElement("input", {type: "text", placeholder: "Email", ref: "email"})
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
                React.createElement("select", {ref: "frequency"}, 
                    React.createElement("option", {value: "1w"}, "Weekly"), 
                    React.createElement("option", {value: "2w"}, "Bi-weekly"), 
                    React.createElement("option", {value: "1m"}, "Monthly")
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

var Nav = React.createClass({displayName: "Nav",
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
            React.createElement("div", {className: "nav", style: navStyle}, 
                React.createElement("div", {className: "logo"}, "PinChats"), 
                React.createElement("div", {className: "settings"}, "Settings")
            )
        );
    }
});

var About = React.createClass({displayName: "About",
    render: function() {
        var imgUrl = 'client/images/mainImage.png';
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
            React.createElement("div", {className: "about", style: aboutStyle}, 
                React.createElement("div", {className: "mainHeading"}, "Welcome to PinChat!"), 
                React.createElement("ul", null, 
                    React.createElement("li", null, "Blah blah blah blah blah"), 
                    React.createElement("li", null, "Blah blah blah blah blah"), 
                    React.createElement("li", null, "Blah blah blah blah blah")
                )
            )
        );
    }
});

var Trends = React.createClass({displayName: "Trends",
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
            React.createElement("div", {className: "trends"}, 
                React.createElement("div", {className: "heading"}, "Trending stats:"), 
                React.createElement("div", {className: "stats", style: statStyle.mainSection}, 
                    React.createElement("div", {className: "signedUp"}, 
                        React.createElement("div", {style: statStyle.signedUp}, "140"), 
                        React.createElement("div", {style: statStyle.text}, "Pinployees signed up")
                    ), 
                    React.createElement("div", {className: "scheduled"}, 
                        React.createElement("div", {style: statStyle.scheduled}, "243"), 
                        React.createElement("div", {style: statStyle.text}, "PinChats scheduled")
                    ), 
                    React.createElement("div", {className: "remaining"}, 
                        React.createElement("div", {style: statStyle.remaining}, "200"), 
                        React.createElement("div", {style: statStyle.text}, "Pinployees to go")
                    )
                )
            )
        );
    }
});

var Help = React.createClass({displayName: "Help",
    render: function() {
        return (
            React.createElement("div", {className: "help"}, 
                React.createElement("div", {className: "heading"}, "Helpful resources:"), 
                React.createElement("ul", null, 
                    React.createElement("li", null, "Blah blah blah blah blah"), 
                    React.createElement("li", null, "Blah blah blah blah blah"), 
                    React.createElement("li", null, "Blah blah blah blah blah")
                )
            )
        );
    }
});


var PinChats = React.createClass({displayName: "PinChats",
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
            React.createElement("div", {className: "content"}, 
                React.createElement(Nav, null), 
                React.createElement(About, null), 
                React.createElement("div", {className: "main", style: mainStyle}, 
                    React.createElement("div", {className: "form"}, 
                        React.createElement(UserForm, null)
                    ), 
                    React.createElement("div", {className: "trendsAndHelp", style: trendsAndHelp}, 
                        React.createElement(Trends, null), 
                        React.createElement(Help, null)
                    )
                )
            )
        );
    }
});

React.render(
  React.createElement(PinChats, null),
  document.getElementById('content')
);
