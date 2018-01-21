from EllipticCurve import generate_key
from EllipticCurve import generate_signature
from EllipticCurve import verify_message

def generate_keys():
	private_key, public_key = generate_key()
	return private_key, public_key
