import sys

from flask import request, jsonify
from werkzeug.exceptions import abort
from repos.employee_repo import EmployeeRepo
from services.employee_service import EmployeeService
from classes import Employee

repo = EmployeeRepo()
service = EmployeeService(repo)


def route(app):
    @app.route("/employees", methods=['POST'])
    def create_employee():
        body = request.json

        emp = Employee(1 + repo.total_employees, body['name'],
                       body['phone'], body['address'], body['email'])
        emp = service.create_employee(emp)
        return emp.to_json()

    @app.route("/employees/<employee_id>", methods=['GET'])
    def get_employee(employee_id):
        employee_id = int(employee_id)
        emp = service.get_employee(employee_id)

        if isinstance(emp, str):
            return emp, 404
        else:
            return emp.to_json(), 200

    @app.route("/employees", methods=['GET'])
    def get_all_employees():
        all_employees = service.get_all_employees()
        return jsonify([an_employee.to_json() for an_employee in all_employees])

    @app.route("/employees/<employee_id>", methods=['PUT'])
    def update_employee(employee_id):
        employee_id = int(employee_id)
        emp = service.get_employee(employee_id)

        if isinstance(emp, str):
            return emp, 404
        else:
            body = request.json
            emp = Employee(employee_id, body['name'],
                           body['phone'], body['address'], body['email'])
            emp = service.update_employee(emp)
            return emp.to_json(), 200

    @app.route("/employees/<employee_id>", methods=['DELETE'])
    def delete_employee(employee_id):
        employee_id = int(employee_id)
        emp = service.get_employee(employee_id)

        if isinstance(emp, str):
            return emp, 404
        else:
            service.delete_employee(employee_id)
            return "Employee deleted from database"
