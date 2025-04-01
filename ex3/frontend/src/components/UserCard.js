import React from 'react';
import { Card, Image, Row, Col } from 'react-bootstrap';

const UserCard = ({ user }) => {
  const sortedPreferences = Array.isArray(user?.preferences) ? [...user.preferences].sort((a, b) => parseInt(a) - parseInt(b)) : [];

  return (
    <Card className="m-2 h-100" style={{ 
      backgroundColor: user?.affiliate ? '#28a745' : '#6c757d', 
      color: 'white',
      boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
      borderRadius: '10px'
    }}>
      <Card.Body>
        <Card.Title className="h4 mb-3">{user?.name}</Card.Title>
        <Card.Text>
          <a 
            href={`mailto:${user?.email}`} 
            style={{ 
              color: 'white', 
              textDecoration: 'none',
              borderBottom: '1px solid white'
            }}
          >
            {user?.email}
          </a>
        </Card.Text>
        <Card.Text className="mt-3">
          <strong>Preferencias:</strong>
          {sortedPreferences.length > 0 ? (
            <Row className="mt-2">
              {sortedPreferences.map((preference, index) => (
                <Col key={index} xs={4} className="mb-2 text-center">
                  <div className="small">{preference}</div>
                </Col>
              ))}
            </Row>
          ) : (
            <div className="text-center mt-2">No preferences</div>
          )}
        </Card.Text>
      </Card.Body>
    </Card>
  );
};

export default UserCard;