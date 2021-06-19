import hazelcast
import time

client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=[
        "127.0.0.1:9001",
        "127.0.0.1:9002",
        "127.0.0.1:9003"
    ]
)

my_queue = client.get_queue("task3").blocking()

while True:
    val = my_queue.take()
    print("Read:" + str(val))
    if val == -1:
        print("Read stop val: " + str(val))
        break

print("Reader stop")













