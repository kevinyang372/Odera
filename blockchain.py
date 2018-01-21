from EllipticCurve import generate_key
from EllipticCurve import generate_signature
from EllipticCurve import verify_message
import hashlib
import random

class blockchain:
	def __init__(self,previous_block,users):
		self.blockchain = previous_block
		self.temp_block = []
		self.HASH = "bdb20d83a467125eaee83d71ace906fee166ac8627df6ef13b4401538a8feb3e"
		self.users = users

	def add_data(self,number,fromuser,touser):
		if len(self.temp_block) == 3:
			self.ProofOfWork()
			self.update_user_info()
			summary = self.combination()
			self.blockchain.append([self.HASH,summary])
			self.HASH = self.MerkleRoot(self.HASH,summary)
			self.temp_block = []
		self.temp_block.append([number,fromuser,touser])

	def combination(self):
		temp = []
		for i in self.temp_block:
			message = str(i[0]) + " from " + i[1] + " to " + i[2]
			temp.append(message)
		return temp

	def ShowBlocks(self):
		for i in range(1,len(self.blockchain)):
			print()
			print("HASH: ",self.blockchain[i][0])
			result = []
			for t in self.blockchain[i][1]:
				result.append(t)
			print(result)

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

	def MerkleRoot(self,previous_hash,info_summary):
		t = previous_hash
		for i in info_summary:
			t = t + i
		return hashlib.sha256(t.encode('utf-8')).hexdigest()

	def update_user_info(self):
		for i in self.temp_block:
			for k in range(0,len(self.users)):
				if self.users[k][1] == i[1]:
					self.users[k][2] = str(int(self.users[k][2]) - i[0])
				if self.users[k][1] == i[2]:
					self.users[k][2] = str(int(self.users[k][2]) + i[0])

	def synchronize(self):
		return self.users