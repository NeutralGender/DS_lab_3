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

for i in range(20):
    print(my_queue.offer(i))
    print('Producing: ' + str(i))
my_queue.add(-1)

client.shutdown()