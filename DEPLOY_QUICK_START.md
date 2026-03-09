# 🚀 DEPLOYMENT QUICK REFERENCE

## 📋 3-Step Deployment

### Step 1️⃣: Supabase (5 min)
```
1. https://supabase.com → New Project
2. SQL Editor → Run backend/database_schema.sql
3. Settings → API → Copy URL and anon key
```

### Step 2️⃣: Railway Backend (3 min)
```
1. https://railway.app → Deploy from GitHub
2. Variables:
   SUPABASE_URL=https://xxx.supabase.co
   SUPABASE_KEY=eyJxxx...
   SECRET_KEY=any-random-key
   CORS_ORIGINS=https://yoursite.netlify.app
3. Settings:
   Build: pip install -r requirements.txt
   Start: gunicorn --config gunicorn.conf.py app:app
4. Copy your Railway URL
```

### Step 3️⃣: Netlify Frontend (3 min)
```
1. cd frontend
2. Create .env.production:
   VITE_SUPABASE_URL=https://xxx.supabase.co
   VITE_SUPABASE_ANON_KEY=eyJxxx...
   VITE_API_URL=https://your-railway-url.app/api
3. netlify deploy --prod
4. Add same env vars in Netlify dashboard
```

---

## ✅ Verification

### Test Backend
```bash
curl https://your-backend.railway.app/api/health
```

### Test Frontend
```
Visit: https://your-site.netlify.app
```

---

## 🔧 Quick Commands

### Local Testing
```bash
# Backend
cd backend && source venv/bin/activate && python run.py

# Frontend
cd frontend && npm run dev
```

### Deploy
```bash
# Frontend
cd frontend && netlify deploy --prod

# Backend (auto-deploys on git push)
git push origin main
```

---

## 📊 Your Stack

| Component | Service | URL |
|-----------|---------|-----|
| Frontend | Netlify | https://xxx.netlify.app |
| Backend | Railway | https://xxx.up.railway.app |
| Database | Supabase | https://xxx.supabase.co |

**Cost: $0-5/month** (all free tiers available)

---

## 🆘 Help

Full guide: `DEPLOYMENT_GUIDE.md`

---

## ✨ Features Deployed

- ✅ Modern Gen Z design
- ✅ Dark/Light mode toggle
- ✅ Animated skill filters
- ✅ Projects with googly eyes
- ✅ Education timeline
- ✅ Contact form
- ✅ Responsive design
- ✅ High contrast modes
- ✅ Supabase database
- ✅ Flask REST API
- ✅ Auto-deployment

**You're ready to deploy! 🎉**
