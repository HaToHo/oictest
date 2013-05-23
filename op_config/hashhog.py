#!/usr/bin/env python

import json

info = {
    "features": {
        "registration":True,
        "discovery": True,
        "session_management": False,
    },
    "client": {
        "redirect_uris": ["https://hashog.umdc.umu.se/authz_cb"],
        "contact": ["hans.horberg@umu.se"],
        "application_type": "web",
        "application_name": "OIC test tool",
    },
    "provider": {
        "version": { "oauth": "2.0", "openid": "3.0"},
        "dynamic": "https://hashog.umdc.umu.se:8088/",
    },
    "interaction": [
        {
            "matches": {
                "url": "https://hashog.umdc.umu.se:8088/authorization",
            },
            "page-type": "login",
            "control": {
                "type": "form",
                "set": {"login":"diana","password": "krall"}
            }
        }
    ]
}

print json.dumps(info)
