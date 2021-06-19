import hazelcast
import time

if __name__ == "__main__":
    client = hazelcast.HazelcastClient(
        cluster_name="dev",
        cluster_members=[
            "127.0.0.1:9001",
            "127.0.0.1:9002",
            "127.0.0.1:9003"
        ],

    )

my_map = client.get_map("lab3_task1").blocking()
key = '1'
my_map.put_if_absent(key, 1)

print('Start: ')

for i in range(1000):
    my_map.lock(key)
    try:
        value = my_map.get(key)
        value = int(value) + 1
        my_map.set(key, value)
    finally:
        my_map.unlock(key)

print("Done pes locking: ", my_map.get(key))

client.shutdown()





'''
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

my_map = client.get_map("lab3_task1").blocking()

key = "1"
my_map.put(key, 0)

print("Starting pessemistic:")

for i in range(1, 10):
    my_map.lock(key)#.result()
    try:
        value = my_map.get(key)#.result()
        print(value)
        time.sleep(1)
        value = int(value) + 1
        my_map.put(key, value)
    finally:
        my_map.unlock(key)
        
print("Pessimostic Result: " + str(my_map.get(key)))#.result()))
'''
