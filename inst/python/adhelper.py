#!/usr/bin/env python

import ldap

def adauth(address, user_email, password):
    conn = ldap.initialize('ldap://' + address)
    conn.protocol_version = 3
    conn.set_option(ldap.OPT_REFERRALS, 0)

    try:
        result = conn.simple_bind_s(user_email, password)
        response = {'is_authenticated': True, 'message': None}
    except ldap.INVALID_CREDENTIALS:
        response = {'is_authenticated': False, 'message': 'Invalid credentials'}
    except ldap.SERVER_DOWN:
        response = {'is_authenticated': False, 'message': 'Can\'t authenticate - server down'}
    except ldap.LDAPError, e:
        if type(e.message) == dict and e.message.has_key('desc'):
            response = {'is_authenticated': False, 'message': 'LDAP error: ' + e.message['desc']}
        else:
            response = {'is_authenticated': False, 'message': 'LDAP error: ' + e}
    finally:
        conn.unbind_s()

    return response

