import React from 'react';
import Table from 'react-bootstrap/Table';

const Tables = props => {
    const data = Object.fromEntries(Object.entries(props.data).sort(([,a],[,b]) => a-b));
    console.log(data)
    return (
        <div id='tables' className='tables'>
            {Object.keys(data).length===0?<></>:
                <Table striped bordered hover>
                    <thead>
                        <tr>
                        <th>Имя компании</th>
                        <th>Количество упонинаний</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            Object.entries(data).map(e=><tr>{e.map(e=><td>{e}</td>)}</tr>)
                        }
                    </tbody>
                </Table>
            }
        </div>
    );
}

export default Tables;
