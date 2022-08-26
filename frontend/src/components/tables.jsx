import React from 'react';
import Table from 'react-bootstrap/Table';
import DownloadInput from './DownloadInput';

const Tables = props => {
    return (
        <div id='tables' className='tables'>
            {Object.keys(props.data).length===0?<></>:
                <Table striped bordered hover>
                    <thead>
                        <tr>
                        <th>Имя компании</th>
                        <th>Количество упонинаний</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            Object.entries(props.data).map(e=><tr>{e.map(e=><td>{e}</td>)}</tr>)
                        }
                    </tbody>
                </Table>
            }
        <DownloadInput/>
        </div>
    );
}

export default Tables;
