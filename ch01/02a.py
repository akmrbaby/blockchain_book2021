import hashlib

IV = "0000"
data_list = ["0001", "0002", "0003", "0004"]

def hashchain(data_list, prev_hash):
    blockchain = []
    for data in data_list:
        block = data + ":" + prev_hash
        prev_hash = hashlib.sha256(block.encode("utf-8")).hexdigest()
        blockchain.append(block)
    return blockchain

blockchain = hashchain(data_list, IV)
lasthash = hashlib.sha256(blockchain[-1].encode("utf-8")).hexdigest()

print(f"ハッシュチェーン: {blockchain}")
print(f"最終ハッシュ値: {lasthash}")