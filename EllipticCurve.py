import ecdsa
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import random
from ecdsa.util import string_to_number, number_to_string
import codecs
import binascii

def random_secret():
    sk = SigningKey.generate(curve=SECP256k1)
    return sk

def generate_key():
    # Generate a new private key.
    secret = random_secret() 
    print("Private Key: ", secret.to_string().hex())

    public = secret.get_verifying_key()
    print("Public Key:", public.to_string().hex())

    print()

    return secret.to_string().hex(), public.to_string().hex()

def generate_signature(private_key,message):
    sk = SigningKey.from_string(bytes.fromhex(private_key),curve=SECP256k1)
    signature = sk.sign(message.encode('utf-8'))
    return signature.hex()

def verify_message(signature,message,public_key):
    pk = VerifyingKey.from_string(bytes.fromhex(public_key),curve=SECP256k1)
    result = pk.verify(bytes.fromhex(signature),message.encode('utf-8'))
    return result