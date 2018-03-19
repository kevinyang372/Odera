from EllipticCurve import generate_key
from EllipticCurve import generate_signature
from EllipticCurve import verify_message
import hashlib
import random

#generate the whole blockchain network
class blockchain:
	#initialization
	def __init__(self,previous_block,users):
		self.blockchain = previous_block
		self.temp_block = []
		self.HASH = "bdb20d83a467125eaee83d71ace906fee166ac8627df6ef13b4401538a8feb3e"
		self.users = users

	#append new transaction data
	def add_data(self,number,fromuser,touser):
		#when the number of transactions in a block reaches three => append to the blockchain
		if len(self.temp_block) == 3:
			#conduct proof of work
			self.ProofOfWork()
			#update user assets info
			self.update_user_info()
			#summary of information in the block
			summary = self.combination()
			self.blockchain.append([self.HASH,summary])
			#update HASH of the block
			self.HASH = self.MerkleRoot(self.HASH,summary)
			#clear the temporary block
			self.temp_block = []
		self.temp_block.append([number,fromuser,touser])

	#summarize the information in the temporary block
	def combination(self):
		temp = []
		for i in self.temp_block:
			message = str(i[0]) + " from " + i[1] + " to " + i[2]
			temp.append(message)
		return temp

	#present the blockchain
	def ShowBlocks(self):
		for i in range(1,len(self.blockchain)):
			print()
			print("HASH: ",self.blockchain[i][0])
			result = []
			for t in self.blockchain[i][1]:
				result.append(t)
			print(result)

	#Proof of work algorithm
	def ProofOfWork(self):
		string = "FinBlock is Awesome"
		complete = False
		n = 0
		while complete == False:
			curr_string = string + str(n)
			curr_hash = hashlib.md5(curr_string.encode('utf-8')).hexdigest()
			n = n + 1
			if curr_hash.startswith('00000'):
				print("Proof Of Work Done")
				complete = True

	#compute the merkle root of the block
	def MerkleRoot(self,previous_hash,info_summary):
		t = previous_hash
		for i in info_summary:
			t = t + i
		return hashlib.sha256(t.encode('utf-8')).hexdigest()

	#update the user account
	def update_user_info(self):
		for i in self.temp_block:
			for k in range(0,len(self.users)):
				if self.users[k][1] == i[1]:
					self.users[k][2] = str(float(self.users[k][2]) - i[0])
				if self.users[k][1] == i[2]:
					self.users[k][2] = str(float(self.users[k][2]) + i[0])

	#return users
	def synchronize(self):
		return self.users
