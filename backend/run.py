import os
import warnings

# Suppress the google.generativeai deprecation FutureWarning in production logs
warnings.filterwarnings('ignore', category=FutureWarning, module='google.generativeai')

from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'

    if debug:
        print(f"🔧 Bachat AI Backend starting in DEVELOPMENT mode on port {port}...")
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        print(f"🚀 Bachat AI Backend starting in PRODUCTION mode on port {port}...")
        try:
            from waitress import serve
            serve(app, host='0.0.0.0', port=port, threads=4)
        except ImportError:
            print("⚠️  waitress not installed — falling back to Flask dev server.")
            print("   Install it with: pip install waitress")
            app.run(host='0.0.0.0', port=port, debug=False)
