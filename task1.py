import hazelcast

client = hazelcast.HazelcastClient(
    cluster_name="dev",
    cluster_members=[
        "127.0.0.1:9001",
        "127.0.0.1:9002",
        "127.0.0.1:9003"
    ]
)

my_map = client.get_map("lab3_task1")

key = "1"
my_map.put(key, 0)

for i in range(1000):
    value = my_map.get(key).result()
    value = int(value) + 1
    my_map.put(key, value)

print("Result: " + str(my_map.get(key).result()))
