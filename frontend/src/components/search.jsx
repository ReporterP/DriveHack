import React from 'react';
import Form from 'react-bootstrap/Form';

const Search = () => {
    return (
        <div className='search'>
            <Form>
                <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                    <Form.Label>date</Form.Label>
                    <Form.Control type="date" />
                </Form.Group>
                {/* <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
                    <Form.Label>Example textarea</Form.Label>
                    <Form.Control as="textarea" rows={3} />
                </Form.Group> */}
            </Form>
        </div>
    );
}

export default Search;
