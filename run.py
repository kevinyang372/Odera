from create_user import retrieve_user_data, retrieve_block_data, write_user_data, write_block_data, cleandata
from users import generate_keys
from blockchain import blockchain
import EllipticCurve

cleandata()
users = retrieve_user_data()
data = retrieve_block_data()
ledgers = blockchain(data,users)

while True:
	print("Do you want to create a new account or sign in")
	k = input()
	if k == '1':
		public, private = generate_keys()
		users.append([public, private, '10'])
		current_user = [public, private, '10']
		current_index = len(users) - 1
	else:
		print("Please input your public key")
		p = input()
		print("Please input your private key")
		p2 = input()
		for i in range(0,len(users)):
			if p == users[i][0] and p2 == users[i][1]:
				current_user = users[i]
				current_index = i
				print("Login Successful")
	print("Continue?")
	stop = input()
	if stop == "exit":
		break

while True:
	print()
	print("Who do you want to transfer to? (public key)")
	k = input()
	print("How much do you want to transfer?")
	num = int(input())
	while num > int(current_user[2]):
		print("Invalid input")
		num = int(input())
	current_user[2] = str(int(current_user[2]) - num)
	ledgers.add_data(num,current_user[1],k)
	print("Continue?")
	stop = input()
	if stop == "exit":
		break

ledgers.ShowBlocks()

users = ledgers.synchronize()

print()
print(users)
print()

print("Process Ended")

write_user_data(users)


