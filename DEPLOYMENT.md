# Deployment Guide

## Deploy to Netlify (Frontend) + Supabase (Database) + Railway/Render (Backend)

---

## 📋 Prerequisites

1. **GitHub Account** - Your code repository
2. **Supabase Account** - Database (free tier available)
3. **Netlify Account** - Frontend hosting (free tier available)
4. **Railway/Render Account** - Backend hosting (free tier available)

---

## 🗄️ Step 1: Set Up Supabase Database

### 1.1 Create Supabase Project
1. Go to [supabase.com](https://supabase.com)
2. Sign up/Login
3. Click "New Project"
4. Fill in:
   - **Name**: portfolio-db
   - **Database Password**: (save this securely)
   - **Region**: Choose closest to you
5. Click "Create new project"

### 1.2 Create Database Tables
1. In your Supabase dashboard, go to **SQL Editor**
2. Click "New Query"
3. Copy and paste the entire contents of `backend/database_schema.sql`
4. Click "Run" to execute

### 1.3 Get API Credentials
1. Go to **Settings** → **API**
2. Copy these values:
   - **Project URL** (e.g., `https://xxxxx.supabase.co`)
   - **anon/public key** (long string starting with `eyJ...`)

### 1.4 Insert Sample Data (Optional)
Run the INSERT statements from `backend/database_schema.sql` to populate initial data.

---

## 🚀 Step 2: Deploy Backend to Railway/Render

### Option A: Railway (Recommended)

#### 2.1 Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub

#### 2.2 Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your `PORTFOLIO` repository

#### 2.3 Configure Backend
1. In Railway dashboard, click on your project
2. Go to **Variables** tab
3. Add these environment variables:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-anon-key
   SECRET_KEY=your-secret-key-here
   CORS_ORIGINS=http://localhost:3000,http://localhost:5173,https://your-site.netlify.app
   PORT=5000
   ```

#### 2.4 Set Build & Start Commands
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --config gunicorn.conf.py app:app`

#### 2.5 Deploy
1. Railway will automatically deploy
2. Copy your public URL (e.g., `https://portfolio-backend-production.up.railway.app`)

### Option B: Render

1. Go to [render.com](https://render.com)
2. Create new "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --config gunicorn.conf.py app:app`
5. Add environment variables (same as Railway)
6. Deploy

---

## 🎨 Step 3: Deploy Frontend to Netlify

### 3.1 Prepare Frontend

#### Update Environment Variables
Create `frontend/.env.production`:
```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_API_URL=https://your-backend-url.railway.app/api
```

### 3.2 Deploy to Netlify

#### Method 1: Netlify CLI (Recommended)

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login to Netlify
netlify login

# Navigate to frontend
cd frontend

# Initialize Netlify
netlify init

# Choose:
# - Create & configure a new site
# - Select your team
# - Site name: your-portfolio

# Deploy
netlify deploy --prod
```

#### Method 2: Netlify UI

1. Go to [netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect with GitHub
4. Choose your repository
5. Configure build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`
6. Click "Deploy site"

### 3.3 Add Environment Variables in Netlify

1. In Netlify dashboard, go to **Site settings** → **Environment variables**
2. Add:
   ```
   VITE_SUPABASE_URL=https://your-project.supabase.co
   VITE_SUPABASE_ANON_KEY=your-anon-key
   VITE_API_URL=https://your-backend-url.railway.app/api
   ```

### 3.4 Update CORS in Backend

Add your Netlify URL to backend CORS:
```
CORS_ORIGINS=https://your-site.netlify.app,https://your-custom-domain.com
```

---

## 🔗 Step 4: Connect Everything

### Update Backend URL in Frontend

In Netlify environment variables, update `VITE_API_URL` with your Railway/Render backend URL.

### Test the Deployment

1. Visit your Netlify URL: `https://your-site.netlify.app`
2. Check if data loads from Supabase
3. Test contact form
4. Verify all sections display correctly

---

## 📊 Step 5: Manage Data in Supabase

### View/Edit Data

1. Go to Supabase Dashboard
2. **Table Editor** → Select table → Edit data directly

### Enable Row Level Security (RLS)

The schema already includes RLS policies. To verify:

1. Go to **Authentication** → **Policies**
2. Ensure policies are enabled for all tables

### Backup Data

1. Go to **Database** → **Backups**
2. Enable automatic backups
3. Download manual backups as needed

---

## 🔒 Security Best Practices

### 1. Environment Variables
- Never commit `.env` files
- Use Netlify/Railway environment variables
- Rotate keys periodically

### 2. Supabase Security
- Enable RLS on all tables
- Use anon key only (never service key in frontend)
- Set up proper policies

### 3. CORS
- Only allow your production domains
- Update CORS when deploying to new domains

---

## 📈 Monitoring & Analytics

### Netlify Analytics
- Enable in Netlify dashboard ($9/month)
- Or use Google Analytics (free)

### Railway Monitoring
- Built-in metrics in Railway dashboard
- View logs, CPU, memory usage

### Supabase Logs
- Go to **Database** → **Logs**
- Monitor queries and errors

---

## 🔄 Continuous Deployment

### Automatic Deploys

- **Netlify**: Auto-deploys on push to main branch
- **Railway**: Auto-deploys on push to main branch
- **Render**: Auto-deploys on push to main branch

### Manual Trigger
```bash
# Deploy to Netlify
cd frontend
netlify deploy --prod

# Railway auto-deploys on git push
git push origin main
```

---

## 🐛 Troubleshooting

### Frontend Issues

**Problem**: Data not loading
- Check browser console for errors
- Verify `VITE_API_URL` is correct
- Check CORS settings in backend

**Problem**: Build fails
- Clear cache: `netlify deploy --prod --clear`
- Check Node version (use `.nvmrc`)

### Backend Issues

**Problem**: Can't connect to Supabase
- Verify `SUPABASE_URL` and `SUPABASE_KEY`
- Check Supabase project is active
- Test connection locally first

**Problem**: CORS errors
- Add frontend domain to `CORS_ORIGINS`
- Restart backend after env var changes

### Database Issues

**Problem**: Tables not found
- Run `database_schema.sql` in Supabase SQL Editor
- Check table names match queries

---

## 💰 Cost Breakdown

| Service | Plan | Cost |
|---------|------|------|
| Netlify | Free | $0/mo |
| Railway | Hobby | $5/mo (or free with limits) |
| Supabase | Free | $0/mo |
| **Total** | | **$0-5/mo** |

---

## ✅ Deployment Checklist

- [ ] Supabase project created
- [ ] Database tables created
- [ ] Sample data inserted
- [ ] Backend deployed to Railway/Render
- [ ] Backend environment variables set
- [ ] Frontend deployed to Netlify
- [ ] Frontend environment variables set
- [ ] CORS configured correctly
- [ ] Contact form tested
- [ ] All sections load correctly
- [ ] Mobile responsive tested
- [ ] Custom domain configured (optional)

---

## 🎉 You're Done!

Your portfolio is now live with:
- ✅ Netlify hosting (frontend)
- ✅ Railway/Render hosting (backend)
- ✅ Supabase database
- ✅ Automatic deployments
- ✅ Production-ready setup

**Share your portfolio URL with the world!** 🚀
