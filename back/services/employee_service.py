from repos.employee_repo import EmployeeRepo, EmployeeRepoLocal, Employee
from exceptions_errors import NonexistentItemError


class EmployeeService:
    def __init__(self, repo: EmployeeRepo):
        self.repo = repo

    def create_employee(self, new_employee: Employee):
        return self.repo.create_employee(new_employee)

    def get_employee(self, employee_id):
        try:
            return self.repo.get_employee(employee_id)
        except NonexistentItemError as n:
            return n.message

    def get_all_employees(self):
        return self.repo.get_all_employees()

    def update_employee(self, updated_employee: Employee):
        return self.repo.update_employee(updated_employee)

    def delete_employee(self, employee_id):
        self.repo.delete_employee(employee_id)


class EmployeeServiceLocal:
    def __init__(self, repo: EmployeeRepoLocal):
        self.repo = EmployeeRepoLocal()

    def create_employee(self, new_employee: Employee):
        return self.repo.create_employee(new_employee)

    def get_employee(self, employee_id):
        try:
            return self.repo.get_employee(employee_id)
        except NonexistentItemError as n:
            return n.message

    def update_employee(self, updated_employee: Employee):
        return self.repo.update_employee(updated_employee)

    def delete_employee(self, employee_id):
        self.repo.delete_employee(employee_id)


if __name__ == '__main__':
    er = EmployeeRepoLocal()
    es = EmployeeServiceLocal(er)

    emp1 = es.get_employee(2)
    print(emp1)
    nu = Employee(4, 'Robert Simms', '152-695-5167', 'Charlotte, NC 09753', 'icaanora@sample.net')
    print(nu)
    print('---new employee data incoming---')
    print(es.create_employee(nu))
    nu = Employee(4, 'Prada Proche III', '322-159-4823', 'Hershey, PA 60235', 'chocolate@hersheypark.com')
    print('---updates in progress here---')
    print(es.update_employee(nu))
    es.delete_employee(nu.id)
    print('---Employee was deleted---')
    emp2 = es.get_employee(nu.id)
    print(emp2)
