from exceptions_errors import NonexistentItemError
from repos.request_repo import RequestRepoLocal, RequestRepo, Request


class RequestService:
    def __init__(self, repo: RequestRepo):
        self.repo = repo

    def create_request(self, new_request: Request):
        return self.repo.create_request(new_request)

    def create_event_for_request(self, req, new_event):
        return self.repo.create_event_for_request(req, new_event)

    def get_request(self, request_id):
        try:
            return self.repo.get_request(request_id)
        except NonexistentItemError as n:
            return n.message

    def get_all_requests(self):
        return self.repo.get_all_requests()

    def get_event_from_request(self, request):
        try:
            return self.repo.get_event_from_request(request)
        except NonexistentItemError as n:
            return n.message

    def update_request(self, updated_request: Request):
        return self.repo.update_request(updated_request)

    def delete_request(self, request_id):
        self.repo.delete_request(request_id)


class RequestServiceLocal:
    def __init__(self, repo: RequestRepoLocal):
        self.repo = repo

    def create_request(self, new_request: Request):
        return self.repo.create_request(new_request)

    def get_request(self, request_id):
        try:
            return self.repo.get_request(request_id)
        except NonexistentItemError as n:
            return n.message

    def update_request(self, updated_request):
        return self.repo.update_request(updated_request)

    def delete_request(self, request_id):
        self.repo.delete_request(request_id)


if __name__ == '__main__':
    rr = RequestRepoLocal()
    rs = RequestServiceLocal(rr)

    r1 = rs.get_request(3)
    print(r1)
    nu = Request(4, 10, 711.13, "A+", 2, 900.90)
    print(nu, "---new request form incoming---", sep="\n")
    print(rs.create_request(nu))
    nu = Request(4, 10, 420.69, "B-", 2, 914.14, status="Completed")
    print(rs.update_request(nu))
    rs.delete_request(nu.id)
    print("---Request was deleted---")
    r2 = rs.get_request(nu.id)
    print(r2)
