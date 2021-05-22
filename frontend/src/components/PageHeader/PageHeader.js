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
import SearchBar from "material-ui-search-bar";

// reactstrap components
import { Container } from "reactstrap";

export default function PageHeader() {
  const [searchText, setSearchText] = React.useState("");
  const handleChange = (event) => {
    console.log(searchText)
  }
  return (
    <div className="page-header header-filter">
      <div className="squares square1" />
      <div className="squares square2" />
      <div className="squares square3" />
      <div className="squares square4" />
      <div className="squares square5" />
      <div className="squares square6" />
      <div className="squares square7" />
      <Container>
        <div className="content-center brand">
          <SearchBar
            style={{
              "margin-left": "5%",
              "margin-right": "5%",
              "margin-bottom": "10%",
            }}
            placeholder="Search 30,000 online courses"
            size="large"
            value={searchText}
            onChange={(newValue) => setSearchText(newValue)}
            onRequestSearch={() => 
              {
                
                const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                  queries: [searchText],
                  k: 10
                }),
              };
              //Use POST method to get value from UI to API.
              fetch(
                "http://localhost:8000/api/course-list",
                requestOptions
              ).then((response) =>{
                if(response.status === 200){
                 
                  return response.json();     
                }else{
                 
                }
                
              });}
            }
            
          />
          
          <h1 className="h1-seo">Best Course For You</h1>
          <h3 className="d-none d-sm-block">
            A project is developed by cool guys.
          </h3>
        </div>
      </Container>
    </div>
  );
}
