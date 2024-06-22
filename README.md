# Hyperdiv Session
Adds the support for sessions to Hyperdiv. This is an essential plugin that enables Hyperdiv users to create authorization flows, data persistence across browser sessions and multiuser support.

# Getting Started
1. `pip install hyperdiv-session`
1. Import this plugin `from hyperdiv_session import session`.
2. Initialize this plugin and provide the `secret` string for cookie signing to work.
3. Handle non-authenticated state, create new session after authentication, persist sessions if required.

# Demo app
The `example.py` contains a basic Hyperdiv application that can handle authentication or log in, persist user across browser windows, persist user data to the filesystem and have log out feature. 
```python
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
```

https://github.com/vladignatyev/hyperdiv-session/assets/513940/abdf89f6-9d38-48a3-89d2-2d9166bdfddc


# Notes on implementation
The client-side persistence implemented using `localStorage` (see: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)). We use `signed cookie` as session token.
The cookie signing mechanism is derived from `Django`. We use salted HMAC with `SHA-256` hasher for timestamped cookies. 

# Warning
This is a work-in-progress software! It may lack required features, contain bugs or breaches. Please create new issue for feature request and bug report.

# TODO
- [ ] Test coverage 
- [ ] Make the XSS testing stage
- [ ] Create documentation and samples
- [ ] Implement GDPR compliance
