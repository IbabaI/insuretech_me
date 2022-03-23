import React, {useState} from 'react'
// rafce 자동완성
const InputTest = () => {
//    let text = "test";
    const [text, setText] = useState("test");

    const handleChange = (event) => {
        const { value} = event.target;
        setText(value);
        console.log(text);
    };
  return (
    <div>
        <p>{text}</p>
        <input onChange={handleChange}></input>
    </div>
  );
};

export default InputTest;