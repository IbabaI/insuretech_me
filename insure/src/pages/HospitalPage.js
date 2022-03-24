import axios from "axios";
import React, { useState } from "react";
import Header from "../components/Header";
import SearchInput from "../components/Hospital/SearchInput";
import SearchResult from "../components/Hospital/SearchResult";

const PhamacyPage = () => {
  const [HospitalList, setPhamacyList] = useState([]);
  const [searchInputText, setSearchInputText] = useState("");

  const handleChange = (event) => {
    const { value } = event.target;
    setSearchInputText(value);
  };

  const handleClick = () => {
    const option = {
      method: "GET",
      url: "http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1",
      params: {
        ServiceKey:
          "RYlCnxxOruxJFp9YOSb8KEPqtNk2YnQu%2Fseqnlzx9iYdkhnBc6Be077oaAxMiYxxMJPA4QhpAeMUJJ6I047Lyg%3D%3D",
          sidoCd: 110000,
          clCd: 31,
          yadmNm: searchInputText,
      },
    };

    axios(option).then(function ({ data }) {
      console.log(data);
      setPhamacyList(data.response.body.items.item);
    });
  };
  return (
    <div>
    <Header title={"병원정보 목록"} />
    <SearchInput
      handleChange={handleChange}
      handleClick={handleClick}
    ></SearchInput>
    <SearchResult hospitalList={hospitalList}></SearchResult>
    {
      //searchInput
      //searchList <- HospitalListItem
      /* HospitalListItem 컴포넌트를 활용하여 병원 목록을 출력 searchList 안에 선언 */
    }
  </div>
);
};

export default HospitalPage;