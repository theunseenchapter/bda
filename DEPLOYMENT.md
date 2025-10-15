# Deployment Guide - Vercel

This guide explains how to deploy your Friend Recommendation System to Vercel.

## Prerequisites

- Git installed on your system
- Vercel account (free tier available at https://vercel.com)
- Your Supabase credentials ready

## Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

Or if you prefer not to install globally, you can use `npx vercel` in the commands below.

## Step 2: Prepare Your Project

The project is already configured with:
- `vercel.json` - Vercel configuration file
- `.vercelignore` - Files to exclude from deployment
- Clean `requirements.txt` - Python dependencies

## Step 3: Initialize Git Repository (if not already done)

```bash
git init
git add .
git commit -m "Initial commit - Friend Recommendation System"
```

## Step 4: Deploy to Vercel

Run the following command in your project directory:

```bash
vercel
```

This will:
1. Ask you to log in to Vercel (follow the prompts)
2. Link your project to Vercel
3. Deploy your application

For production deployment:

```bash
vercel --prod
```

## Step 5: Configure Environment Variables

After deployment, you need to add your Supabase credentials:

### Option A: Via Vercel CLI

```bash
vercel env add SUPABASE_URL
# Enter: https://srncohfedkisalftxmex.supabase.co

vercel env add SUPABASE_KEY
# Paste your Supabase anon key
```

### Option B: Via Vercel Dashboard

1. Go to your project on https://vercel.com/dashboard
2. Click on your project
3. Go to Settings → Environment Variables
4. Add the following variables:
   - `SUPABASE_URL`: `https://srncohfedkisalftxmex.supabase.co`
   - `SUPABASE_KEY`: Your Supabase anon key from .env file

## Step 6: Redeploy with Environment Variables

After setting environment variables, redeploy:

```bash
vercel --prod
```

## Your Application is Live! 🎉

Vercel will provide you with a URL like:
- `https://your-project-name.vercel.app`

## Troubleshooting

### Build Fails
- Check the Vercel build logs in the dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### Database Connection Issues
- Verify environment variables are set correctly
- Check Supabase credentials
- Ensure Supabase RLS policies allow access

### Application Crashes
- Check Vercel Function logs in dashboard
- Verify `app.py` is compatible with serverless environment

## Updating Your Deployment

To update your deployment after making changes:

```bash
git add .
git commit -m "Description of changes"
vercel --prod
```

## Custom Domain (Optional)

To add a custom domain:
1. Go to your project in Vercel dashboard
2. Settings → Domains
3. Add your custom domain
4. Follow DNS configuration instructions

## Notes

- Vercel free tier includes:
  - Unlimited deployments
  - Automatic HTTPS
  - Global CDN
  - 100GB bandwidth per month
  
- Serverless functions have a 10-second execution timeout on free tier
- Database connections are created per request (serverless environment)

## Support

For Vercel-specific issues, visit:
- Vercel Documentation: https://vercel.com/docs
- Vercel Community: https://github.com/vercel/vercel/discussions

For Supabase issues:
- Supabase Documentation: https://supabase.com/docs
- Supabase Community: https://github.com/supabase/supabase/discussions
