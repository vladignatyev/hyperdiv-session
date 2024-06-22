window.hyperdiv.registerPlugin("session", (ctx) => {
    const sessionCookieName = "hyperdiv-session";
    let temporarySessionCookie = undefined;
    let gdprConfirmed = false;

    function setSessionCookie(value) {
        if (!gdprConfirmed) {
            temporarySessionCookie = value;
            return;
        }
        window.localStorage.setItem(sessionCookieName, value);
    }

    function getSessionCookie() {
        const storedCookie = window.localStorage.getItem(sessionCookieName);
        if (storedCookie) {
            return storedCookie;
        }
        else { 
            return temporarySessionCookie;
        }
    }

    function deleteSessionCookie() {
        window.localStorage.removeItem(sessionCookieName);
    }
    
    ctx.onPropUpdate((propName, propValue) => {
        if (propName === "session_id" && propValue !== "") {
            setSessionCookie(propValue);
        }
        if (propName === "clear_session" && propValue === true) {
            deleteSessionCookie();
            ctx.updateProp("session_id", "");
            ctx.updateProp("clear_session", false);
        }
        if (propName === "gdpr_flag" && propValue === true) {
            gdprConfirmed = true;
            if (temporarySessionCookie) {
                setSessionCookie(temporarySessionCookie);
            }
        }
    });
    
    if (getSessionCookie()) {
        ctx.updateProp("session_id", getSessionCookie());
    }
});