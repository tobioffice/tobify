# Tobify - Student Management System 📚

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-4.0+-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-13+-blue.svg)](https://www.postgresql.org/)

A modern and comprehensive web application for managing student notes, attendance, and user authentication.

## 🌐 Live Demo

Check out our live demo at [https://5qd-resolute-tesla.circumeo-apps.net/](https://5qd-resolute-tesla.circumeo-apps.net/)

## ✨ Core Features

### 🔐 Authentication System
- User registration with email verification
- Secure login system
- Password reset functionality
- Email-based OTP verification

### 📝 Notes Management
- Create, edit, and delete personal notes
- Make notes public or private
- Share notes with other users
- Organize notes by categories
- Rich text editor support

### 📊 Attendance Tracking
- Track attendance for 2nd year students
- View attendance records by date
- Generate attendance reports
- Mark attendance status (Present/Absent)

## 🛠️ Technical Stack

### Backend
- [Django](https://www.djangoproject.com/) - Python web framework
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Django REST Framework](https://www.django-rest-framework.org/) - API

### Security
- JWT Authentication
- Email verification
- Environment variables for sensitive data

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tobify.git
cd tobify
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
- Copy `.env.example` to `.env`
- Update the following variables:
  ```env
  # Database Configuration
  PGDATABASE=your_database_name
  PGUSER=your_database_user
  PGPASSWORD=your_database_password
  PGHOST=your_database_host
  PGPORT=your_database_port

  # Email Configuration
  SMTP_SERVER=smtp.gmail.com
  SMTP_PORT=465
  SENDER_EMAIL=your_email@gmail.com
  SENDER_PASSWORD=your_app_password
  ```

5. Setup the database:
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## 📁 Project Structure

```
tobify/
├── 🔐 auth_app/         # Authentication application
│   ├── views.py         # Authentication views
│   └── utils.py         # Email utilities
├── 📝 notes_app/        # Notes management application
│   └── views.py         # Notes CRUD operations
├── 📊 get_attendence/   # Attendance tracking application
│   └── views.py         # Attendance management
└── ⚙️ tobify/           # Project configuration
    ├── settings.py      # Project settings
    └── urls.py          # URL routing
```

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/verify-email/` - Email verification

### Notes
- `GET /api/notes/` - List all notes
- `POST /api/notes/` - Create new note
- `PUT /api/notes/<id>/` - Update note
- `DELETE /api/notes/<id>/` - Delete note
- `PATCH /api/notes/<id>/visibility/` - Toggle note visibility

### Attendance
- `GET /api/attendance/` - View attendance records
- `POST /api/attendance/` - Mark attendance
- `GET /api/attendance/report/` - Generate attendance report

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

For support:
- 📧 Email: support@tobify.com
- 🐛 Open an issue in the GitHub repository
- 🌐 Visit our [live demo](https://5qd-resolute-tesla.circumeo-apps.net/)
