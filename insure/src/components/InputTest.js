import React from 'react'
// rafce 자동완성
const InputTest = () => {
    const handleChange = (event) => {
        const { value} = event.target;
        console.log(value);
    };
  return (
    <div>
        <input onChange={handleChange}></input>
    </div>
  );
};

export default InputTest;