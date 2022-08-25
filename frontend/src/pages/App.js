import {Routes, Route} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/main.scss';
import MainPage from "./MainPage";
import Header from "../components/header";
import Footer from "../components/footer";

function App() {
  return (
    <>
      <Header/>
        <Routes>
          <Route exact path="/" element={<MainPage/>}/>
        </Routes>
      <Footer/>
    </>
  );
}

export default App;
