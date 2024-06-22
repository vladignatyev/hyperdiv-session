import hyperdiv as hd
from hyperdiv_session import session

from _storage import connect, persist, load, delete


def main():
    # Create a session object with a secret key
    sid = session(secret_key="some very secret")

    # Create some view state to store a count
    counter = hd.state(count=0)

    with hd.box(padding=8, gap=2):
        if not sid.is_authenticated():
            hd.text("Not authenticated yet.")
        
            if hd.button("Authenticate").clicked:
                sid.create_new() # create new session
                persist(sid.session_id, counter.count)  # save session into storage
        
        else:
            counter.count = load(sid.session_id)  # load state for given session_id from storage
        
            hd.text("Session demo app.")
            hd.text(sid.session_id)
            hd.text(counter.count)

            if hd.button("Increment").clicked:
                counter.count += 1
                persist(sid.session_id, counter.count)  # update session state in storage

            if hd.button("Log out").clicked:
                sid.clear()
                delete(sid.session_id)

connect()  # open connection to storage or create a new one

hd.run(main)