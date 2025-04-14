import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

interface Cart {
  id: number;
  items: any[];
}

const Carts: React.FC = () => {
  const [carts, setCarts] = useState<Cart[]>([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/carts')
      .then(response => setCarts(response.data))
      .catch(error => console.error('Error fetching carts:', error));
  }, []);

  return (
    <>
      <h1 className="text-center mb-4">Carts</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Items</th>
          </tr>
        </thead>
        <tbody>
          {carts.map(cart => (
            <tr key={cart.id}>
              <td>{cart.id}</td>
              <td>{cart.items.length} items</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </>
  );
};

export default Carts;
