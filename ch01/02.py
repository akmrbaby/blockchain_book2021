import hashlib

IV = "0000"
block1 = "0001:" + IV
block2 = "0002:" + hashlib.sha256(block1.encode("utf-8")).hexdigest()
block3 = "0003:" + hashlib.sha256(block2.encode("utf-8")).hexdigest()
block4 = "0004:" + hashlib.sha256(block3.encode("utf-8")).hexdigest()

hashchain = [block1, block2, block3, block4]
lasthash = hashlib.sha256(block4.encode("utf-8")).hexdigest()

print(f"ハッシュチェーン: {hashchain}")
print(f"最終ハッシュ値: {lasthash}")