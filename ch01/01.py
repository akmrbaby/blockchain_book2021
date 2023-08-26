import hashlib

data1 = "12345"
data2 = "12346"

hash1 = hashlib.sha256(data1.encode("utf-8")).hexdigest()
hash2 = hashlib.sha256(data2.encode("utf-8")).hexdigest()

print(f"'{data1}'のハッシュ値: {hash1}")
print(f"'{data2}'のハッシュ値: {hash2}")