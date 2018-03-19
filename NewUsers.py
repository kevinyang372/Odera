from EllipticCurve import generate_key
from EllipticCurve import generate_signature
from EllipticCurve import verify_message
import ecdsa
from ecdsa import SigningKey
import hashlib
import random

# create a new user in the network
class NewUsers:
	def __init__(self):
		self.private_key, self.public_key = generate_key()
		self.temp_block = []
		self.present_block = []
		self.blockchain = []
		self.present_blockchain = []
		self.tempencrypted_message = []
		self.encrypted_message=[]
		self.HASH = "00000"

	def AddData(self,data):
		if len(self.temp_block) == 4:
			pointer = int(random.random()*10)
			self.ProofOfWork()
			self.blockchain.append([self.HASH,pointer,self.temp_block])
			self.HASH = self.MerkleRoot(self.HASH,pointer,self.temp_block)
			self.present_blockchain.append(self.present_block)
			self.encrypted_message.append(self.tempencrypted_message)
			self.temp_block = []
			self.present_block = []
			self.tempencrypted_message = []
		signature = generate_signature(self.private_key,data)
		self.temp_block.append(signature)
		self.present_block.append(signature.hex())
		self.tempencrypted_message.append(data)

	def ShowBlocks(self):
		for i in self.blockchain:
			print()
			print("HASH: ",i[0])
			print("Pointer: ",i[1])
			result = []
			for t in i[2]:
				result.append(t.hex())
			print(result)

	def MerkleRoot(self,previous_hash,pointer,info_summary):
		t = previous_hash + str(pointer)
		for i in info_summary:
			t = t + i.hex()
		return hashlib.sha256(t.encode('utf-8')).hexdigest()

	#def CheckBlocks(self):
		#check = True
		#if len(self.blockchain) > 1:
			#for i in range(1,len(self.blockchain)):
				#if self.blockchain[i]

	def GetData(self,private_key):
		if self.private_key.to_string().hex() == private_key:
			for i in range(len(self.blockchain)):
				for k in range(len(self.blockchain[i][2])):
					if verify_message(self.blockchain[i][2][k],self.encrypted_message[i][k],self.public_key):
						print(self.encrypted_message[i][k])

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
