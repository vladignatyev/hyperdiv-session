import os
import hyperdiv as hd

from .crypto import generate_session_id, verify_session_id


class session(hd.Plugin):
    _assets_root = os.path.join(os.path.dirname(__file__), "assets")
    _assets = ["*"]

    session_id = hd.Prop(hd.String, "")
    clear_session = hd.Prop(hd.Bool, False)
    gdpr_flag = hd.Prop(hd.Bool, False)


    def __init__(self, secret_key, *, key=None, collect=True, **prop_kwargs):
        super().__init__(key=key, collect=collect, **prop_kwargs)
        self.secret_key = secret_key

    def create_new(self):
        self.session_id = generate_session_id(self.secret_key)

    def is_authenticated(self):
        return self.session_id != 'None' and verify_session_id(self.session_id, self.secret_key)
    
    def is_gdpr_allowed(self):
        return self.gdpr_flag
    
    def clear(self):
        self.clear_session = True
        self.session_id = ""
        self.gdpr_flag = False
