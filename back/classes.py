class Request:
    def __init__(self, id, employee_id, cost, grade,event_id, amount_reinb=0.0, status ='Unknown'):
        self.id = id
        self.employee_id = employee_id
        self.cost = cost
        self.status = status
        self.grade = grade
        self.amount_reimb = amount_reinb
        self.event_id = event_id

    def __repr__(self):
        return str({
            'id': self.id,
            'employee-id': self.employee_id,
            'cost': self.cost,
            'status': self.status,
            'grade': self.grade,
            'amount_reimb': self.amount_reimb,
            'event_id': self.event_id
        })

    def to_json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'cost': self.cost,
            'status': self.status,
            'grade': self.grade,
            'amount_reimb': self.amount_reimb,
            'event_id': self.event_id
        }


class Employee:
    def __init__(self, id, name, phone, address, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def __repr__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'email': self.email
        })

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'email': self.email
        }

class Event:
    def __init__(self, id, type, start_date, description, location):
        self.id = id
        self.type = type
        self.start_date = start_date
        self.description = description
        self.location = location

    def __repr__(self):
        return str({
            'id': self.id,
            'type': self.type,
            'start_date': self.start_date,
            'description': self.description,
            'location': self.location
        })

    def to_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'start_date': self.start_date,
            'description': self.description,
            'location': self.location
        }