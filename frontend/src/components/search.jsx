import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import DatePicker from "react-datepicker";
import dateFormat from "dateformat";
import {startOfWeek, endOfWeek} from 'date-fns'

const Search = () => {
    const [dateRange, setDateRange] = useState([
        startOfWeek(new Date(), {weekStartsOn: 6}), 
        endOfWeek(new Date(), {weekStartsOn: 6})
    ]);
    const [startDate, endDate] = dateRange;
    
    console.log(dateFormat(startDate, "isoDateTime").split("T")[0] + "\n" + dateFormat(endDate, "isoDateTime").split("T")[0])

    return (
        <div className='search'>
            <Form>
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
