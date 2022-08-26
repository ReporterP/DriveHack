import React, {useRef} from 'react';
import { CSVLink } from 'react-csv'
import Button from 'react-bootstrap/Button';

const DownloadInput = props => {
    const csvLink = useRef() 
    
    const getTransactionData = () => csvLink.current.link.click()

    return (
        <div className='DownloadInput'>
            <Button onClick={getTransactionData}>Скачать CSV</Button>
            <CSVLink
                data={props.search}
                filename='top.csv'
                className='hidden'
                ref={csvLink}
                target='_blank'
            />
        </div>
    );
}

export default DownloadInput;
