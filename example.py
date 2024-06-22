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
                # create new session
                sid.create_new()
                sid.gdpr_flag = True  # GDPR consent

                # save session into storage
                persist(sid.session_id, counter.count)

        else:
            # load state for given session_id from storage
            counter.count = load(sid.session_id)

            hd.text("Session demo app.")
            hd.text(sid.session_id)
            hd.text(counter.count)

            if hd.button("Increment").clicked:
                counter.count += 1

                # update session state in storage
                persist(sid.session_id, counter.count)

            if hd.button("Log out").clicked:
                sid.clear()
                delete(sid.session_id)


connect()  # open connection to storage or create a new one

hd.run(main)
