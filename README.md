# Locust for bd_eventreceiver

本测试用例仅针对bd_eventreceiver v4版本API。首先应当部署启动好bd_eventreceiver到9998。

## 单机压测

```shell
locust -f locustfile_eventv4.py --host="http://localhost:9998"
```

## 并行压测

首先启动master进程

```shell
locust -f locustfile_eventv4.py --master --host="http://localhost:9998"
```

然后启动slave进程

```shell
locust -f locustfile_eventv4.py --slave --host="http://localhost:9998"
```

如过想在分布式集群内进行部署压测，首先开启主节点master进程，然后启动slave指定master节点的IP

```shell
locust -f locustfile_eventv4.py --slave --master-host=10.8.8.111 --host="http://localhost:9998"
```

## 测试配置

在启动master的节点上可以访问到locust的web操作界面：

[http://127.0.0.1:8089](http://127.0.0.1:8089)

鉴于我们的线上业务场景是短连接形式：

`Number of users to simulate` 设置 300
`Hatch rate (users spawned/second)` 设置 10
