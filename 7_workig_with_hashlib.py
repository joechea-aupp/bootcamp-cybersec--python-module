import hashlib

data = "Hello World".encode()
print("data: ", data)

md5_hash = hashlib.md5(data).hexdigest()
print("hash_object: ", md5_hash)

sha256_hash = hashlib.sha256(data).hexdigest()
print("sha256_hash: ", sha256_hash)


# hash lookup
# https://md5hashing.net/hash/md5/b10a8db164e0754105b7a99be72e3fe5
