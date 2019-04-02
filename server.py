from blockchain_study import Blockchain
import json
from textwrap import dedent
from uuid import uuid4
from flask import request, Flask, jsonify

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/transactions/new/json', methods=['POST'])
def new_transactions():
	values = request.get_json()
	if not values:
		return 'Data is None', 400

	#요청된 필드가 POST 된 데이터인지 확인
	required = ['sender', 'recipient', 'amount']
	if not all(k in values for k in required):
		return 'Missing values', 400

	# 새로운 거래 생성
	index = blockchain.new_transaction(
		values['sender'], values['recipient'], values['amount'])

	response = {'message': f'Transaction will be added to Block{index}'}
	return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
	response = {
		'chain': blockchain.chain,
		'length': len(blockchain.chain)
		}
	return jsonify(response), 200

@app.route('/mine', methods = ['GET'])
def mine():
	#다음 블록의 proof 값을 얻어내기 위해 POW 알고리즘을 수행한다.
	last_block = blockchain.last_block
	last_proof = last_block['proof']
	proof = blockchain.mine_proof(last_proof)

	#proof 값을 찾으면(채굴에 성공하면) 보상을 준다.
	#sender의 주소를 0으로 한다. (원래 거래는 송신자, 수신자가 있어야 하는데
	# 채굴에 대한 보상으로 얻은 코인은 sender가 없다.)
	blockchain.add_new_transaction(
		sender="0",
		recipient=node_identifier,
		amount=1)

	previous_hash = blockchain.hash(last_block)
	block = blockchain.add_new_block(proof, previous_hash)

	response = {
		'message': "NewBlock Forged",
		'index': block['index'],
		'transactions': block['transactions'],
		'proof': block['proof'],
		'previous_hash': block['previous_hash']
		}
	return jsonify(response), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port= 5000)