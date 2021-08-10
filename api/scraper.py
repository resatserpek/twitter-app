import networkx as nx
import requests
import re
KEY = 'Yz2OYLuBeAkpC93o6zb250NRk'
SECRET = 'LE2lGJZ3a4eEjKycgvYHbYpbQxfvBd5pIcrVf8rYwV89d0wd2'
TOKEN ='AAAAAAAAAAAAAAAAAAAAAGp%2BMwEAAAAAgMV5asR0sjjDd0jGof%2B2Lss%2FL58%3DHDF1XUNJULhWujwC6MewLILf0LKmqfnPl1josxVBJDmhXEb0UW'


headers = {"Authorization": "Bearer " + TOKEN}

#Given a username return id
def get_user_id(name):
    URL = 'https://api.twitter.com/1.1/users/show.json?screen_name=' + name
    resp = any 
    try:
        resp = requests.get(URL, headers=headers)
        print(resp)
        print()
    except requests.exceptions.RequestException as e:
        print('Error')
    data = resp.json()
    return data['id_str']

def get_user_pic(name):    
    URL = 'https://api.twitter.com/1.1/users/show.json?screen_name=' + name
    resp = any 
    try:
        resp = requests.get(URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print('Error')
    data = resp.json()
    print(resp.headers['x-rate-limit-reset'])
    data = re.sub(r'normal', 'bigger', data['profile_image_url_https'])
    return data

def get_user_name(uid):

    URL = 'https://api.twitter.com/2/users/' + uid
    try:
        resp = requests.get(URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print('Error')
    data = resp.json()['data']
    return data['username']

#Given a user name import users that mentioned them
def get_mentions(name):

    userID = ''
    try:
        userID = get_user_id(name)
        print(name, )
    except Exception as e:
        print('Error')
    URL = 'https://api.twitter.com/2/users/' + userID + '/mentions?expansions=author_id'
    try:
        resp = requests.get(URL, headers=headers)
        print(resp.headers)
    except requests.exceptions.RequestException as e:
        (e)
    return resp.json()['data']
#https://api.twitter.com/2/users/by/username/:username
def mention_graph(name):
    #Mentions of the input user and adding it as a node to graph
    G = nx.Graph()
    entity1 = {'name': name, 'pic': get_user_pic(name)}
    G.add_node(name, data=entity1)

    #Mentioning users
    for user in get_mentions(name):
        uName = get_user_name(user['author_id'])
        entity2 = {
            "name": uName,
            "pic": get_user_pic(uName)
        }
        G.add_node(uName, data=entity2)
        G.add_edge(uName, name)

        for u in get_mentions(uName):
            sName = get_user_name(u['author_id'])
            entity3 = {
                "name": sName,
                "pic": get_user_pic(sName)
            }
            G.add_node(sName, data=entity3)
            G.add_edge(sName, uName)
    return G
    