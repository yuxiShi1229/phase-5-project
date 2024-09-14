from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Configure CORS
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

    # Register blueprints
    from routes import auth, classroom
    app.register_blueprint(auth.bp)
    app.register_blueprint(classroom.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)  # or any other available port
