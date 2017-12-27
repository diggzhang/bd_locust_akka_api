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
import uuid
import time
import json
import random
from locust import HttpLocust, TaskSet, task


APIURL = "/api/v4/events"

EVENTS_LIST = [
    {
        "u_gender" : "female",
        "u_juniorPhysics" : "16,2",
        "u_tenant" : "-1",
        "noticeName" : "9年级期末课程包-几何最值",
        "u_phone" : "15230398493",
        "u_highMath" : "19,1",
        "d_build_id" : "000e4e5",
        "d_build_time" : "Thu Dec 14 16:03:16 CST 2017",
        "d_model_brand" : "R7c",
        "u_city" : "北京市",
        "d_os_version" : "4.4.4",
        "u_activateDate" : "2017-12-10T02:34:48.123Z",
        "u_role" : "student",
        "u_province" : "北京",
        "role" : "student",
        "u_juniorMath" : "17,2",
        "u_ladderJuniorMath" : "18,2",
        "u_name" : "1512873288121_@@_15230398493",
        "u_level" : 9,
        "u_VIP" : "",
        "u_pattern" : "-1",
        "os" : "android",
        "platform" : "app",
        "u_type" : "signup",
        "u_power" : 610,
        "u_nickname" : "15230398493",
        "d_app_version" : "4.3.2",
        "u_leadbarState" : False,
        "u_from" : "android",
        "noticeId" : "5a33af27487f6154f4710a28",
        "u_hasRoom" : False,
        "category" : "learn",
        "d_model_name" : "OPPO",
        "u_lastPublisher" : "2,1",
        "eventKey" : "getChapterListBanner",
        "u_ability" : 240,
        "u_school" : "北京大学附属中学",
        "device" : "868239024974375",
        "uuid" : "80131b0d-0778-4ce4-897a-3087a3ab034c",
        "eventTime" : 1514356023649,
        "d_os_name" : "android",
        "channel" : "oppokeke",
        "u_channel" : "oppokeke",
        "u_user" : "5a2c9d48b5cc21289c5ad8b3",
        "ip" : "118.191.248.3",
        "ua" : "okhttp/3.4.2",
        "api" : "/api/v4/events",
        "d_appVersion" : "4.3.2",
        "user" : "5a2c9d48b5cc21289c5ad8b3"
    },
    {
        "u_gender" : "female",
        "u_juniorPhysics" : "16,2",
        "u_tenant" : "-1",
        "u_phone" : "15230398493",
        "d_build_id" : "000e4e5",
        "d_build_time" : "Thu Dec 14 16:03:16 CST 2017",
        "d_model_brand" : "R7c",
        "u_city" : "北京市",
        "d_os_version" : "4.4.4",
        "u_activateDate" : "2017-12-10T02:34:48.123Z",
        "u_role" : "student",
        "u_province" : "北京",
        "role" : "student",
        "u_juniorMath" : "17,2",
        "u_ladderJuniorMath" : "18,2",
        "u_name" : "1512873288121_@@_15230398493",
        "u_level" : 9,
        "u_VIP" : "",
        "u_pattern" : "-1",
        "os" : "android",
        "platform" : "app",
        "u_type" : "signup",
        "u_power" : 610,
        "u_nickname" : "15230398493",
        "d_app_version" : "4.3.2",
        "u_leadbarState" : False,
        "u_from" : "android",
        "noticeId" : "5a2fa8620533b9258fe19ba7",
        "u_hasRoom" : False,
        "category" : "show",
        "d_model_name" : "OPPO",
        "u_lastPublisher" : "2,1",
        "eventKey" : "enterShowBanner",
        "u_ability" : 240,
        "u_school" : "北京大学附属中学",
        "device" : "868239024974375",
        "uuid" : "be22e1a3-0fa6-412c-8b73-cc20b9b91926",
        "eventTime" : 1514356022202,
        "d_os_name" : "android",
        "channel" : "oppokeke",
        "u_channel" : "oppokeke",
        "u_user" : "5a2c9d48b5cc21289c5ad8b3",
        "ip" : "106.118.160.183",
        "ua" : "okhttp/3.4.2",
        "api" : "/api/v4/events",
        "d_appVersion" : "4.3.2",
        "user" : "5a2c9d48b5cc21289c5ad8b3"
    },
    {
        "u_gender" : "female",
        "u_juniorPhysics" : "16,2",
        "u_tenant" : "-1",
        "noticeName" : "9年级期末课程包-函数综合",
        "u_phone" : "15230398493",
        "u_highMath" : "19,1",
        "d_build_id" : "000e4e5",
        "d_build_time" : "Thu Dec 14 16:03:16 CST 2017",
        "d_model_brand" : "R7c",
        "u_city" : "北京市",
        "d_os_version" : "4.4.4",
        "u_activateDate" : "2017-12-10T02:34:48.123Z",
        "u_role" : "student",
        "u_province" : "北京",
        "role" : "student",
        "u_juniorMath" : "17,2",
        "u_ladderJuniorMath" : "18,2",
        "u_name" : "1512873288121_@@_15230398493",
        "u_level" : 9,
        "u_VIP" : "",
        "u_pattern" : "-1",
        "os" : "android",
        "platform" : "app",
        "u_type" : "signup",
        "u_power" : 610,
        "u_nickname" : "15230398493",
        "d_app_version" : "4.3.2",
        "u_leadbarState" : False,
        "u_from" : "android",
        "noticeId" : "5a33aeecb03e1e7b53aa7800",
        "u_hasRoom" : False,
        "category" : "learn",
        "d_model_name" : "OPPO",
        "u_lastPublisher" : "2,1",
        "eventKey" : "getChapterListBanner",
        "u_ability" : 240,
        "u_school" : "北京大学附属中学",
        "device" : "868239024974375",
        "uuid" : "7fa290ca-1e51-4850-980f-c29635143eb3",
        "eventTime" : 1514356019649,
        "d_os_name" : "android",
        "channel" : "oppokeke",
        "u_channel" : "oppokeke",
        "u_user" : "5a2c9d48b5cc21289c5ad8b3",
        "ip" : "61.48.33.123",
        "ua" : "okhttp/3.4.2",
        "api" : "/api/v4/events",
        "d_appVersion" : "4.3.2",
        "user" : "5a2c9d48b5cc21289c5ad8b3"
    }
]


def request_header():
    """
    Set request header
    """
    return {
        "Content-Type": "application/json",
        "timestamp": str(int(time.time())),
        "uuid": str(uuid.uuid4()),
    }


def request_body(user_id, type_is):
    """
    Set request body
    """
    random_num = random.randint(0, len(EVENTS_LIST) - 1)
    return dict(EVENTS_LIST[random_num])


class UserBehavior(TaskSet):
    """ Set user behavior """
    def on_start(self):
        """ on_start is called when Locust start before any task is scheduled """
        self.index()

    def index(self):
        """ Visit index api ping-pong test """
        response = self.client.get("/api")
        print(response)

    @task(1)
    def eventv4_single(self):
        """ Send single event """
        req_header = request_header()
        req_body = request_body(req_header["uuid"], "single")
        req_header["remoteip"] = req_body["ip"]
        data = json.dumps(req_body)
        response = self.client.request(
            method="POST",
            url=APIURL,
            data=data,
            headers=req_header
        )
        if response.status_code == 204:
            print("SINGLE REQUEST SUCCESS: " + req_header["uuid"])

    """
    @task takes an optional weight argument that can be used
    to specify the task’s execution ratio.
    In the following example task2 will be executed
    twice as much as task1:
    """
    @task(2)
    def eventv4_batch(self):
        """ Send batch events """
        req_header = request_header()
        req_body = request_body(req_header["uuid"], "single")
        req_header["remoteip"] = req_body["ip"]
        batch_data = []
        batch_data.append(req_body)
        batch_data = batch_data * random.randint(1, 6)
        response = self.client.request(
            method="POST",
            url=APIURL,
            data=json.dumps(batch_data),
            headers=req_header,
        )
        if response.status_code == 204:
            print("BATCH REQUSET SUCCESS: "+ req_header["uuid"])


class WebsiteUser(HttpLocust):
    """ The Locust class (as well as HttpLocust since
    it’s a subclass) also allows one to specify minimum
    and maximum wait time—per simulated user—between
    the execution of tasks (min_wait and max_wait)
    as well as other user behaviours. """
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
