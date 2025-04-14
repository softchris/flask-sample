import React, { useState } from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';
import Products from './components/Products';
import Users from './components/Users';
import Carts from './components/Carts';

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<string>('products');

  const renderContent = () => {
    switch (activeTab) {
      case 'products':
        return <Products />;
      case 'users':
        return <Users />;
      case 'carts':
        return <Carts />;
      default:
        return <Products />;
    }
  };

  return (
    <>
      <Navbar bg="dark" variant="dark" expand="lg">
        <Container>
          <Navbar.Brand href="#">Flask Sample</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link onClick={() => setActiveTab('products')}>Products</Nav.Link>
            <Nav.Link onClick={() => setActiveTab('users')}>Users</Nav.Link>
            <Nav.Link onClick={() => setActiveTab('carts')}>Carts</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <Container className="mt-4">
        {renderContent()}
      </Container>
    </>
  );
};

export default App;
