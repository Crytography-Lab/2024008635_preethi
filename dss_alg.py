from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(2048)
private_key = key
public_key = key.publickey()

message = b"Cryptography Digital signature standard"
hash_obj = SHA256.new(message)

signer = DSS.new(private_key, 'fips-186-3')
signature = signer.sign(hash_obj)

print("Message: ", message.decode())
print("Digital signature: ", signature.hex())

hash_obj = SHA256.new(message)
verifier = DSS.new(public_key, 'fips-186-3')

try:
    verifier.verify(hash_obj, signature)
    print("Signature is valid.")
except ValueError:
    print("Signature is invalid.")
