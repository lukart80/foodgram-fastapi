from hashlib import sha256


async def hash_string(string: str) -> str:
    hash_obj = sha256(bytes(string, 'utf8'))
    return hash_obj.hexdigest()
