# AI Blog - Modern Django Blog Platform

## Features Implemented

### Authentication System
- Custom user model with avatar support
- Signup/Login/Logout functionality
- Profile management with avatar upload
- Password reset via email

### Blog System
- Full CRUD operations for posts
- Rich text editor (CKEditor)
- SEO-friendly slugs (auto-generated)
- Category and tag support
- Comments system
- Like/Bookmark functionality
- Reading time calculation
- Search and filter by category
- Pagination

### AI Integration (OpenCode)
- AI content generation from title/keywords
- Auto summary generation
- Tag suggestions
- Grammar improvement
- Reusable AI service module

### Modern Frontend
- Tailwind CSS for styling
- AOS animations on scroll
- Dark/Light mode toggle
- Responsive design
- Glassmorphism effects
- Hover animations
- Loading skeletons ready

### Custom Dashboard
- Overview with stats (posts, users, categories)
- Posts management table
- Users management table
- Chart.js integration for post trends
- Fully responsive layout

### Extra Features
- Newsletter subscription model
- Bookmarked posts page
- Trending posts (by likes)
- Reading time calculation

## Setup Instructions

1. **Clone/Download** the project to `C:\new\blogwebsite`

2. **Activate virtual environment:**
   ```powershell
   cd C:\new\blogwebsite
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   - Copy `.env.example` to `.env`
   - Add your OpenCode API key to `.env`

5. **Run migrations:**
   ```powershell
   python manage.py migrate
   ```

6. **Create superuser:**
   ```powershell
   python manage.py createsuperuser
   ```

7. **Start server:**
   ```powershell
   python manage.py runserver
   ```

8. **Visit:** http://localhost:8000

## Project Structure

```
ai_blog/
├── ai_blog/           # Project settings
├── users/             # Authentication app
├── posts/             # Blog system app
├── ai_features/       # AI integration app
├── dashboard/         # Custom admin dashboard
├── templates/         # All HTML templates
│   ├── base.html
│   ├── users/
│   ├── posts/
│   ├── ai_features/
│   └── dashboard/
├── static/            # Static files
├── media/             # User uploads
├── .env               # Environment variables
└── requirements.txt   # Dependencies
```

## API Keys

To use AI features, get an API key from OpenCode and add it to `.env`:
```
OPENCODE_API_KEY=your_actual_api_key_here
```

## Default Admin Access

- Username: `admin`
- Password: `admin123`
- Login at: http://localhost:8000/users/login/
- Dashboard: http://localhost:8000/dashboard/

## Technologies Used

- Django 6.0.3
- SQLite (default)
- Tailwind CSS (CDN)
- CKEditor 4 (rich text)
- Chart.js (dashboard charts)
- AOS (animations)
- Django Taggit (tags)
- Django Crispy Forms (forms)
