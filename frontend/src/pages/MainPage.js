import React, {useState} from 'react';
import Search from '../components/search';
import Container from 'react-bootstrap/Container';
import Tables from '../components/tables';

const MainPage = () => {

    const [data, setdata] = useState({})

    return (
        <div>
            <Container>
                <Search data={setdata} />
                <Tables data={data}/>
            </Container>
        </div>
    );
}

export default MainPage;
