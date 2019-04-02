import unittest
import blockchain_study
import json
import random
import hashlib

class Test_testcase(unittest.TestCase):
	def setUp(self):
		self.blockchain = blockchain_study.Blockchain()

	def tearDown(self):
		print('----------------------------------------------------------------------')

	def test_last_block(self):
		print('last_block')
		test = self.blockchain.last_block
		self.assertEqual(0, test['index'])
		self.assertEqual([], test['transactions'])
		self.assertEqual(100, test['proof'])
		self.assertEqual('1', test['previous_hash'])
		
	def test_add_new_block(self):
		print('add_new_block')
		first_test = self.blockchain.add_new_block(100, '1')
		self.assertEqual(1, first_test['index'])
		self.assertEqual([], first_test['transactions'])
		self.assertEqual(100, first_test['proof'])
		self.assertEqual('1', first_test['previous_hash'])

	def test__hash_block(self):
		print('_hash_block')
		self.assertEqual("1f29b53c61e104320ab84a4601bc52632d400f1c1c65a6f8fa238d86e6d8b2a5",
				   self.blockchain._hash_block({'index': 1, 'timestamp': 1553963991.0131576, 'transactions': [], 'proof': 100, 'previous_hash': 1}))
		self.assertEqual("e0502abd15fde09f6d26d9908d088da9550e88e7e687a25884c071ddc155cc09",
				   self.blockchain._hash_block({'index': 2, 'timestamp': 1553963619.006812, 'transactions': [], 'proof': 1, 'previous_hash': '5c0c40ab181eba10a74fd8d9b52ab0ec260e3d412560ca2025092cae29ecf4e7'}))
		self.assertEqual("fc5e10d432f43e8befed7597249046fcccb5422e4cb64272d87a7b239084d2fd",
				   self.blockchain._hash_block({'index': 3, 'timestamp': 1553963619.006812, 'transactions': [], 'proof': 1, 'previous_hash': '55c3e27d01c5bdcb0ef34a03c3d9f860f9120cfd6ecd2b3c83ddd3dae1fbdb94'}))

	def test__create_block_dict(self):
		print('_create_block_dict')
		test = self.blockchain._create_block_dict(1, 2, [], 100, "123")
		self.assertTrue({'index':1, 'timestamp':2, 'transactions':[], 'proof':100,'previous_hash':'123'},
				  test)

	def test_add_new_transaction(self):
		print('add_new_transaction')
		self.assertEqual(1, self.blockchain.add_new_transaction('kyung', 'byeu', '1'))
		self.assertEqual([{'sender': 'kyung', 'recipient': 'byeu', 'amount': '1'}],
				   self.blockchain.current_transactions)
		self.assertEqual(1, self.blockchain.add_new_transaction('kue', 'co', '1'))
		self.assertEqual([{'sender': 'kyung', 'recipient': 'byeu', 'amount': '1'}, {'sender': 'kue', 'recipient': 'co', 'amount': '1'}], 
				   self.blockchain.current_transactions)
		self.assertEqual(1, self.blockchain.add_new_transaction('dae', 'byung', '1'))
		self.assertEqual([{'sender': 'kyung', 'recipient': 'byeu', 'amount': '1'}, {'sender': 'kue', 'recipient': 'co', 'amount': '1'}, {'sender': 'dae', 'recipient': 'byung', 'amount': '1'}], 
				   self.blockchain.current_transactions)

	def test__create_transaction_dict(self):
		print('_create_transaction_dict')
		self.assertEqual({'sender': 'kyung', 'recipient':'byeu', 'amount':'1'},
			self.blockchain._create_transaction_dict('kyung', 'byeu', '1'))
		self.assertEqual({'sender':'kue', 'recipient':'co', 'amount':'1'},
			self.blockchain._create_transaction_dict('kue', 'co', '1'))
		self.assertEqual({'sender':'dae', 'recipient':'byung', 'amount':'1'},
			self.blockchain._create_transaction_dict('dae', 'byung', '1'))

	def test_mine_proof(self):
		print('mine_proof')
		self.assertEqual(35293, self.blockchain.mine_proof(100))

	def test__is_valid_proof(self):
		print('_is_balid_proof')
		self.assertFalse(self.blockchain._is_valid_proof(100, 101))
		self.assertTrue(self.blockchain._is_valid_proof(100, 35293))

	def test__are_first_four_zero(self):
		print('_are_first_four_zero')
		self.assertFalse(self.blockchain._are_first_four_zero('1010010000'))
		self.assertTrue(self.blockchain._are_first_four_zero('0000123123'))
		self.assertFalse(self.blockchain._are_first_four_zero('000'))
		self.assertTrue(self.blockchain._are_first_four_zero('0000'))

	def test_register_node(self):
		print('register_node')
		self.blockchain.register_node('https://127.0.0.1:52273/index.html')
		self.assertEqual(self.blockchain.nodes, {'127.0.0.1:52273'})

if __name__ == '__main__':
    unittest.main()
