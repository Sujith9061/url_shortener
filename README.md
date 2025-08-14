# Django URL Shortener

## Setup & Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Make migrations and migrate:
   ```bash
   python manage.py makemigrations ioss_backend
   python manage.py migrate
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```

## Features
- Shorten URLs with a unique code
- Redirect from short code to original URL
- Track click counts
- Responsive Bootstrap 5 UI
- Session-based table of shortened URLs

## Deployment (Render)
- Procfile and requirements.txt included
- Static files served via Whitenoise
- ALLOWED_HOSTS set for deployment

## Docker
- Build and run with:
   ```bash
   docker-compose up --build
   ```

## Code Quality
- Follows PEP8
- Uses Django path routing
- Clean, reusable functions

## GitHub
- Keep code in a public repository for deployment
