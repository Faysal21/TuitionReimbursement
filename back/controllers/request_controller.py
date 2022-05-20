import sys

from flask import request, jsonify
from werkzeug.exceptions import abort
from repos.request_repo import RequestRepo
from services.request_service import RequestService
from classes import Request, Event

repo = RequestRepo()
service = RequestService(repo)


def route(app):
    @app.route("/requests", methods=['POST'])
    def create_request():
        body = request.json

        if not 'event_id' in body:
            req = Request(1 + repo.total_requests, body['employee_id'], body['cost'],
                          body['grade'], 0, body['amount_reimb'], body['status'])
        else:
            req = Request(1 + repo.total_requests, body['employee_id'], body['cost'],
                          body['grade'], body['event_id'], body['amount_reimb'], body['status'])

        req = service.create_request(req)
        return req.to_json()

    @app.route("/requests/<request_id>/event", methods=['POST'])
    def create_event_for_request(request_id):
        request_id = int(request_id)
        req = service.get_request(request_id)

        body = request.json

        ev = Event(1 + repo.total_events, body['type'], body['start_date'],
                   body['description'], body['location'])

        ev = service.create_event_for_request(req, ev)
        return ev.to_json()

    @app.route("/requests/<request_id>", methods=['GET'])
    def get_request(request_id):
        request_id = int(request_id)
        req = service.get_request(request_id)

        if isinstance(req, str):
            return req, 404
        else:
            return req.to_json(), 200

    @app.route("/requests/<request_id>/event", methods=['GET'])
    def get_event_from_request(request_id):
        request_id = int(request_id)
        req = service.get_request(request_id)

        if isinstance(req, str):
            return req, 404

        ev = service.get_event_from_request(req)
        if isinstance(ev, str):
            return ev, 404
        else:
            return ev.to_json()

    @app.route("/requests", methods=['GET'])
    def get_all_requests():
        all_requests = service.get_all_requests()
        return jsonify([a_request.to_json() for a_request in all_requests])

    @app.route("/requests/<request_id>", methods=['PUT'])
    def update_request(request_id):
        request_id = int(request_id)
        req = service.get_request(request_id)

        if isinstance(req, str):
            return req, 404
        else:
            body = request.json

            req = Request(request_id, body['employee_id'], body['cost'],
                          body['grade'], body['event_id'], body['amount_reimb'], body['status'])
            req = service.update_request(req)
            return req.to_json(), 200

    @app.route("/requests/<request_id>", methods=['DELETE'])
    def delete_request(request_id):
        request_id = int(request_id)
        req = service.get_request(request_id)

        if isinstance(req, str):
            return req, 404
        else:
            service.delete_request(request_id)
            return "Request deleted from database"
