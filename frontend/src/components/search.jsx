import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import DatePicker from "react-datepicker";
import dateFormat from "dateformat";
import {startOfWeek, endOfWeek} from 'date-fns'
import axios from 'axios'

const Search = () => {
    const [dateRange, setDateRange] = useState([
        startOfWeek(new Date(), {weekStartsOn: 6}), 
        endOfWeek(new Date(), {weekStartsOn: 6})
    ]);
    const [startDate, endDate] = dateRange;

    const formData = data => dateFormat(data, "isoDateTime").split("T")[0]

    const handleSubmit = e => {
        e.preventDefault();  
        var data = {
            "start_date": formData(startDate),
            "final_date": formData(endDate)
        }
        console.log(data)

        // axios.post('http://127.0.0.1:5000/api/get_csv', data, {
        //     headers: {
        //         "Access-Control-Allow-Origin": "*",
        //         'Content-Type': "multipart/from-data"
        //     }
        // }).then(res =>  console.log(res.data)).catch(err => console.log(err))
    }

    return (
        <div className='search'>
            <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Выберете даты</Form.Label>
                    <DatePicker
                    selectsRange={true}
                    startDate={startDate}
                    endDate={endDate}
                    onChange={(update) => {
                        setDateRange(update);
                    }}
                    dateFormat="dd.MM.yyyy"
                    withPortal
                    />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    );
}

export default Search;
