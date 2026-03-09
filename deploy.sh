# Quick Deploy Script
# Run this to prepare for deployment

#!/bin/bash

echo "🚀 Portfolio Deployment Preparation"
echo "===================================="
echo ""

# Check if in portfolio directory
if [ ! -f "frontend/package.json" ]; then
    echo "❌ Please run this script from the PORTFOLIO root directory"
    exit 1
fi

echo "✅ In correct directory"
echo ""

# Check frontend
echo "📦 Checking Frontend..."
if [ -f "frontend/package.json" ] && [ -f "frontend/netlify.toml" ]; then
    echo "✅ Frontend files present"
else
    echo "❌ Missing frontend files"
    exit 1
fi

# Check backend
echo "📦 Checking Backend..."
if [ -f "backend/requirements.txt" ] && [ -f "backend/app.py" ] && [ -f "backend/database_schema.sql" ]; then
    echo "✅ Backend files present"
else
    echo "❌ Missing backend files"
    exit 1
fi

echo ""
echo "✅ All required files present!"
echo ""

# Install dependencies
echo "📥 Installing Frontend Dependencies..."
cd frontend
npm install
cd ..

echo "📥 Installing Backend Dependencies..."
cd backend
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ..

echo ""
echo "✅ Dependencies installed!"
echo ""

# Show next steps
echo "===================================="
echo "📋 NEXT STEPS:"
echo "===================================="
echo ""
echo "1. Set up Supabase:"
echo "   - Go to https://supabase.com"
echo "   - Create new project"
echo "   - Run backend/database_schema.sql in SQL Editor"
echo "   - Copy Project URL and anon key"
echo ""
echo "2. Deploy Backend to Railway:"
echo "   - Go to https://railway.app"
echo "   - Deploy from GitHub"
echo "   - Add environment variables:"
echo "     SUPABASE_URL=your_url"
echo "     SUPABASE_KEY=your_key"
echo "     SECRET_KEY=any_random_key"
echo "     CORS_ORIGINS=https://your-site.netlify.app"
echo ""
echo "3. Deploy Frontend to Netlify:"
echo "   - cd frontend"
echo "   - netlify deploy --prod"
echo "   - Add environment variables in Netlify dashboard"
echo ""
echo "📖 Full guide: DEPLOYMENT_GUIDE.md"
echo ""
echo "Good luck! 🎉"
