# Email Setup for Enquiry Form

## Overview
The contact form on the NLIPL website sends enquiries to: **enquiry@namakkallogistics.com**

---

## Environment Variables Required

Add these in your **Render Dashboard** → **Environment** section:

| Variable | Description | Example Value |
|----------|-------------|---------------|
| `MAIL_SERVER` | SMTP server address | `smtp.gmail.com` |
| `MAIL_PORT` | SMTP port (usually 587 for TLS) | `587` |
| `MAIL_USERNAME` | Email address to send from | `noreply@namakkallogistics.com` |
| `MAIL_PASSWORD` | Email password or App Password | `your-app-password` |

---

## Setup Instructions

### Option 1: Using Gmail (Quick Setup)

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable **2-Step Verification**
3. Go to **App passwords** (under 2-Step Verification)
4. Select "Mail" and "Other (Custom name)" → Enter "NLIPL Website"
5. Copy the generated 16-character password
6. Use these settings:
   - `MAIL_SERVER`: `smtp.gmail.com`
   - `MAIL_PORT`: `587`
   - `MAIL_USERNAME`: `your-gmail@gmail.com`
   - `MAIL_PASSWORD`: `xxxx xxxx xxxx xxxx` (the app password)

### Option 2: Using Domain Email (Recommended for Production)

Contact your domain email provider for SMTP settings:

| Provider | SMTP Server | Port |
|----------|-------------|------|
| Hostinger | `smtp.hostinger.com` | `587` |
| GoDaddy | `smtpout.secureserver.net` | `465` |
| Zoho | `smtp.zoho.com` | `587` |
| Namecheap | `mail.privateemail.com` | `587` |

---

## Adding Variables on Render

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Select your **nlipl** web service
3. Click **Environment** in the left sidebar
4. Click **Add Environment Variable**
5. Add each variable:
   - Key: `MAIL_SERVER` → Value: `smtp.gmail.com`
   - Key: `MAIL_PORT` → Value: `587`
   - Key: `MAIL_USERNAME` → Value: `your-email@domain.com`
   - Key: `MAIL_PASSWORD` → Value: `your-password`
6. Click **Save Changes**
7. The service will automatically redeploy

---

## Testing

After setup, test the form:
1. Go to your website's contact section
2. Fill in the form and submit
3. Check enquiry@namakkallogistics.com for the email

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Emails not sending | Check environment variables are set correctly |
| Authentication error | Ensure you're using App Password (not regular password) |
| Connection timeout | Verify MAIL_SERVER and MAIL_PORT are correct |
| Emails going to spam | Add SPF/DKIM records to your domain DNS |

---

## Status

- [ ] Choose email provider (Gmail / Domain email)
- [ ] Generate App Password or get SMTP credentials
- [ ] Add environment variables to Render
- [ ] Test contact form submission
- [ ] Verify emails are received at enquiry@namakkallogistics.com

