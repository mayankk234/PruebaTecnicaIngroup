import React from 'react';
import ReactDOM from 'react-dom/client';  // Cambia esta importación
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';

// Crear una raíz en lugar de usar ReactDOM.render
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
