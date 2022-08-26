import React, {useState} from 'react';
import Search from '../components/search';
import Container from 'react-bootstrap/Container';
import Tables from '../components/tables';
import DownloadInput from '../components/DownloadInput';

const MainPage = () => {

    const [data, setdata] = useState({})

    return (
        <div className='mainPage'>
            <DownloadInput/>
            <Container>
                <Search data={setdata} />
                <Tables data={data}/>
            </Container>
        </div>
    );
}

export default MainPage;
