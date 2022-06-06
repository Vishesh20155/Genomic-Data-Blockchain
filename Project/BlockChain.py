import hashlib

class genome_blockchain:
	def __init__(self, previous_block_hash, transaction_list):
		self.previous_block_hash = previous_block_hash
		self.transaction_list = transaction_list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "A sends 3 to M"
t2 = "B sends 4.1 to M"
t3 = "M sends 5.4 to C"
t4 = "C sends 7 to D"

initial_block = genome_blockchain("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

''' 
	Instead of string transactions, we will store the transaction type:
		1. STORE the genomic data
		2. Access Genomic Data
	Above thing implemented using a class and different functions for each will be made.

'''