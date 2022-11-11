import requests


def login(email, password):
    session = requests.Session()
    response = session.post('https://auth-ac.my.com/auth?lang=en&nosavelogin=0',
                            data={
                                'email': email,
                                'password': password,
                                'continue': 'https://target-sandbox.my.com/auth/mycom?'
                                            'state=target_login=1&ignore_opener=1#email',
                                'failure': 'https://account.my.com/login/'
                            }, headers={'referer': 'https://target-sandbox.my.com'})

    session.get(response.url)

    return session
