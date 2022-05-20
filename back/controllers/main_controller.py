from controllers import employee_controller, request_controller


def route(app):
    employee_controller.route(app)
    request_controller.route(app)
