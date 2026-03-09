# 🚀 Quick Deploy Guide

## Deploy Your Portfolio in 3 Steps

### Step 1: Set Up Supabase (5 minutes)

1. Go to [supabase.com](https://supabase.com) and create account
2. Create new project:
   - Name: `portfolio-db`
   - Password: (save this!)
   - Region: Choose closest
3. Go to **SQL Editor** → **New Query**
4. Copy entire `backend/database_schema.sql` and run it
5. Go to **Settings** → **API** and copy:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon/public key**: `eyJ...`

### Step 2: Deploy Backend to Railway (3 minutes)

1. Go to [railway.app](https://railway.app) and sign in with GitHub
2. New Project → **Deploy from GitHub repo**
3. Select your `PORTFOLIO` repository
4. Set these variables in Railway:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-anon-key
   SECRET_KEY=any-random-secret-key
   CORS_ORIGINS=https://your-site.netlify.app
   PORT=5000
   ```
5. Railway auto-deploys. Copy your URL: `https://your-backend.up.railway.app`

### Step 3: Deploy Frontend to Netlify (3 minutes)

1. In Netlify dashboard, create `frontend/.env.production`:
   ```
   VITE_SUPABASE_URL=https://your-project.supabase.co
   VITE_SUPABASE_ANON_KEY=your-anon-key
   VITE_API_URL=https://your-backend.up.railway.app/api
   ```
2. Deploy to Netlify:
   ```bash
   cd frontend
   netlify deploy --prod
   ```
3. Or use Netlify UI:
   - Base directory: `frontend`
   - Build command: `npm run build`
   - Publish directory: `frontend/dist`

---

## ✅ Test Your Deployment

1. Visit your Netlify URL
2. Check if data loads from Supabase
3. Test contact form
4. All sections should display your CV data

---

## 📝 Update Your Data

Edit data directly in Supabase:
1. Go to Supabase Dashboard
2. **Table Editor** → Select table
3. Edit/Insert data

---

## 🎉 Done!

Your portfolio is live with:
- ✅ Netlify hosting
- ✅ Railway backend
- ✅ Supabase database
- ✅ Auto-deployment on git push

**Total Cost: $0** (all free tiers)

---

## 🆘 Need Help?

See full documentation in `DEPLOYMENT.md`
