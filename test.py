from create_user import retrieve_user_data, retrieve_block_data, write_user_data, write_block_data, cleandata
from users import generate_keys
from blockchain import blockchain
import EllipticCurve
import random

cleandata()
users = retrieve_user_data()
data = retrieve_block_data()
ledgers = blockchain(data,users)

for i in range(50):
	public, private = generate_keys()
	users.append([public, private, '10'])
	current_user = [public, private, '10']
	current_index = len(users) - 1

for i in range(500):
	k = users[random.randint(1,len(users))-1][0]
	num = random.random() * 0.1
	while num > float(current_user[2]):
		print("Invalid input")
		num = random.random() * 0.1
	current_user[2] = str(float(current_user[2]) - num); ledgers.add_data(num,current_user[1],k); current_user = users[random.randint(1,len(users))-1]

ledgers.ShowBlocks()

users = ledgers.synchronize()

print("================")
print(users)
print("================")

print("Process Ended")

write_user_data(users)
