from ..crypto import generate_session_id, verify_session_id


def test_crypto():
    secret = 'secret'
    sid = generate_session_id(secret=secret)
    assert verify_session_id(sid, secret) is True
