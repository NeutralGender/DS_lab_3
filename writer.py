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

my_queue = client.get_queue("task3")

for i in range(20):
    print(my_queue.add(i).result())
    print('Producing: ' + str(i))
    time.sleep(0.5)
my_queue.add(-1)

'''
for i in range(1, 200):
    my_queue.add(i)
    print("Add: " + str(i))
    time.sleep(0.5)

my_queue.add(-1)
'''

client.shutdown()