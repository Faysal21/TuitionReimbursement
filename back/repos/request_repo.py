from classes import Request, Event
from database_conn import conn as connection
from exceptions_errors import NonexistentItemError


def build_request(request_record):
    return Request(id=int(request_record[0]), employee_id=int(request_record[1]),
                   cost=float(request_record[2]), status=request_record[3],
                   grade=request_record[4], amount_reinb=float(request_record[5]),
                   event_id=int(request_record[6]))


def build_event(event_record):
    return Event(id=int(event_record[0]), type=event_record[1], start_date=event_record[2],
                 description=event_record[3], location=event_record[4])


class RequestRepo:
    def __init__(self):
        cursor = connection.cursor()
        cursor.execute("SELECT count(*) FROM requests")
        self.total_requests = cursor.fetchone()[0]

        cursor.execute("SELECT count(*) FROM events")
        self.total_events = cursor.fetchone()[0]

    def create_request(self, new_request: Request):
        cursor = connection.cursor()

        sql_line = "INSERT INTO requests VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING *"
        new_request_details = [new_request.id, new_request.employee_id, new_request.cost,
                               new_request.status, new_request.grade, new_request.amount_reimb,
                               new_request.event_id]

        cursor.execute(sql_line, new_request_details)
        connection.commit()
        request_record = cursor.fetchone()
        self.total_requests += 1
        return build_request(request_record)

    def create_event_for_request(self, req: Request, new_event: Event):
        cursor = connection.cursor()

        sql_line = "INSERT INTO events VALUES(%s, %s, %s, %s, %s) RETURNING *"
        new_event_details = [new_event.id, new_event.type, new_event.start_date,
                             new_event.description, new_event.location]

        cursor.execute(sql_line, new_event_details)
        connection.commit()
        self.total_events += 1

        event_record = cursor.fetchone()
        event = build_event(event_record)

        req.event_id = event.id
        self.update_request(req)
        return event

    def get_all_requests(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * from requests ORDER BY id")

        request_records = cursor.fetchall()
        all_requests = [build_request(request_record) for request_record in request_records]
        return all_requests

    def get_requests_of_employee(self, employee_id):
        cursor = connection.cursor()

        sql_line = "SELECT * from requests WHERE employee_id=%s"
        cursor.execute(sql_line, [employee_id])

        request_records = cursor.fetchall()
        all_requests = [build_request(request_record) for request_record in request_records]
        return all_requests

    def get_request(self, request_id):
        cursor = connection.cursor()

        sql_line = "SELECT * from requests WHERE id=%s"
        cursor.execute(sql_line, [request_id])

        request_record = cursor.fetchone()
        if request_id > self.total_requests:
            error_msg = "Employee with ID no. " + str(request_id) + " does not exist"
            raise NonexistentItemError(error_msg)
        else:
            return build_request(request_record)

    def get_event_from_request(self, request: Request):
        event_id = request.event_id
        if event_id == 0:
            raise NonexistentItemError("No event associated with this request")

        cursor = connection.cursor()

        sql_line = "SELECT * from events WHERE id=%s"
        cursor.execute(sql_line, [event_id])

        event_record = cursor.fetchone()
        return build_event(event_record)

    def update_request(self, updated_request: Request):
        cursor = connection.cursor()
        sql_line = "UPDATE requests SET employee_id=%s, cost=%s, status=%s, grade=%s, amount_reimb=%s, event_id=%s WHERE id=%s RETURNING *"
        updated_request_details = [updated_request.employee_id, updated_request.cost,
                                   updated_request.status, updated_request.grade,
                                   updated_request.amount_reimb, updated_request.event_id,
                                   updated_request.id]

        cursor.execute(sql_line, updated_request_details)
        connection.commit()
        request_record = cursor.fetchone()
        return build_request(request_record)

    def delete_request(self, request_id):
        cursor = connection.cursor()

        sql_line = "DELETE FROM requests WHERE id=%s"
        cursor.execute(sql_line, [request_id])
        connection.commit()
        self.total_requests -= 1


class RequestRepoLocal(RequestRepo):
    def __init__(self):
        self.local_database = []
        self.local_database.append(Request(1, 2, 55.2, "76%", 1, 1000.00))
        self.local_database.append(Request(2, 1, 55.2, "76%", 1, 800.45))
        self.local_database.append(Request(3, 3, 55.2, "76%", 1, 999.20))

        self.total_requests = len(self.local_database)

    def create_request(self, new_request: Request):
        self.local_database.append(new_request)
        self.total_requests += 1
        return self.local_database[new_request.id - 1]

    def get_request(self, request_id):
        request_id = int(request_id)

        if request_id > self.total_requests:
            error_msg = "Request with ID no. " + str(request_id) + " does not exist"
            raise NonexistentItemError(error_msg)
        else:
            return self.local_database[request_id - 1]

    def update_request(self, updated_request: Request):
        self.local_database[updated_request.id - 1] = updated_request
        return self.local_database[updated_request.id - 1]

    def delete_request(self, request_id):
        self.local_database.remove(self.local_database[request_id - 1])
        self.total_requests -= 1


if __name__ == '__main__':
    rr = RequestRepo()
    for request in rr.get_all_requests():
        print(request)
    # print(rr.get_request(6))
    # print("---Adding new requests---")
    # print(rr.create_request(Request(1, 2, 55.2, "76%", 1, 1000.00)))
    # print(rr.create_request(Request(2, 1, 55.2, "76%", 1, 800.45)))
    # print(rr.create_request(Request(3, 3, 55.2, "76%", 1, 999.20)))
    # print(rr.create_request(Request(4, 10, 711.13, "A+", 2, 900.90)))

    # nu = Request(4, 5, 800.81, "84 of 150", 3, 901.01)
    # print(nu, "---Updating request---", sep="\n")
    # print(rr.update_request(nu))

    # print(rr.get_request(4))
    # rr.delete_request(4)
    # print('---Request was deleted---')
    # rr.get_request(4)
