import hashlib

IV = "0000"   # 初期値？
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

def verifyhashchain(hashchain, prev_hash, lasthash):
    isVerified = True
    for block in hashchain:
        hash = block.split(":")[1]
        if hash == prev_hash:
            prev_hash = hashlib.sha256(block.encode("utf-8")).hexdigest()
            continue
        else:
            isVerified = False
            break
    if prev_hash != lasthash:
        isVerified = False
    return isVerified

isVerified = verifyhashchain(blockchain, IV, lasthash)
print(f"検証結果: {isVerified}")