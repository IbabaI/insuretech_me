import logo from './logo.svg';
import './App.css';

const Welcome = ({userName, age}) => {
  //console.log(props);
  return <h2>안녕하세요{userName} {age}</h2>;
};

function App() {
  return (
    <>
      <h1>안녕하세요</h1>
      <h3>리엑트 입니다</h3>
      <Welcome userName={"홍길동"} age={45}></Welcome>
      <Welcome userName={"고귀남"} age={13}></Welcome>
    </>
  );
}

export default App;
