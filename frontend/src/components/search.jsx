import React, { useState, forwardRef } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import DatePicker from "react-datepicker";
import dateFormat from "dateformat";
import {startOfWeek, endOfWeek} from 'date-fns'
import axios from 'axios'

const Search = props => {
    const [dateRange, setDateRange] = useState([
        startOfWeek(new Date(), {weekStartsOn: 6}), 
        endOfWeek(new Date(), {weekStartsOn: 6})
    ]);
    
    const [startDate, endDate] = dateRange;

    const CustomInput = forwardRef(({ value, onClick }, ref) => (
        <Button className="custom-input" onClick={onClick} ref={ref}>
            {value}
        </Button>
        ));


    const formData = data => dateFormat(data, "isoDateTime").split("T")[0]

    const handleSubmit = e => {
        e.preventDefault();

        var data = {
            "start_date": formData(startDate),
            "final_date": formData(endDate)
        }

        console.log(data    )

        axios.post('https://tim-fs.herokuapp.com/api/get_data', data, {
            headers: {
                "Access-Control-Allow-Origin": "*",
                'Content-Type': "application/json"
            }
        }).then(res => props.data(res.data)).catch(err => console.log(err))
    }

    return (
        <div className="search d-flex justify-content-center" style={{width: "100%"}}>
            <Form>
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>Выберете даты:</Form.Label>
                    <DatePicker
                    selectsRange={true}
                    startDate={startDate}
                    endDate={endDate}
                    onChange={(update) => {
                        setDateRange(update);
                    }}
                    customInput={<CustomInput />}
                    dateFormat="dd.MM.yyyy"
                    showMonthDropdown
                    showYearDropdown
                    withPortal
                    />
                </Form.Group>
                <Button className="formBtn" onClick={handleSubmit}>Поиск</Button>
            </Form>
        </div>
    );
}

export default Search;
