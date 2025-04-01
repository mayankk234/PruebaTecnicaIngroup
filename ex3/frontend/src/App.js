import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserForm from './components/UserForm';
import UserCard from './components/UserCard';
import { Container, Row, Col } from 'react-bootstrap';

const App = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchUsers = () => {
    setLoading(true);
    axios.get('http://localhost:8000/api/users/')
      .then(response => {
        setUsers(response.data.users);
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <Container fluid className="vh-100 py-4" style={{ backgroundColor: '#f8f9fa' }}>
      <Row className="h-100">
        <Col md={4} className="mb-3">
          <div className="sticky-top pt-2">
            <h2 className="mb-4">Add New User</h2>
            <UserForm setUsers={setUsers} />
          </div>
        </Col>
        <Col md={8}>
          <h2 className="mb-4">User List</h2>
          <Row>
            {loading ? (
              <Col className="text-center">
                <div>Loading users...</div>
              </Col>
            ) : users.map(user => (
              <Col lg={6} xl={4} key={user.email} className="mb-4">
                <UserCard user={user} />
              </Col>
            ))}
          </Row>
        </Col>
      </Row>
    </Container>
  );
};

export default App;