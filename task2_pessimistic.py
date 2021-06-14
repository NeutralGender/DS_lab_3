import hazelcast

client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=[
        "172.17.0.4:5701",
        "172.17.0.5:5701",
        "172.17.0.6:5701"
    ]
)

my_map = client.get_map("lab3_task1")

key = "1"
my_map.put(key, 0)

print("Starting pessemistic:")

for i in range(1, 1000):
    my_map.lock(key).result()
    try:
        value = my_map.get(key).result()
        value = int(value) + 1
        my_map.put(key, value)
    finally:
        my_map.unlock(key)
        
print("Pessimostic Result: " + str(my_map.get(key).result()))




















