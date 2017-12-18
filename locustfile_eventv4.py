"""
API: http://localhost:9000/api/v4/event

Headers:
    Content-Type: application/json
    timestamp：发起请求时的时间戳
    uuid: 区分请求数

Requset:
    Json format event
    {"eventKey": "enterHome","user":"<RAMDOM_STRING>"}

Response:
    code 204
"""
from locust import HttpLocust, TaskSet, task
import uuid
import time
import json

apiUrl = "/api/v4/event"
request_body = json.dumps({
    "eventKey": "enterHome",
    "os": "ios",
    "user": str(uuid.uuid4())
})


def request_header():
    return {
        "Content-Type": "application/json",
        "timestamp": str(int(time.time())),
        "uuid": str(uuid.uuid4())
    }


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when Locust start before any task is scheduled """
        self.index()

    def index(self):
        self.client.get("/")

    @task(1)
    def eventv4(self):
        headers = request_header()
        response = self.client.request(
            method="POST",
            url=apiUrl,
            data=request_body,
            headers=headers
        )
        if response.status_code == 204:
            print(headers["uuid"] + " request success")


class WebsiteUser(HttpLocust):
    """ The Locust class (as well as HttpLocust since
    it’s a subclass) also allows one to specify minimum
    and maximum wait time—per simulated user—between
    the execution of tasks (min_wait and max_wait)
    as well as other user behaviours. """
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

