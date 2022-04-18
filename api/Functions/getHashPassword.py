
import hashlib

def getHashPassword( _pwd: bytes, _salt: bytes ):
    return hashlib.pbkdf2_hmac(hash_name="sha512", password=_pwd, salt=_salt, iterations=104356 )