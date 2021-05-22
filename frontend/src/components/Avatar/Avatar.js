import React, { Component } from "react";
import AvatarTag from "react-avatar";
import {Button} from "reactstrap";
export default class Avatar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLogin: false,
    };
  }
  render() {
    let avtData;
    let email = localStorage.getItem('username')
    if(localStorage.getItem('username')!=null){
        this.state.isLogin = true
    }
    this.state.isLogin
      ? (avtData = (
          <AvatarTag
            round = {true}
            size="45"
            email= {email}
          />
        ))
      : (avtData = (
          <Button
            className="nav-link d-none d-lg-block"
            color="primary"
            href="/register-page?#"
          >
            <i className="tim-icons icon-spaceship" /> Getting Started
          </Button>
        ));
    return <>{avtData}</>;
  }
}
