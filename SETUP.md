# Environment Setup Instructions

## Configuration Files

This project uses environment variables for sensitive configuration data to keep secrets safe.

### Setting up config.py

1. Copy the template configuration file:
   ```bash
   cp config.py.template config.py
   ```

2. Edit `config.py` and replace the placeholder values:
   - `your-secret-key-here` → Generate a secure secret key
   - `your_db_user` → Your database username
   - `your_db_password` → Your database password

### Environment Variables

You can also set these values as environment variables:
- `SECRET_KEY` - Flask secret key for sessions
- `DB_USER` - Database username
- `DB_PASSWORD` - Database password
- `DB_HOST` - Database host (default: localhost)
- `DB_PORT` - Database port (default: 3306)
- `DB_NAME` - Database name (default: hbnb_v1)
- `UNSPLASH_ACCESS_KEY` - Your Unsplash API key for images

### Security Notes

⚠️ **NEVER commit sensitive files:**
- `config.py` (contains actual credentials)
- `instance/` directory (contains database files)
- `.env` files
- Any files with real API keys or passwords

✅ **Safe to commit:**
- `config.py.template` (template with placeholder values)
- This `SETUP.md` file
- Code files without hardcoded secrets
