import csv

def retrieve_user_data():
	user_data = []
	with open('users.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			user_data.append(row)
	user_data.pop(0)
	return user_data

def retrieve_block_data():
	block_data = []
	with open('block.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			block_data.append(row)
	return block_data

def write_user_data(s):
	with open('users.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in s:
			filewriter.writerow(i)

def write_block_data(s):
	with open('block.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in s:
			filewriter.writerow(i)

def cleandata():
	with open('users.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow([])