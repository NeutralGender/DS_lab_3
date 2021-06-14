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

for i in range(0, 1000):
    while True:
        old_val = my_map.get(key).result()
        new_val = int(old_val) + 1
        if my_map.replace_if_same(key, old_val, new_val).result():
            break

print("Optimistic Result: " + str(my_map.get(key).result()))



















