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
key = '1'
my_map.put_if_absent(key, 1)

def custom_replace_if_the_same(key, old_value, new_value):
    if my_map.contains_key(key) and my_map.get(key) == old_value:
        my_map.put(key, new_value)
        return True
    else:
        return False

print('starting')
for i in range(1000):
    while True:
        old_value = my_map.get(key)
        new_value = int(old_value) + 1
        if custom_replace_if_the_same(key, old_value, new_value):
            break
        
        # Standart impl:
        #if my_map.replace_if_same(key, old_value, new_value):
        #    break

print(" Optimistic locking Finished! Result = " + str(my_map.get(key)))



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
my_map.put_if_absent(key, 0)

for i in range(0, 10):
    while True:
        old_val = my_map.get(key)
        time.sleep(0.1)
        new_val = int(old_val) + 1
        print(new_val)
        if my_map.replace_if_same(key, old_val, new_val):
            break

print("Optimistic Result: " + str(my_map.get(key)))

'''

















