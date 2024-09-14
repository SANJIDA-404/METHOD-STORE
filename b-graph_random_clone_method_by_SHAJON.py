import uuid
import random
import requests

#===========[ GIFTED BY SHAJON ]===============#
#===========[ GitHub : SHAJON-404 ]==============#

data = {
    'adid': str(uuid.uuid4()),
    'format': 'json',
    'device_id': str(uuid.uuid4()),
    'email': "8388383838",
    'password': "SHAJON",
    'generate_analytics_claims': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'family_device_id': str(uuid.uuid4()),
    'credentials_type': 'password',
    'source': 'login',
    'error_detail_type': 'button_with_disabled',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'generate_machine_id': '1',
    'currently_logged_in_userid': '0',
    'locale': 'en_GB',
    'client_country_code': 'GB',
    'fb_api_req_friendly_name': 'authenticate'
}

head = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CK7n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Mobile Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-FB-Friendly-Name': 'authenticate',
    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
    'X-FB-Connection-Type': 'unknown',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-FB-HTTP-Engine': 'Liger'
}

url1 = 'https://b-graph.facebook.com/auth/login'

response = requests.post(url1, data=data, headers=head)
print(response.json())
