# Supabase Setup Guide ✅

Your Supabase project has been configured! Follow these steps to complete the setup.

## Your Supabase Credentials

- **Project URL**: `https://ltpjidftzlhqsidfjevt.supabase.co`
- **Publishable Key**: `sb_publishable_mfpOqiC2GTpOBHa16n6qvA_6HujPVpZ`
- **Database Password**: `zYd*6b5WMG?EB_x`

---

## Step 1: Initialize Database Tables

1. Go to your Supabase dashboard: https://supabase.com/dashboard/project/ltpjidftzlhqsidfjevt
2. Click on **SQL Editor** in the left sidebar
3. Click **New query**
4. Copy the entire contents of `backend/database_schema.sql`
5. Paste it into the SQL editor
6. Click **Run** (or press Ctrl+Enter)

This will create:
- ✅ 8 database tables (profiles, experiences, educations, skills, projects, certifications, awards, contact_messages)
- ✅ Sample data from your CV
- ✅ Row Level Security (RLS) policies
- ✅ Indexes for performance

---

## Step 2: Configure Netlify Environment Variables

1. Go to your Netlify dashboard
2. Select your portfolio site
3. Go to **Site settings** → **Environment variables**
4. Add these variables:

| Variable Name | Value |
|--------------|-------|
| `VITE_SUPABASE_URL` | `https://ltpjidftzlhqsidfjevt.supabase.co` |
| `VITE_SUPABASE_ANON_KEY` | `sb_publishable_mfpOqiC2GTpOBHa16n6qvA_6HujPVpZ` |

5. Click **Save** for each variable
6. **Redeploy** your site (Site settings → Deploys → Trigger deploy → Clear cache and deploy site)

---

## Step 3: Verify Connection

After redeploying:

1. Open your live site
2. Open browser DevTools (F12)
3. Go to the **Console** tab
4. Check for any errors related to Supabase
5. Your portfolio data should load automatically

---

## Step 4: (Optional) Update Your Data

You can update your portfolio data in two ways:

### Option A: Via Supabase Dashboard

1. Go to **Table Editor** in Supabase
2. Select any table (e.g., `profiles`, `experiences`, `skills`)
3. Edit data directly in the UI
4. Changes will appear on your site immediately

### Option B: Via API

Your backend API endpoints are ready:
- `GET /api/profiles` - Get all profiles
- `POST /api/profiles` - Create profile
- `GET /api/experiences` - Get all experiences
- `GET /api/skills` - Get all skills
- etc.

---

## Security Notes

✅ **Safe to use in frontend:**
- `VITE_SUPABASE_URL` - Public project URL
- `VITE_SUPABASE_ANON_KEY` - Publishable key (designed for client-side use)

❌ **NEVER expose:**
- `service_role` key - This bypasses RLS and should only be used server-side
- Database password - Keep this secure

---

## Troubleshooting

### Data not loading?

1. Check browser console for errors
2. Verify database tables exist in Supabase Table Editor
3. Check RLS policies are enabled
4. Ensure environment variables are set in Netlify

### CORS errors?

1. Go to Supabase Dashboard → Settings → API
2. Ensure your site URL is allowed (Netlify handles this automatically)

### Permission denied errors?

1. Go to Supabase Dashboard → Authentication → Policies
2. Verify RLS policies allow public read access
3. The schema includes these policies by default

---

## Next Steps

1. ✅ Initialize database (Step 1)
2. ✅ Set Netlify environment variables (Step 2)
3. ✅ Redeploy site
4. ✅ Verify everything works
5. 🎉 Your portfolio is live!

---

**Questions?** Check the main [README.md](./README.md) for more details.
