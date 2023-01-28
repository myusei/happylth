import requests
from bs4 import BeautifulSoup

root_url = 'https://happylth.com'
root_url_2 = 'https://point.happylth.com'
user_id = 'ymaeda24'
user_password = 'Xjr1200@'

session = requests.session()
data = {
    'data[Member][login_id]' : user_id,
    'data[Member][password]' : user_password,
}
session.post(root_url + '/login', data=data)

data = {
    'doActionAfterSSOLogin' : 'true',
}
session.get(root_url + '/sso/6')
session.get(root_url_2 + '/web/nec/home', data=data)

res = session.get(root_url_2 + '/web/nec/inputrecord')
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.find(class_='form'))