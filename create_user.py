import csv

#get user data
def retrieve_user_data():
	user_data = []
	with open('users.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			user_data.append(row)
	user_data.pop(0)
	return user_data

#get blockchain data
def retrieve_block_data():
	block_data = []
	with open('block.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			block_data.append(row)
	return block_data

#write new user data into record
def write_user_data(s):
	with open('users.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in s:
			filewriter.writerow(i)

#write new blockchain data into record
def write_block_data(s):
	with open('block.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in s:
			filewriter.writerow(i)

#clean all the data in the file
def cleandata():
	with open('users.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow([])
