from flask import Flask, send_from_directory
from app.routes import api


def create_app():
    app = Flask(__name__, static_folder="../static")

    app.register_blueprint(api)

    @app.route("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
