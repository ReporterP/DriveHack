import React from 'react';

import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
// import Button from 'react-bootstrap/Button';
// import Form from 'react-bootstrap/Form';

const Header = () => {
    return (
        <>
            <Navbar expand="lg">
                <Container>
                    <Navbar.Brand href="#">TIMFS</Navbar.Brand>
                    {/* <Navbar.Toggle aria-controls="navbarScroll" />
                    <Navbar.Collapse id="navbarScroll">
                    <Form className="d-flex">
                        <Form.Control
                        type="search"
                        placeholder="Поиск"
                        className="me-2"
                        aria-label="Search"
                        />
                        <Button>Поиск</Button>
                    </Form>
                    </Navbar.Collapse> */}
                </Container>
            </Navbar>
        </>
    );
}

export default Header;
