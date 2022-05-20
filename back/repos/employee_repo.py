from classes import Employee
from exceptions_errors import NonexistentItemError
from database_conn import conn as connection


def build_employee(employee_record):
    return Employee(id=int(employee_record[0]), name=employee_record[1],
                    phone=employee_record[2], address=employee_record[3],
                    email=employee_record[4])


class EmployeeRepo:
    def __init__(self):
        cursor = connection.cursor()
        cursor.execute("SELECT count(*) FROM employees")
        self.total_employees = cursor.fetchone()[0]

    def create_employee(self, new_employee: Employee):
        cursor = connection.cursor()

        sql_line = "INSERT INTO employees VALUES(%s, %s, %s, %s, %s) RETURNING *"
        new_employee_details = [new_employee.id, new_employee.name,
                                new_employee.phone, new_employee.address,
                                new_employee.email]

        cursor.execute(sql_line, new_employee_details)
        connection.commit()
        employee_record = cursor.fetchone()
        self.total_employees += 1
        return build_employee(employee_record)

    def get_employee(self, employee_id) -> Employee:
        cursor = connection.cursor()

        sql_line = "SELECT * from employees WHERE id=%s"
        cursor.execute(sql_line, [employee_id])

        employee_record = cursor.fetchone()
        if employee_id > self.total_employees:
            error_msg = "Employee with ID no. " + str(employee_id) + " does not exist"
            raise NonexistentItemError(error_msg)
        else:
            return build_employee(employee_record)

    def get_all_employees(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees ORDER BY id")

        employee_records = cursor.fetchall()
        all_employees = [build_employee(employee_record) for employee_record in employee_records]
        return all_employees


    def update_employee(self, updated_employee: Employee):
        cursor = connection.cursor()

        sql_line = "UPDATE employees SET name=%s, phone=%s, address=%s, email=%s WHERE ID =%s RETURNING *"
        updated_employee_details = [updated_employee.name, updated_employee.phone,
                                    updated_employee.address, updated_employee.email,
                                    updated_employee.id]

        cursor.execute(sql_line, updated_employee_details)
        connection.commit()
        employee_record = cursor.fetchone()
        return build_employee(employee_record)

    def delete_employee(self, employee_id):
        cursor = connection.cursor()

        sql_line = "DELETE FROM employees WHERE id=%s"
        cursor.execute(sql_line, [employee_id])
        connection.commit()
        self.total_employees -= 1


class EmployeeRepoLocal(EmployeeRepo):
    def __init__(self):
        self.local_database = []
        self.local_database.append(
            Employee(1, 'John Elway', '720-316-5280', 'Denver, CO 80230', 'helicopter98@broncos.net'))
        self.local_database.append(
            Employee(2, 'Mike Davis', '804-537-2884', 'Atlanta, GA 62832', 'ihatepatterson@example.com'))
        self.local_database.append(
            Employee(3, 'Frank Hopkins', '410-223-2110', 'Baltimore, MD 21213', 'jh22@example.com'))
        self.total_employees = len(self.local_database)

    def create_employee(self, new_employee: Employee):
        self.local_database.append(new_employee)
        self.total_employees += 1
        return self.local_database[new_employee.id - 1]

    def get_employee(self, employee_id):
        employee_id = int(employee_id)

        if employee_id > self.total_employees:
            error_msg = "Employee with ID no. " + str(employee_id) + " does not exist"
            raise NonexistentItemError(error_msg)
        else:
            return self.local_database[employee_id - 1]

    def update_employee(self, updated_employee: Employee):
        self.local_database[updated_employee.id - 1] = updated_employee
        return self.local_database[updated_employee.id - 1]

    def delete_employee(self, employee_id):
        self.local_database.remove(self.local_database[employee_id - 1])
        self.total_employees -= 1


if __name__ == '__main__':
    er = EmployeeRepo()
    # print(er.create_employee(Employee(3, 'Frank Hopkins', '410-223-2110', 'Baltimore, MD 21213', 'jh22@example.com')))
    # print(er.create_employee(Employee(4, 'Robert Simms', '152-695-5167', 'Charlotte, NC 09753', 'icaanora@sample.net')))
    # nu = Employee(4, 'Robert Simms', '152-695-5167', 'Charlotte, NC 09753', 'icaanora@sample.net')
    # print(nu)
    # print('---new employee data incoming---')
    # print(er.get_employee(3))
    # nu = Employee(3, 'Prada Proche III', '322-159-4823', 'Hershey, PA 60235', 'chocolate@hersheypark.com')
    # print('---updates in progress here---')
    # print(er.update_employee(nu))
    print(er.get_employee(4))
    er.delete_employee(4)
    print('---Employee was deleted---')
    er.get_employee(4)
