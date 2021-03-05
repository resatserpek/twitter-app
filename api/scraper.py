from networkx.readwrite import json_graph
import requests
import networkx as nx
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
    except requests.exceptions.RequestException as e:
        print (resp)
    data = resp.json()
    return data['id_str']

def get_user_pic(name):    
    URL = 'https://api.twitter.com/1.1/users/show.json?screen_name=' + name
    resp = any 
    try:
        resp = requests.get(URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print (resp)
    data = resp.json()
    data = re.sub(r'normal', 'bigger', data['profile_image_url_https'])
    return data

def get_user_name(uid):

    URL = 'https://api.twitter.com/2/users/' + uid
    try:
        resp = requests.get(URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print (e)
    data = resp.json()['data']
    return data['username']

#Given a user name import users that mentioned them
def get_mentions(name):

    userID = ''
    try:
        userID = get_user_id(name)
    except Exception as e:
        print (e)
    URL = 'https://api.twitter.com/2/users/' + userID + '/mentions?expansions=author_id'
    try:
        resp = requests.get(URL, headers=headers)
    except requests.exceptions.RequestException as e:
        print (e)
    return resp.json()['data']

def get_social_circle(name):
    mentions = get_mentions(name)
    entity = {
        "name": name,
        "pic": get_user_pic(name),
        "mentions" : get_secondary(name, mentions)
    }
    return entity
    

def get_secondary(name, mentions):
    temp = []
    for user in mentions:
        user_name = get_user_name(user['author_id'])
        if user_name != name:
            entity = {
                "name": user_name,
                "pic": get_user_pic(user_name),
                "mentions" : get_third(name, get_mentions(user_name))
            }
            temp.append(entity)
    return temp
def get_third(name, mentions):
    temp = []
    for user in mentions:
        user_name = get_user_name(user['author_id'])
        if user_name != name:
            entity = {
                "name": user_name,
                "pic": get_user_pic(user_name),
                "mentions" : []
            }
            temp.append(entity)
    return temp

def mention_tree(name):
    mentions = get_mentions(name)
    tree = {}
    temp = []
    for user in mentions:
        user_name = get_user_name(user['author_id'])
        if user_name != name:
            temp.append(user_name)
    
    tree[name] = temp  

    for user in temp:
        mentions = get_mentions(user) 
        temp = []
        for u in mentions:
            u_name = get_user_name(u['author_id'])
            if u_name != user:
                temp.append(u_name)
            tree[user] = temp
    return tree

def mention_graph(name):
    G = nx.Graph()
    G.add_node(name)

    mentions = get_mentions(name)
    temp = []
    for user in mentions:
        user_name = get_user_name(user['author_id'])
        if user_name != name:
            temp.append(user_name)
    for i in temp:
        G.add_edge(name, i)

        mentions = get_mentions(i) 

        for u in mentions:
            user_name = get_user_name(u['author_id'])
            G.add_node(user_name)
            G.add_edge(i,user_name)

    return G