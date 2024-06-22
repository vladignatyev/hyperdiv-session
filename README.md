# Hyperdiv Session
Adds the support for sessions to Hyperdiv. This is an essential plugin that enables Hyperdiv users to create authorization flows, data persistence across browser sessions and multiuser support.

# Getting Started
1. Import this plugin.
2. Initialize this plugin and provide the `secret` string for cookie signing to work.
3. Handle non-authenticated state, create new session after authentication, persist sessions if required.

The `example.py` contains a basic Hyperdiv application that can handle authentication or log in, persist user across browser windows, persist user data to the filesystem and have log out feature. 

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
