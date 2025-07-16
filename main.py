import os
from app import app

if __name__ == '__main__':
    # For local development
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'development') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
else:
    # For production deployment (Render, Heroku, etc.)
    # Gunicorn will handle the app object directly
    pass
