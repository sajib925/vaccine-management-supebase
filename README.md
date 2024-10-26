## Vaccination Management System with Role-Based User Features

This vaccination management system backend offers authentication and profile updates. Doctors can create campaigns and add vaccines, while patients can book vaccinations and leave reviews. Built with Django REST Framework.

## Tech Stack

- **Backend**: 
  - Django REST Framework

## API Endpoints

Here are the available API endpoints:


### Admin
- **Admin Panel**: `/admin/`

### Authentication
- **API Authentication**: `/api-auth/`
- **User Registration**: `/api/patient/register/`
- **User Login**: `/api/patient/login/`
- **User Profile Update**: `/api/patient/profile/`
- **Password Update**: `/api/patient/password/`
- **User Logout**: `/api/patient/logout/`

### Contact
- **Contact Us**: `/api/contact/`

### Services
- **Service List & Create**: `/api/service/`

### Booking
- **Booking List & Create**: `/api/booking/`
- **Booking Detail & Delete**: `/api/booking/<int:pk>/`

### Review
- **Review (Comment) List**: `/api/review/`

### Campaign
- **Campaign List**: `/api/campaign/`
- **Campaign Detail**: `/api/campaign/<int:pk>/`

### Vaccine
- **Vaccine List**: `/api/campaign/vaccine/`
- **Vaccine Detail**: `/api/campaign/vaccine/<int:pk>/`

### Patient
- **Patient List & Create**: `/api/patient/`
- **Patient Detail**: `/api/patient/<int:pk>/`

### Doctor
- **Doctor List & Create**: `/api/doctor/`
- **Doctor Detail**: `/api/doctor/<int:pk>/`


**Base URL**: [https://vaccine-management-supebase.vercel.app](https://vaccine-management-backend-j2ii.onrender.com/)

## Features

# Project Features

### User Management
- **User Authentication**: Allows users to register, log in, and log out.
- **Profile Management**: Users can update their profile details and change their password.

### Doctor Functionality
- **Campaign Management**: Doctors can create, update, and manage vaccination campaigns.
- **Vaccine Management**: Doctors can add new vaccines and manage existing ones within campaigns.

### Patient Functionality
- **Appointment Booking**: Patients can book vaccination appointments for available campaigns.
- **Review System**: Patients can leave reviews for specific vaccines and campaigns, sharing their feedback and experiences.



## Installation

To set up the backend on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sajib925/vaccine-management-supebase
   cd vaccination-management-backend
