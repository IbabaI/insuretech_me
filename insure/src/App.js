import logo from './logo.svg';
import './App.css';
import Header from './components/Header';

function App() {
  return (
    <>
      <h1>안녕하세요</h1>
      <h3>리엑트 입니다</h3>
      <Header title={"테스트 페이지1"}></Header>
      <Header title={"테스트 페이지2"}></Header>
      <Header title={"테스트 페이지3"}></Header>

    </>
  );
}

export default App;