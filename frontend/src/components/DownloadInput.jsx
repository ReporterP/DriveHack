import React, {useState, useRef} from 'react';
import { CSVLink } from 'react-csv'
import Button from 'react-bootstrap/Button';
import axios from 'axios'

const DownloadInput = () => {
    const [transactionData, setTransactionData] = useState([])
    const csvLink = useRef() 
    
    const getTransactionData = () => {
        // 'api' just wraps axios with some setting specific to our app. the important thing here is that we use .then to capture the table response data, update the state, and then once we exit that operation we're going to click on the csv download link using the ref
        axios.get('https://tim-fs.herokuapp.com/api/get_csv',{
            headers: {
                "Access-Control-Allow-Origin": "*",
                'Content-Type': "application/json"
            }
        }).then(res => setTransactionData(res.data)).catch(err => console.log(err))
        csvLink.current.link.click()        
        }

    return (
        <div className='DownloadInput'>
            <Button onClick={getTransactionData}>Загрузить CSV</Button>
            <CSVLink
                data={transactionData}
                filename='top.csv'
                className='hidden'
                ref={csvLink}
                target='_blank'
            />
        </div>
    );
}

export default DownloadInput;
