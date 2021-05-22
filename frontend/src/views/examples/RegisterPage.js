/*!

=========================================================
* BLK Design System React - v1.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/blk-design-system-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/blk-design-system-react/blob/main/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";

import classnames from "classnames";
import Facebook from "components/Button/FaceBook.js";
import NotificationAlert from 'react-notification-alert';
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
// reactstrap components
import {
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardImg,
  CardTitle,
  Label,
  FormGroup,
  Form,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Container,
  Row,
  Col,
} from "reactstrap";

// core components
import ExamplesNavbar from "components/Navbars/IndexNavbar.js";
import Footer from "components/Footer/Footer.js";


var options = {};
options = {
    place: 'br',
    message: (
        <div>
            <div>
                Email đã tồn tại!
            </div>
        </div>
    ),
    type: "info",
    icon: "now-ui-icons ui-1_bell-53",
    autoDismiss: 7
}

export default function RegisterPage() {
  // const responseFacebook = (response) => {
  //   const requestOptions = {
  //     method: "POST",
  //     headers: { "Content-Type": "application/json" },
  //     body: JSON.stringify({
  //       userid: response.userID,
  //       email: response.email,
  //       access_token_fb: response.accessToken,
  //       picture: response.picture.data.url,
  //       provider: response.graphDomain,
  //     }),
  //   };
  //   fetch("http://localhost:8000/api/oauth/login/", requestOptions)
  //     .then((response) => console.log(response.json()))
  //     .then((data) => {
  //       console.log(data);
  //     });
  //   //.then((data) => this.props.history.push("/room/" + data.code));
  // };

  const [squares1to6, setSquares1to6] = React.useState("");
  const [squares7and8, setSquares7and8] = React.useState("");
  
  React.useEffect(() => {
    document.body.classList.toggle("register-page");
    document.documentElement.addEventListener("mousemove", followCursor);
    // Specify how to clean up after this effect:
    return function cleanup() {
      document.body.classList.toggle("register-page");
      document.documentElement.removeEventListener("mousemove", followCursor);
    };
  }, []);
  const followCursor = (event) => {
    let posX = event.clientX - window.innerWidth / 2;
    let posY = event.clientY - window.innerWidth / 6;
    setSquares1to6(
      "perspective(500px) rotateY(" +
        posX * 0.05 +
        "deg) rotateX(" +
        posY * -0.05 +
        "deg)"
    );
    setSquares7and8(
      "perspective(500px) rotateY(" +
        posX * 0.02 +
        "deg) rotateX(" +
        posY * -0.02 +
        "deg)"
    );
  };

  return (
    <>
      <ExamplesNavbar />
      <div className="wrapper">
        <div className="page-header">
          <div className="page-header-image" />
          <div className="content">
            <Container>
              <Row>
                <Col className="offset-lg-0 offset-md-3" lg="5" md="6">
                  <div
                    className="square square-7"
                    id="square7"
                    style={{ transform: squares7and8 }}
                  />
                  <div
                    className="square square-8"
                    id="square8"
                    style={{ transform: squares7and8 }}
                  />
                  <Card className="card-register">
                    <CardHeader>
                      <CardImg
                        alt="..."
                        src={require("assets/img/square-purple-1.png").default}
                      />
                      <CardTitle tag="h4">Register</CardTitle>
                      <Register />
                    </CardHeader>
                  </Card>
                </Col>
              </Row>
              <div className="register-bg" />
              <div
                className="square square-1"
                id="square1"
                style={{ transform: squares1to6 }}
              />
              <div
                className="square square-2"
                id="square2"
                style={{ transform: squares1to6 }}
              />
              <div
                className="square square-3"
                id="square3"
                style={{ transform: squares1to6 }}
              />
              <div
                className="square square-4"
                id="square4"
                style={{ transform: squares1to6 }}
              />
              <div
                className="square square-5"
                id="square5"
                style={{ transform: squares1to6 }}
              />
              <div
                className="square square-6"
                id="square6"
                style={{ transform: squares1to6 }}
              />
            </Container>
          </div>
        </div>
        <Footer />
      </div>
    </>
  );
}
class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      fullname: "",
      password: "",
      fullNameFocus: false,
      emailFocus: false,
      passwordFocus: false,
      url: "",
      toHome: false
    };
    this.handleChangeEmail = this.handleChangeEmail.bind(this);
    this.handleChangeFullName = this.handleChangeFullName.bind(this);
    this.handleChangePassWord = this.handleChangePassWord.bind(this);

    this.handleSubmit = this.handleSubmit.bind(this);
  }
  myFunc(){
    
  }
  handleChangeEmail(event) {
    this.setState({ email: event.target.value });
  }
  handleChangeFullName(event) {
    this.setState({ fullname: event.target.value });
  }
  handleChangePassWord(event) {
    this.setState({ password: event.target.value });
  }
  handleSubmit() {
    if (
      this.state.email !== "" ||
      this.state.fullname !== "" ||
      this.state.password !== ""
    ) {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: this.state.email,
          name: this.state.fullname,
          password: this.state.password,
        }),
      };
      //Use GET method to get data from UI to Database.
      fetch(
        "http://localhost:8000/api/create-user",
        requestOptions
      ).then((response) =>{
        if(response.status === 200){
          this.refs.notify.notificationAlert(options)
          return response.json();     
        }else{
          //chuyển đường dẫn về home,
          this.setState({toHome: true})
          localStorage.setItem('username', this.state.email);
        }
        
      });
    }
    else{
      this.refs.notify.notificationAlert(options);
    }
  }
  render() {
    if (this.state.toHome === true) {
      return (<Redirect to='/' />);
    }
    return (
      <Form onSubmit={this.handleSubmit} action="#" className="form">
        <CardBody>
          <InputGroup
            className={classnames({
              "input-group-focus": this.state.fullNameFocus,
            })}
          >
            <InputGroupAddon addonType="prepend">
              <InputGroupText>
                <i className="tim-icons icon-single-02" />
              </InputGroupText>
            </InputGroupAddon>
            <Input
              required
              onChange={this.handleChangeFullName}
              placeholder="Full Name"
              value={this.state.fullname}
              type="text"
              onFocus={(e) => this.setState({ fullNameFocus: true })}
              onBlur={(e) => this.setState({ fullNameFocus: false })}
            />
          </InputGroup>
          <InputGroup
            className={classnames({
              "input-group-focus": this.state.emailFocus,
            })}
          >
            <InputGroupAddon addonType="prepend">
              <InputGroupText>
                <i className="tim-icons icon-email-85" />
              </InputGroupText>
            </InputGroupAddon>
            <Input
              required
              onChange={this.handleChangeEmail}
              value={this.state.email}
              placeholder="Email"
              type="text"
              onFocus={(e) => this.setState({ emailFocus: true })}
              onBlur={(e) => this.setState({ emailFocus: false })}
            />
          </InputGroup>
          <InputGroup
            className={classnames({
              "input-group-focus": this.state.passwordFocus,
            })}
          >
            <InputGroupAddon addonType="prepend">
              <InputGroupText>
                <i className="tim-icons icon-lock-circle" />
              </InputGroupText>
            </InputGroupAddon>
            <Input
              required
              onChange={this.handleChangePassWord}
              placeholder="Password"
              value={this.state.password}
              type="password"
              onFocus={(e) => this.setState({ passwordFocus: true })}
              onBlur={(e) => this.setState({ passwordFocus: false })}
            />
          </InputGroup>
          <FormGroup check className="text-left">
            <Label check>
              <Input type="checkbox" />
              <span className="form-check-sign" />I agree to the{" "}
              <a href="#pablo" onClick={(e) => e.preventDefault()}>
                terms and conditions
              </a>
              .
            </Label>
          </FormGroup>
        </CardBody>
        <CardFooter>
          <NotificationAlert ref="notify" zIndex={9999}/>
          <Button className="btn-round" color="primary" size="lg">
            Get Started
          </Button>
          Or
          <Facebook />
        </CardFooter>
      </Form>
    );
  }
}
