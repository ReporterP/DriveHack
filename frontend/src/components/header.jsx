import React from 'react';

import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';


const Header = () => {
    return (
        <header>
            <Navbar expand="lg">
                <Container>
                    <Navbar.Brand href="#">TIMFS</Navbar.Brand>               
                </Container>
            </Navbar>
        </header>
    );
}

export default Header;
