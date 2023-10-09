from flask import Flask
from app.router.router import init_app_routes

app = Flask(__name__)

init_app_routes(app)

if __name__ == '__main__':
  app.run()
