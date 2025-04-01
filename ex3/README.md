# User Management System with Django and React

A full-stack web application for managing users and their preferences, built with Django REST Framework backend and React frontend.

## Features

- User creation with name, email, and preferences
- Affiliate status tracking
- Preference management with even/odd number validation
- Responsive card-based UI
- Real-time form validation
- API integration with external test server

## Project Structure

```
ex3/
├── backend/         # Django REST Framework backend
│   ├── myapp/       # Main application
│   └── backend/     # Project settings
└── frontend/        # React frontend application
    └── frontend/    # React components and assets
```

## Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers requests
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

The backend server will be running at `http://localhost:8000`

## Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend/frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The frontend application will be running at `http://localhost:3000`

## API Endpoints

### GET /api/users/
Retrieve all users with their preferences

### POST /api/users/create/
Create a new user

Request body:
```json
{
    "name": "string",
    "email": "string",
    "preferences": ["string"],
    "affiliate": boolean
}
```

Validation rules:
- Name and email are required
- Preferences must include at least one even and one odd number
- Duplicate preferences are not allowed

## Features Description

### User Form
- Input validation for required fields
- Preference validation for even/odd numbers
- Affiliate status toggle
- Error message display

### User Cards
- Responsive grid layout
- Color-coded cards based on affiliate status
- Sorted preference display
- Clickable email links

## Technology Stack

### Backend
- Django 5.1.7
- Django REST Framework
- SQLite database
- django-cors-headers

### Frontend
- React
- React Bootstrap
- Axios for API requests
- CSS for custom styling

## Error Handling

The application includes comprehensive error handling for:
- Form validation errors
- API request failures
- Database constraints
- External service integration