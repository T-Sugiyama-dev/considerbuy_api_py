from app.controller.calc_controller import calc_controller

def init_app_routes(app):
  app.register_blueprint(calc_controller, url_prefix='/api/v1')