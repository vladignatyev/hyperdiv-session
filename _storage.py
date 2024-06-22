'''
This is a simple storage module that uses pickle to store the session data in a file.
'''
import pickle 

storage = {}


def persist(session_id, state):
    global storage
    storage[session_id] = state
    save()


def connect():
    global storage
    try:
        with open('storage.pickle', 'rb') as f:
            storage = pickle.load(f)
    except FileNotFoundError:
        save()


def save():
    with open('storage.pickle', 'wb') as f:
        pickle.dump(storage, f)


def load(session_id):
    global storage
    return storage.get(session_id, None)


def delete(session_id):
    global storage
    storage.pop(session_id, None)
    save()
