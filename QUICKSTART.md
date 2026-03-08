# Quick Start Guide

Get your portfolio up and running in minutes!

## 🚀 Quick Setup (5 minutes)

### Option 1: Docker (Easiest)

```bash
# Clone and enter directory
cd PORTFOLIO

# Start all services
docker-compose up --build

# Visit http://localhost for frontend
# Visit http://localhost:5000/api/health for backend API
```

### Option 2: Manual Setup

#### Backend (Terminal 1)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set minimal environment
export FLASK_APP=app.py
export SECRET_KEY=dev-key
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/portfolio_db

# Create database (if PostgreSQL is installed)
createdb portfolio_db
psql -d portfolio_db -f database_schema.sql

# Run backend
flask run --port 5000
```

#### Frontend (Terminal 2)
```bash
cd frontend
npm install
npm run dev

# Visit http://localhost:5173
```

## 📝 First Steps After Setup

### 1. Update Your Information

The database comes pre-populated with Babajide Salami's information from the CV. To update:

**Option A: Via API**
```bash
# Update profile
curl -X PUT http://localhost:5000/api/profile/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Your Name", "title": "Your Title"}'
```

**Option B: Direct Database Edit**
```sql
-- Connect to database
psql -d portfolio_db

-- Update profile
UPDATE profiles SET 
  name = 'Your Name',
  title = 'Your Title',
  email = 'your.email@example.com'
WHERE id = 1;
```

### 2. Configure Supabase (Optional)

For cloud database:

1. Go to [supabase.com](https://supabase.com) and create account
2. Create new project
3. Go to SQL Editor, paste contents of `backend/database_schema.sql`
4. Get credentials from Settings > API
5. Update `.env` files:

**Backend .env:**
```env
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your-anon-key
```

**Frontend .env:**
```env
VITE_SUPABASE_URL=https://xxxxx.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

### 3. Add Your Projects

```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Awesome Project",
    "description": "Project description",
    "technologies": ["React", "Python"],
    "duration": "3 months",
    "role": "Lead Developer"
  }'
```

## 🧪 Run Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## 📦 Build for Production

```bash
# Frontend
cd frontend
npm run build

# Backend uses Gunicorn automatically with docker-compose
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Kill process on port 3000/5173
lsof -ti:3000 | xargs kill -9
```

### Database Connection Error
```bash
# Check PostgreSQL is running
pg_isready

# Restart PostgreSQL (macOS with Homebrew)
brew services restart postgresql@15
```

### Node Modules Issues
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Python Dependencies Issues
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 📚 Next Steps

1. ✅ Review and update all personal information
2. ✅ Add your real projects and experience
3. ✅ Update social media links
4. ✅ Configure production deployment
5. ✅ Set up custom domain (optional)
6. ✅ Enable HTTPS
7. ✅ Set up monitoring and logging

## 🆘 Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Review error logs in terminal
- Check database connection
- Verify environment variables are set correctly

---

Happy building! 🚀
