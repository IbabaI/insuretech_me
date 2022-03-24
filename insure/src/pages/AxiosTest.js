import React from "react";
import axios from "axios";
import Header from "../components/Header";

const AxiosTest = () => {
  const handleClick = () => {
    axios.get(
        "https://newsapi.org/v2/everything?q=tesla&from=2022-02-23&sortBy=publishedAt&apiKey=84c96b195b1e4e97b8cb2e5cd8977e9f"
        ).then(function (response) {
      // handle success
      console.log(response);
    });
  };
  return(
    <>  
        <Header title={"데이터 요청 실습"}></Header>
        <button onClick={handleClick}>요청 전송</button>;
    </>
  ) 
};

export default AxiosTest;
