import React, {useState} from 'react';
import Search from '../components/search';
import Container from 'react-bootstrap/Container';
import Tables from '../components/tables';
import DownloadInput from '../components/DownloadInput';

const MainPage = () => {

    const [data, setdata] = useState({})
    const [Download, setDownload] = useState(false)
    const [transactionData, setTransactionData] = useState("")

    return (
        <div className='mainPage'>
            {Download && <DownloadInput search={transactionData}/>}
            <Container>
                <Search data={setdata} download={setDownload} search={setTransactionData}/>
                <Tables data={data}/>
            </Container>
        </div>
    );
}

export default MainPage;
