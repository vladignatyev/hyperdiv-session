import hmac
import hashlib
import time
import os

# This is the salt used to sign the session id
session_salt = "io.hyperdiv.session"


def random_string():
    random_bytes = os.urandom(64)
    return hashlib.sha256(random_bytes).hexdigest()


def force_bytes(s):
    if isinstance(s, bytes):
        return s
    if isinstance(s, memoryview):
        return bytes(s)
    return str(s).encode("utf-8", "strict")


def sign(string, secret, salt=session_salt):
    key_salt = force_bytes(salt)
    secret = force_bytes(secret)
    key = hashlib.sha256(key_salt + secret).digest()
    return hmac.new(key, msg=force_bytes(string), digestmod=hashlib.sha256).hexdigest()


def verify(string, signature, secret, salt=session_salt):
    return hmac.compare_digest(force_bytes(signature), force_bytes(sign(string, secret, salt)))


def generate_session_id(secret, sep="."):
    timestamp = int(time.time())
    random_sid = str(random_string()) + sep + str(timestamp)
    signature = sign(random_sid, secret)

    return f"{random_sid}{sep}{signature}"


def verify_session_id(session_id, secret):
    try:
        session_id, timestamp, signature = session_id.split(".")
        return verify(session_id + "." + timestamp, signature, secret)
    except ValueError:
        return False
