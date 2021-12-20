from test_data.api_enpoints import *
from test_data.common_data import data_from_server
from test_data.headers import headers_post
from test_data.payloads import *


def response_get_times_today():
    """returns response and status for login with only email password"""
    res = data_from_server("GET", times_today)
    return res.json(), res.status_code


def response_get_times_tomorrow():
    """returns response and status for login with only email password"""
    res = data_from_server("GET", times_tomorrow)
    return res.json(), res.status_code


def test():
    """returns response and status for login with only email password"""
    res = data_from_server("GET", test_url)
    return res.json(), res.status_code


def test_post():
    """returns response and status for login with only email password"""
    res = data_from_server("POST", test_post_url, headers_post, params=create)
    return res.text, res.status_code