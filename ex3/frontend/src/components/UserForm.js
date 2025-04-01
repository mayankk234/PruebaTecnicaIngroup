import React, { useState } from 'react';
import axios from 'axios';
import { Form, Button } from 'react-bootstrap';

const UserForm = ({ setUsers }) => {
  const [formData, setFormData] = useState({ name: '', email: '', preferences: '', affiliate: false });
  const [error, setError] = useState('');

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    setError('');  // Resetear el error antes de enviar la solicitud

    // Convert preferences string to array and clean it
    const dataToSend = {
      ...formData,
      preferences: formData.preferences.split(',').map(p => p.trim()).filter(p => p),
      affiliate: formData.affiliate  // Send the boolean value directly
    };

    axios.post('http://localhost:8000/api/users/create/', dataToSend)
      .then(response => {
        // Fetch updated user list after successful creation
        axios.get('http://localhost:8000/api/users/')
          .then(response => {
            setUsers(response.data.users);
          })
          .catch(error => {
            console.error('Error fetching updated users:', error);
          });
        // Reset form after successful submission
        setFormData({ name: '', email: '', preferences: '', affiliate: false });
      })
      .catch(error => {
        if (error.response) {
          setError(error.response.data.error);  // Mostrar el error devuelto por la API
        } else {
          setError('Hubo un error en la conexión. Intenta nuevamente.');
        }
      });
  };

  return (
    <Form onSubmit={handleSubmit} className="p-4 bg-white rounded shadow-sm">
      {error && <div className="alert alert-danger">{error}</div>}
      <Form.Group className="mb-3">
        <Form.Label>Nombre</Form.Label>
        <Form.Control 
          type="text" 
          name="name" 
          value={formData.name}
          onChange={handleChange} 
          placeholder="Enter your name"
          className="form-control-lg"
          required 
        />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Email</Form.Label>
        <Form.Control 
          type="email" 
          name="email" 
          value={formData.email}
          onChange={handleChange} 
          placeholder="Enter your email"
          className="form-control-lg"
          required 
        />
      </Form.Group>
      <Form.Group className="mb-3">
        <Form.Label>Preferencias (comma separated numbers)</Form.Label>
        <Form.Control 
          type="text" 
          name="preferences" 
          value={formData.preferences}
          onChange={handleChange} 
          placeholder="e.g., 1,2,3,4"
          className="form-control-lg"
          required 
        />
        <Form.Text className="text-muted">
          Enter numbers separated by commas. Include at least one even and one odd number.
        </Form.Text>
      </Form.Group>
      <Form.Group className="mb-4">
        <Form.Check 
          type="checkbox" 
          label="Afiliado" 
          name="affiliate" 
          checked={formData.affiliate}
          onChange={e => setFormData({ ...formData, affiliate: e.target.checked })} 
          className="form-check-lg"
        />
      </Form.Group>
      <Button 
        type="submit" 
        variant="primary" 
        size="lg" 
        className="w-100"
      >
        Enviar
      </Button>
    </Form>
  );
};

export default UserForm;
