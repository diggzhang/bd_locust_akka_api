from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when Locust start before any task is scheduled """
        self.login()

    def login(self):
        """ login is a post request """
        self.client.post("/login", {"username": "diggzhang", "password": "tellmepass"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")


class WebsiteUser(HttpLocust):
    """ The Locust class (as well as HttpLocust since
    it’s a subclass) also allows one to specify minimum
    and maximum wait time—per simulated user—between
    the execution of tasks (min_wait and max_wait)
    as well as other user behaviours. """
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000


"""
To run Locust with the above Locust file, if it was named 
locustfile.py and located in the current working directory, 
we could run:

```shell
locust -f locust_files/my_locust_file.py --host=http://example.com
```

To run Locust distributed across multiple processes we would 
start a master process by specifying --master:

```shell
locust -f locust_files/my_locust_file.py --master --host=http://example.com
```

and then we would start an arbitrary number of slave processes:

```shell
locust -f locust_files/my_locust_file.py --slave --host=http://example.com
```

If we want to run Locust distributed on multiple machines 
we would also have to specify the master host when starting 
the slaves (this is not needed when running Locust distributed 
on a single machine, since the master host defaults to 127.0.0.1):

```shell
locust -f locust_files/my_locust_file.py --slave --master-host=192.168.0.100 --host=http://example.com
```

Once you’ve started Locust using one of the above command lines, 
you should open up a browser and point it to 
http://127.0.0.1:8089 (if you are running Locust locally). 
"""
