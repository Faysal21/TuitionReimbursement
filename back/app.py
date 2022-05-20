from flask import Flask
from flask_cors import CORS
import controllers.main_controller as ctrl

app = Flask(__name__)
CORS(app)

ctrl.route(app)

if __name__ == '__main__':
    app.run()
