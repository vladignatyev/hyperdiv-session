window.hyperdiv.registerPlugin("session", (ctx) => {
    const sessionCookieName = "hyperdiv-session";

    function setSessionCookie(name, value, maxAgeSeconds) {
        window.localStorage.setItem(name, value);
    }

    function getSessionCookie(name) {
        return window.localStorage.getItem(name);
    }

    function deleteSessionCookie(name) {
        window.localStorage.removeItem(name);
    }
    
    ctx.onPropUpdate((propName, propValue) => {
        if (propName === "session_id" && propValue !== "") {
            setSessionCookie(sessionCookieName, propValue, 60 * 60 * 24 * 7);
        }
        if (propName === "clear_session" && propValue === true) {
            deleteSessionCookie(sessionCookieName);
            ctx.updateProp("session_id", "");
            ctx.updateProp("clear_session", false);
        }
    });
    
    if (getSessionCookie(sessionCookieName)) {
        ctx.updateProp("session_id", getSessionCookie(sessionCookieName));
    }
});