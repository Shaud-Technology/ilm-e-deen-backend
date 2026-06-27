# Codebase Map & Context (`claude.md`)

This file provides a concise, high-level map of the Silsila Backend codebase to minimize context-window token usage and help agents/LLMs immediately understand the architecture.

## Tech Stack
- **Framework**: Django & Django Rest Framework (DRF)
- **Database**: SQLite3 (`db.sqlite3` in project root)
- **Virtual Env**: Python environment in `.\venv\` (Windows PowerShell)

---

## Directory Structure & Modules

```
silsila-backend/
├── main.py                  # Entry/sample script
├── manage.py                # Django administrative utility
├── requirements.txt         # Project dependencies
├── config/                  # Configuration module
│   ├── urls.py              # Main URL router
│   ├── wsgi.py / asgi.py    # Deployment entry points
│   └── settings/            # Settings split by environment
│       ├── __init__.py      # Local settings fallback / configuration loader
│       ├── base.py          # Shared base configuration & INSTALLED_APPS
│       ├── local.py         # Local development settings
│       ├── staging.py       # Staging settings
│       └── production.py    # Production settings
│
├── common/                  # Shared core/utility modules
│   ├── authentication/      # Custom authentication (e.g., customauth.py)
│   ├── permissions/         # Custom permissions (e.g., permission.py: HasGroupPermission, IsAdmin, IsCreator)
│   ├── pagination/          # Custom pagination (e.g., custom_pagination.py)
│   ├── exceptions/          # Custom exception classes & handlers
│   ├── constants/           # Common constants (e.g., user_constants.py)
│   └── utils/               # Shared utilities
│
└── apps/                    # Local Django apps
    ├── users/               # Users, Profiles, and Authentication endpoints
    │   ├── urls.py          # Router for users viewsets (basename: login, profile)
    │   ├── views/           # Views split into files (auth.py, profile.py)
    │   ├── serializers/     # Serializers (e.g. login, register, profile)
    │   ├── services/        # Business logic layers
    │   ├── utils/           # Users-specific helpers
    │   └── models.py        # User/group models
    │
    # Placeholder/V1 domain apps (currently boilerplate placeholders):
    ├── stories/             # Story/reels module (boilerplate admin, models, views, tests)
    ├── seasons/             # Story seasons metadata (boilerplate)
    ├── episodes/            # Episode details and streaming references (boilerplate)
    ├── genres/              # Categories and genres (boilerplate)
    └── subscription/        # Subscriptions and billing (boilerplate)
```

---

## Key Configuration & Imports
- **Settings Module**: `config.settings.local` by default (managed in `manage.py`).
- **Installed Apps**: Django defaults + `rest_framework`, `rest_framework.authtoken`, and local app `apps.users`.
- **Common Import Rules**:
  - Keep custom permissions in `common.permissions.permission`.
  - Keep custom authentication in `common.authentication.customauth`.

---

## Standard Run & Dev Commands

- **Run Dev Server**:
  ```powershell
  .\venv\Scripts\python.exe manage.py runserver
  ```
- **System Integrity Check**:
  ```powershell
  .\venv\Scripts\python.exe manage.py check
  ```
- **Run Tests**:
  ```powershell
  .\venv\Scripts\python.exe manage.py test
  ```
- **Create Migrations**:
  ```powershell
  .\venv\Scripts\python.exe manage.py makemigrations
  ```
- **Apply Migrations**:
  ```powershell
  .\venv\Scripts\python.exe manage.py migrate
  ```
