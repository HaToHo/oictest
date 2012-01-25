__author__ = 'rohe0002'

# ========================================================================

from oictest.opfunc import *

# ========================================================================

RESPOND = {
    "method": "POST",
    }

AUTHZREQ_CODE = {
    "request": "AuthorizationRequest",
    "method": "GET",
    "args": {
        "request": {"response_type": "code",
                    "scope": ["openid"],
        },
    }
}

AUTHZRESP = {
    "response": "AuthorizationResponse",
    "where": "url",
    "type": "urlencoded",
    }

OPENID_REQUEST_CODE = {
    "request": "OpenIDRequest",
    "method": "GET",
    "args": {"request": {"response_type": "code", "scope": ["openid"]}}
}

OPENID_REQUEST_TOKEN = {
    "request": "OpenIDRequest",
    "method": "GET",
    "args": {"request": {"response_type": "token", "scope": ["openid"]}}
}

# {"OpenIDRequest": {"request", {"response_type":["code","token"]}}}

OPENID_REQUEST_CODE_TOKEN = {
    "request": "OpenIDRequest",
    "method": "GET",
    "args": {"request": {"response_type": ["code","token"],
                         "scope": ["openid"]}}
}

OPENID_REQUEST_CODE_IDTOKEN = {
    "request": "OpenIDRequest",
    "method": "GET",
    "args": {"request": {"response_type": ["code","id_token"],
                         "scope": ["openid"]}}
}

OPENID_REQUEST_TOKEN_IDTOKEN = {
    "request": "OpenIDRequest",
    "method": "GET",
    "args": {"request": {"response_type": ["token","id_token"],
                         "scope": ["openid"]}}
}

OPENID_REQUEST_CODE_TOKEN_IDTOKEN = {
    "request": "OpenIDRequest",
    "method": "GET",
    "args": {"request": {"response_type": ["code", "token", "id_token"],
                         "scope": ["openid"]}}
}

# 2.1.2.1.2
# The User Identifier for which an ID Token is being requested.
# If the specified user is not currently authenticated to the Authorization
# Server, they may be prompted for authenticated, unless the prompt parameter
# in the Authorization Request is set to none. The Claim Value in the request
# is an object containing the single element value.
#"user_id": {"value":"248289761001"}

#OPENID_REQUEST_CODE_21212 = {
#    "request": "AuthorizationRequest",
#    "method": "GET",
#    "args": {
#        "request": {"response_type": "code",
#                    "scope": ["openid"],
#                    "prompt": "none"
#                    },
#        "kw": {
#            "idtoken_claims": {
#                "claims": {"user_id": {"value":"248289761001"}}
#            }
#        }
#    }
#}

ACCESS_TOKEN_RESPONSE = {
    "response": "AccessTokenResponse",
    "where": "body",
    "type": "json"
}

USER_INFO_RESPONSE = {
    "response": "OpenIDSchema",
    "where": "body",
    "type": "json"
}

ACCESS_TOKEN_REQUEST_PASSWD = {
    "request":"AccessTokenRequest",
    "method": "POST",
    "args": {
        "kw": {"authn_method": "client_secret_basic"}
    },
}

ACCESS_TOKEN_REQUEST_CLI_SECRET = {
    "request":"AccessTokenRequest",
    "method": "POST",
    "args": {
        "kw": {"authn_method": "client_secret_post"}
    },
}

USER_INFO_REQUEST = {
    "request":"UserInfoRequest",
    "method": "POST",
    "args": {
        "kw": {"authn_method": "bearer_header"}
    },
}

USER_INFO_REQUEST_BODY = {
    "request":"UserInfoRequest",
    "method": "POST",
    "args": {
        "kw": {"authn_method": "bearer_body"}
    },
}

USER_INFO_REQUEST_BODY_GET = {
    "request":"UserInfoRequest",
    "method": "GET",
    "args": {
        "kw": {"authn_method": "bearer_body"}
    },
}

PROVIDER_CONFIGURATION = {
    "request": "ProviderConfigurationRequest"
}

CHECK_ID_REQUEST = {
    "request": "CheckIDRequest",
    "method": "POST"
}

CHECK_ID_RESPONSE = {
    "response": "IdToken",
    "where": "body",
    "type": "json"
}

PHASES= {
    "login": (AUTHZREQ_CODE, AUTHZRESP),
    "oic-login": (OPENID_REQUEST_CODE, AUTHZRESP),
    "oic-login-token": (OPENID_REQUEST_TOKEN, AUTHZRESP),
    "oic-login-idtoken-token": (OPENID_REQUEST_TOKEN_IDTOKEN, AUTHZRESP),
#    "login-form": ([AUTHZREQ_CODE, LOGIN_FORM], AUTHZRESP),
#    "login-form-approve": ([AUTHZREQ_CODE, LOGIN_FORM, APPROVE_FORM],
#                            AUTHZRESP),
    "access-token-request":(ACCESS_TOKEN_REQUEST_CLI_SECRET,
                            ACCESS_TOKEN_RESPONSE),
    "check-id-request":(CHECK_ID_REQUEST, CHECK_ID_RESPONSE),
    "user-info-request":(USER_INFO_REQUEST_BODY, USER_INFO_RESPONSE)
}


FLOWS = {
    'openid-code': {
        "name": 'Basic OpenID Connect Code flow with authentication',
        "descr": ('Very basic test of a Provider using the authorization code ',
                  'flow. The test tool acting as a consumer is very relaxed',
                  'and tries to obtain an access code.'),
        "sequence": ["login"],
        "endpoints": ["authorization_endpoint"]
    },
    'openid-token': {
        "name": 'Basic OpenID Connect Token flow with authentication',
        "descr": ('Very basic test of a OIC Provider using the token ',
                  'flow. The test tool acting as a consumer is very relaxed',
                  'and tries to obtain an access token.'),
        "sequence": ["oic-login-token"],
        "endpoints": ["authorization_endpoint"]
    },
    'openid-code-userdata': {
        "name": 'Basic Code flow with ID Token and User data',
        "descr": ('Very basic test of a Provider using the authorization code'
                  ' flow, but in addition to retrieve an ID Token,',
                  ' this test flow also tried to obtain user data.'),
        "depends": ['openid-token'],
        "sequence": ["oic-login", "access-token-request", "user-info-request"],
        "endpoints": ["authorization_endpoint", "token_endpoint",
                      "userinfo_endpoint"],
        },
    'openid-token-idtoken-userdata': {
        "name": 'Token flow with ID Token and User data',
        "descr": ('Very basic test of a Provider using the authorization code'
                  ' flow, but in addition to retrieve an ID Token,',
                  ' this test flow also tried to obtain user data.'),
        "depends": ['openid-token'],
        "sequence": ["oic-login-idtoken-token", "user-info-request"],
        "endpoints": ["authorization_endpoint", "userinfo_endpoint"],
    },
    'openid-token-idtoken-check_id': {
        "name": 'OpenID Connect Token flow with check id',
        "descr": ('Very basic test of a OIC Provider using the token ',
                  'flow. The test tool acting as a consumer is very relaxed',
                  'and tries to obtain an ID Token.'),
        "depends": ["openid-token"],
        "sequence": ["oic-login-idtoken-token", "check-id-request"],
        "endpoints": ["authorization_endpoint", "check_id_endpoint"],
        "tests": ["cmp_idtoken"]
    },

}