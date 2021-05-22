import React, { Component } from "react";
import FacebookLogin from "react-facebook-login";

export default class Facebook extends Component {
  constructor(props) {
    super(props);
    this.state = {
      auth: false,
      name: "",
      picture: "",
    };
  }
  responseFacebook = (response) => {
    console.log(response);

    if (response.status !== "unknown") {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userid: response.userID,
          email: response.email,
          name: response.name,
          password: response.accessToken,
          avatar: response.picture.data.url,
          provider: response.graphDomain,
        }),
      };
      fetch("http://localhost:8000/api/oauth/login/", requestOptions)
        .then((response) => console.log(response.json()))

      this.setState({
        auth: true,
        name: response.name,
        picture: response.picture.data.url,
      });
    }
  };

  render() {
    let facebookData;

    this.state.auth
      ? (facebookData = (
          <div
            style={{
              width: "400px",
              margin: "auto",
              background: "gray",
              padding: "20px",
              color: "#000",
            }}
          >
            <img src={this.state.picture} alt={this.state.name} />
            <h2>Welcome {this.state.name}!</h2>
          </div>
        ))
      : (facebookData = (
          <FacebookLogin
            appId="459253152013173" // Your ID of FACEBOOK APP
            autoLoad={false}
            cookie={false}
            redirectUri="/home"
            fields="name,picture, email" 
            callback={this.responseFacebook}
          />
        ));

    return <>{facebookData}</>;
  }
}
