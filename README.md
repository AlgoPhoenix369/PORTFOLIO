# Portfolio Website - Babajide Salami

A modern, responsive portfolio website built with React, Tailwind CSS, Bootstrap, and Lucide React for the frontend, and Flask with PostgreSQL/Supabase for the backend.

## 🚀 Features

- **Modern UI/UX**: Clean, professional design with smooth animations
- **Responsive**: Works seamlessly on all devices
- **Dark Mode**: Toggle between light and dark themes
- **Backend API**: RESTful API built with Flask
- **Database**: PostgreSQL with Supabase integration
- **Type Validation**: Marshmallow schemas for data validation
- **Testing**: Comprehensive test suite for both frontend and backend
- **Production Ready**: Docker support, CI/CD pipeline, deployment configurations

## 📁 Project Structure

```
PORTFOLIO/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── lib/             # Utilities (API, Supabase client)
│   │   ├── tests/           # Frontend tests
│   │   ├── App.jsx          # Main App component
│   │   ├── main.jsx         # Entry point
│   │   └── index.css        # Global styles
│   ├── public/              # Static assets
│   ├── package.json         # Frontend dependencies
│   ├── vite.config.js       # Vite configuration
│   ├── tailwind.config.js   # Tailwind configuration
│   ├── vitest.config.js     # Vitest configuration
│   └── Dockerfile           # Docker configuration
│
├── backend/                  # Flask backend API
│   ├── resources/           # API resources (endpoints)
│   ├── models.py            # Database models
│   ├── schemas.py           # Marshmallow schemas
│   ├── app.py               # Flask application
│   ├── config.py            # Configuration classes
│   ├── supabase_client.py   # Supabase integration
│   ├── database_schema.sql  # Database schema
│   ├── requirements.txt     # Python dependencies
│   ├── tests/               # Backend tests
│   └── Dockerfile           # Docker configuration
│
├── docker-compose.yml        # Docker Compose configuration
└── README.md                 # This file
```

## 🛠️ Tech Stack

### Frontend
- **React 19** - UI library
- **Vite** - Build tool
- **Tailwind CSS 4** - Utility-first CSS
- **Bootstrap 5** - Component library
- **Lucide React** - Icon library
- **React Router** - Routing
- **Axios** - HTTP client
- **React Hook Form** - Form handling
- **Supabase JS** - Supabase client
- **Vitest** - Testing framework
- **Testing Library** - React testing utilities

### Backend
- **Flask 3** - Web framework
- **Flask-RESTful** - REST API extension
- **Flask-Marshmallow** - Serialization
- **SQLAlchemy** - ORM
- **Psycopg2** - PostgreSQL adapter
- **Marshmallow** - Data validation
- **Supabase Python** - Supabase client
- **Pytest** - Testing framework
- **Gunicorn** - WSGI server

## 📋 Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.11 or higher)
- **PostgreSQL** (v15 or higher) OR **Supabase** account
- **Docker** (optional, for containerized deployment)

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd PORTFOLIO
```

### 2. Backend Setup

#### Option A: Local Development

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Edit .env with your credentials
# - DATABASE_URL
# - SUPABASE_URL
# - SUPABASE_KEY
# - SECRET_KEY

# Initialize database
psql -U postgres -c "CREATE DATABASE portfolio_db;"
psql -U postgres -d portfolio_db -f database_schema.sql

# Run the application
python app.py
```

#### Option B: Using Docker

```bash
# From the root directory
docker-compose up --build
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment file
cp .env.example .env

# Edit .env with your configuration
# - VITE_SUPABASE_URL
# - VITE_SUPABASE_ANON_KEY
# - VITE_API_URL

# Run development server
npm run dev
```

### 4. Supabase Setup (Optional)

If using Supabase instead of local PostgreSQL:

1. Create a new project at [supabase.com](https://supabase.com)
2. Go to SQL Editor and run the contents of `backend/database_schema.sql`
3. Get your project URL and anon key from Settings > API
4. Update environment files with your Supabase credentials

## 🧪 Running Tests

### Backend Tests

```bash
cd backend

# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_profile.py
```

### Frontend Tests

```bash
cd frontend

# Run tests
npm test

# Run tests with UI
npm run test:ui

# Run tests with coverage
npm run test:coverage
```

## 🚀 Production Deployment

### Using Docker Compose

```bash
# Build and run all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Backend (Standalone)

```bash
cd backend

# Install production dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_ENV=production
export SECRET_KEY=<your-secret-key>
export DATABASE_URL=<your-database-url>

# Run with Gunicorn
gunicorn --config gunicorn.conf.py app:app
```

### Frontend (Standalone)

```bash
cd frontend

# Build for production
npm run build

# Serve with any static file server
# Example with serve:
npm install -g serve
serve -s dist -l 80
```

## 📡 API Endpoints

### Profile
- `GET /api/profiles` - Get all profiles
- `POST /api/profiles` - Create profile
- `GET /api/profile` - Get main profile
- `GET /api/profile/<id>` - Get profile by ID
- `PUT /api/profile/<id>` - Update profile
- `DELETE /api/profile/<id>` - Delete profile

### Experience
- `GET /api/experiences` - Get all experiences
- `POST /api/experiences` - Create experience
- `GET /api/experience/<id>` - Get experience by ID
- `PUT /api/experience/<id>` - Update experience
- `DELETE /api/experience/<id>` - Delete experience

### Education
- `GET /api/educations` - Get all educations
- `POST /api/educations` - Create education
- `GET /api/education/<id>` - Get education by ID
- `PUT /api/education/<id>` - Update education
- `DELETE /api/education/<id>` - Delete education

### Skills
- `GET /api/skills` - Get all skills
- `GET /api/skills?category=<category>` - Get skills by category
- `POST /api/skills` - Create skill
- `GET /api/skill/<id>` - Get skill by ID
- `PUT /api/skill/<id>` - Update skill
- `DELETE /api/skill/<id>` - Delete skill

### Projects
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Create project
- `GET /api/project/<id>` - Get project by ID
- `PUT /api/project/<id>` - Update project
- `DELETE /api/project/<id>` - Delete project

### Certifications
- `GET /api/certifications` - Get all certifications
- `POST /api/certifications` - Create certification
- `GET /api/certification/<id>` - Get certification by ID
- `PUT /api/certification/<id>` - Update certification
- `DELETE /api/certification/<id>` - Delete certification

### Awards
- `GET /api/awards` - Get all awards
- `POST /api/awards` - Create award
- `GET /api/award/<id>` - Get award by ID
- `PUT /api/award/<id>` - Update award
- `DELETE /api/award/<id>` - Delete award

### Contact
- `GET /api/contact` - Get all contact messages (admin)
- `POST /api/contact` - Submit contact message

### Health Check
- `GET /api/health` - API health status

## 🌐 Environment Variables

### Backend (.env)

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Frontend (.env)

```env
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
VITE_API_URL=http://localhost:5000/api
```

## 📝 Customization

### Updating Personal Information

1. **Via API** (Recommended):
   - Start the backend server
   - Use Postman or curl to POST to `/api/profiles`
   - Or use the admin interface

2. **Via Database**:
   - Connect to your PostgreSQL database
   - Run UPDATE queries on the respective tables
   - Or import the sample data from `database_schema.sql`

3. **Directly in Components**:
   - Edit the component files in `frontend/src/components/`
   - Update the hardcoded data

### Styling

- **Tailwind**: Edit `tailwind.config.js` for custom colors, fonts, etc.
- **Custom CSS**: Edit `frontend/src/index.css`
- **Bootstrap**: Override Bootstrap classes in your components

## 🔒 Security Considerations

- Change default SECRET_KEY in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting for API endpoints
- Add authentication for admin endpoints
- Regular dependency updates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Babajide Salami**
- Email: babajide.salami@email.com
- GitHub: [@PhoenixAlgo369](https://github.com/PhoenixAlgo369)
- LinkedIn: [babajide-salami](https://linkedin.com/in/babajide-salami-)
- Location: Croydon, England, United Kingdom

## 🙏 Acknowledgments

- Design inspiration from modern portfolio websites
- Icons by [Lucide React](https://lucide.dev/)
- UI components by [React Bootstrap](https://react-bootstrap.github.io/)
- Styling by [Tailwind CSS](https://tailwindcss.com/)

---

Made with ❤️ using React, Flask, and Tailwind CSS
