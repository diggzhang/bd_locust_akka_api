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
import random


apiUrl = "/api/v4/events"


def request_header():
    return {
        "Content-Type": "application/json",
        "timestamp": str(int(time.time())),
        "uuid": str(uuid.uuid4())
    }


def request_body(user_id, type_is):
    return dict({
        "eventKey": user_id.split('-')[0],
        "timestamp": int(time.time()),
        "user": user_id,
        "type": type_is,
    })


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when Locust start before any task is scheduled """
        self.index()

    def index(self):
        response = self.client.get("/api")
        print(response)

    @task(1)
    def eventv4_single(self):
        headers = request_header()
        data = json.dumps(request_body(headers["uuid"], "single"))
        response = self.client.request(
            method="POST",
            url=apiUrl,
            data=data,
            headers=headers
        )
        if response.status_code == 204:
            print(headers["uuid"] + " request success")

    """
    @task takes an optional weight argument that can be used
    to specify the task’s execution ratio.
    In the following example task2 will be executed
    twice as much as task1:
    """
    @task(2)
    def eventv4_batch(self):
        headers = request_header()
        batch_data = []
        data = request_body(headers["uuid"], "batch")
        batch_data.append(data)
        response = self.client.request(
            method="POST",
            url=apiUrl,
            data=json.dumps(batch_data),
            headers=headers,
        )
        if response.status_code == 204:
            print("BATCH REQUSET SUCCESS: "+ headers["uuid"])


class WebsiteUser(HttpLocust):
    """ The Locust class (as well as HttpLocust since
    it’s a subclass) also allows one to specify minimum
    and maximum wait time—per simulated user—between
    the execution of tasks (min_wait and max_wait)
    as well as other user behaviours. """
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
