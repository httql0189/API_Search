import React from "react";
import { makeStyles } from "@material-ui/core/styles";
// import Grid from '@material-ui/core/Grid';
// import CardActions from '@material-ui/core/CardActions';
// import CardMedia from '@material-ui/core/CardMedia';
// import Typography from '@material-ui/core/Typography';
// import Link from '@material-ui/core/Link';
import { ReactComponent as StarIcon } from "images/star-icon.svg";
import { PrimaryButton as PrimaryButtonBase } from "components/misc/Buttons.js";
import { css } from "styled-components/macro";
import styled from "styled-components";
import { motion } from "framer-motion";
import tw from "twin.macro";
// reactstrap components
import { Button, Container } from "reactstrap";

import ExamplesNavbar from "components/Navbars/IndexNavbar.js";
import { event } from "jquery";
// import Footer from "components/Footer/Footer.js";
// import { Group } from '@material-ui/icons';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  icon: {
    marginRight: theme.spacing(2),
  },
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(3),
  },
  card: {
    height: "85%",
    display: "flex",
    flexDirection: "column",
  },
  cardMedia: {
    paddingTop: "56.25%", // 16:9
  },
  cardContent: {
    flexGrow: 1,
  },
  cardDecor: {
    "border-radius": 1,
  },
}));
const cards = [];

const CardHoverOverlay = styled(motion.div)`
  background-color: rgba(255, 255, 255, 0.5);
  ${tw`absolute inset-0 flex justify-center items-center`}
`;
const TabContent = tw(
  motion.div
)`mt-6 flex flex-wrap sm:-mr-10 md:-mr-6 lg:-mr-12`;
const CardButton = tw(PrimaryButtonBase)`text-sm`;
const CardContainer = tw.div`mt-10 w-full sm:w-1/2 md:w-1/3 lg:w-1/4 sm:pr-10 md:pr-6 lg:pr-12`;
const CardImageContainer = styled.div`
  ${(props) =>
    css`
      background-image: url("${props.imageSrc}");
    `}
  ${tw`h-56 xl:h-64 bg-center bg-cover relative`}
`;
const CardRatingContainer = tw.div`leading-none absolute inline-flex bg-gray-100 bottom-0 left-0 ml-4 mb-4 rounded-full px-5 py-2 items-end`;
const CardReview = tw.div`font-medium text-xs text-gray-600`;
const Card = tw(
  motion.a
)`bg-gray-200 block max-w-xs mx-auto sm:max-w-none sm:mx-0`;
const CardText = tw.div`p-4 text-gray-900`;
const CardTitle = tw.p`mt-1 text-sm font-bold text-gray-600`;
// /tw.h1`text-lg font-semibold group-hover:text-primary-500`
// const CardContent = tw.p`mt-1 text-sm font-medium text-primary-600`;
// const CardPrice = tw.p`mt-4 text-xl font-bold`;
const CardRating = styled.div`
  ${tw`mr-1 text-sm font-bold flex items-end`}
  svg {
    ${tw`w-4 h-4 fill-current text-orange-400 mr-1`}
  }
`;
// const TabsControl = tw.div`flex flex-wrap bg-gray-200 px-2 py-2 leading-none mt-12 xl:mt-0`;
const TabControl = styled.div`
  ${tw`cursor-pointer px-6 py-3 mt-2 sm:mt-0 sm:mr-2 last:mr-0 text-gray-600 font-medium rounded-sm duration-300 text-sm sm:text-base w-1/2 sm:w-auto text-center`}
  &:hover 
    ${tw`bg-gray-300 text-gray-700`}
  }
  ${(props) => props.active && tw`bg-primary-500! text-gray-100!`}
  }
`;
export default function SpacingGrid() {
  const [spacing, setSpacing] = React.useState(2);
  const classes = useStyles();

  const [listCourse, setListCourse] = React.useState();

  const [isDetail, setIsDetail] = React.useState();

  const detailCourse = (event) =>{
    
    window.location.href="/detail-course?course="+event.target.value; //just get value(course_tag) to use for call API (GET method ) at landingpage
  }

  const tabsKeys = Object.keys(cards);
  const [activeTab, setActiveTab] = React.useState(tabsKeys);
  window.onload = (response) => {
    let arr = [];
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    fetch("http://localhost:8000/api/course?limit=10", requestOptions) //this is course data.
      .then((response) => response.json())

      .then((data) => {
        for (var i = 0; i < 10; i++) {
          cards.push(data.results[i]);
        }
        setListCourse(Array(arr));
        // console.log(cards)
      });
    //.then((data) => this.props.history.push("/room/" + data.code));
  };
  return (
    <>
      <ExamplesNavbar />
      <div className="wrapper">
        <div className="page-header-image" />
        <div className="content">
          <Container className={classes.cardGrid} maxWidth="md">
            {/* End hero unit */}
            {/* <TabsControl>
                {Object.keys(cards).map((tabName, index) => (
                  <TabControl key={index} active={activeTab === tabName} onClick={() => setActiveTab(tabName)}>
                    {tabName}
                  </TabControl>
                ))}
              </TabsControl> */}
            {[0].map((tabsKey, index) => (
              <TabContent
                key={index}
                variants={{
                  current: {
                    opacity: 1,
                    scale: 1,
                    display: "flex",
                  },
                  hidden: {
                    opacity: 0,
                    scale: 0.8,
                    display: "none",
                  },
                }}
                transition={{ duration: 0.4 }}
                initial="hidden"
                animate="current"
              >
                {cards.map((card, index) => (
                  <CardContainer key={index}>
                    <Card
                      className="group"
                      initial="rest"
                      whileHover="hover"
                      animate="rest"
                    >
                      <CardImageContainer imageSrc={card.course_image}>
                        <CardRatingContainer>
                          <CardRating>
                            <StarIcon />
                            {card.rating}
                          </CardRating>
                          <CardReview>({card.rating_count})</CardReview>
                        </CardRatingContainer>
                        <CardHoverOverlay
                          variants={{
                            hover: {
                              opacity: 1,
                              height: "auto",
                            },
                            rest: {
                              opacity: 0,
                              height: 0,
                            },
                          }}
                          transition={{ duration: 0.3 }}
                        >
                          {/*  <button>Detail</button> */}
                          <Button
                            className="nav-link d-none d-lg-block"
                            color="secondary"
                            value={card.course_tag}
                            onClick={detailCourse} //this is input prams for function.
                          >
                            Detail
                          </Button>
                        </CardHoverOverlay>
                      </CardImageContainer>
                      <CardText>
                        <CardTitle>{card.course_title}</CardTitle>
                        {/* <CardContent>{card.content}</CardContent>
                          <CardPrice>{card.price}</CardPrice> */}
                      </CardText>
                    </Card>
                  </CardContainer>
                ))}
              </TabContent>
            ))}
          </Container>
        </div>
      </div>
    </>
  );
}

