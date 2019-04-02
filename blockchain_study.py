import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

class Blockchain(object):
	def __init__(self):
		self.chain = [] # blocks' chain
		self.current_transactions = [] # transaction list that is writed when the blockchain created
		self.nodes = set() # use set() to eliminate redundancy

		#create genesis block(the first block)
		self.add_new_block(proof=100, genesis_hash='1')

	@property
	def last_block(self):
		return self.chain[-1]

	def add_new_block(self, proof, genesis_hash=None):
		"""
		add blockchain the new block

		:param proof: <int> proof is provided by Proof of Work algorithm
		:param previous_hash: <str> previous block's hash. if first, put None
		:return : <dict> new block
		"""
		
		block = self._create_block_dict(
			len(self.chain), 
			time(),
			self.current_transactions,
			proof,
			self._hash_block(self.chain[-1]) if genesis_hash is None else genesis_hash
			)

		# 거래 내역 초기화
		self.current_transactions.clear()

		self.chain.append(block)
		return block

	def _hash_block(self, block):
		"""
		create block's sha-256 hash

		:param block: <dict> Block
		:return : <str> hexdigest
		"""

		#hash block
		block_string = json.dumps(block, sort_keys = True).encode()
		return hashlib.sha256(block_string).hexdigest()

	def _create_block_dict(self, index, timestamp, transactions, proof, previous_hash):
		#새로운 블록 생성
		return {'index': index,
               'timestamp': timestamp,
               'transactions': transactions,
               'proof': proof,
               'previous_hash': previous_hash}

	def add_new_transaction(self, sender, recipient, amount):
		"""
		create transaction for next block

		:param sender: <str> Sender's address
		:param recipient: <str> Recipient's address
		:param amount: <int> amount
		:return: <int> block's index that will include this transaction
		"""
		self.current_transactions.append(
			self._create_transaction_dict(
				sender, recipient, amount
			))
		
		return (self.last_block['index'] + 1)

	def _create_transaction_dict(self, sender, recipient, amount):
		return {'sender': sender,
				'recipient': recipient,
				'amount': amount}

	def mine_proof(self, last_proof):
		"""
		POW(proof of work) algorithm:
		 - search hash(pp') whose first four number are 0
		 - p is previous block's proof, p' is new block's proof

		:param last_proof : <int>
		:return : <int>
		"""

		proof = 0
		while self._is_valid_proof(last_proof, proof) is False:
			proof +=1

		return proof

	def _is_valid_proof(self, last_proof, proof):
		"""
		check hash(last_proof + proof)'s first four digits are 0

		:param last_proof: <int> previous block's proof
		:param proof: <int> current block's proof
		:return: <bool>
		"""
		
		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return self._are_first_four_zero(guess_hash)

	def _are_first_four_zero(self, hex_hash):
		if len(hex_hash) < 4:
			return False
		for i in range(0,4):
			if hex_hash[i] != '0':
				return False
		return True

	def register_node(self, address):
		"""
		register a new node in the existing node list
		use: request to register in the fomm of 'http://ip:port'.
		
		:param address: <string> (ex)127.0.0.1:52273
		"""
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc)

	def resolve_conflicts(self):
		"""
		Algorithm agreement:
		the node having the longest chain is considered valid.
		"""
		neighbours = self.nodes
		new_chain = None

		max_length = len(self.chain)

		for node in neighbours:
			response = requests.get(f'http://{node}/chain')

			if response.status_code == 200:
				length = response.json()['length']
				chain = response.json()['chain']

				if length > max_legth and self._is_valid_chain(chain):
					max_length = length
					nex_chain = chain

			if new_chain:
				self.chain = new_chain
				return True

		return False

	def _is_valid_chain(self, chain):
		"""
		decide whether the chain is valid.
		"""

		last_block = chain[0]
		current_index = 1

		while current_index < len(chain):
			block = chain[current_index]
			print(f'{last_block}')
			print(f'{block}')
			print('\n-------------\n')

			if block['previous_hash'] != self._hash_block(last_block):
				return False

			if not self._is_valid_proof(last_block['proof'], block['proof']):
				return False

			last_block = block
			current_index += 1

		return True
				
