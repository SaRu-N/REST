import requests
import json

# URL="http://127.0.0.1:8000/articleapi/"
# URL="http://127.0.0.1:8000/clarticleapi/"
URL="http://127.0.0.1:8000/articleapi/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data =json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data =r.json()
    print(data)


def post_data():
    data={
    'title':'java',
    'author':'teacher',
    'email': 'gshow@gmail.com',
    'date':'2022-02-10'
    }
    headers ={'content-Type':'application/json'}
    json_data =json.dumps(data)

    r=requests.post(url=URL,headers=headers,data=json_data)

    data=r.json()
    print(data)

def update_data():
    data={
    'id':'5',
    'title':'Nothing',
    'author':'nody',
    'email': 'nody@gmail.com',
    'date':'2022-02-22'
    }
    json_data =json.dumps(data)

    r=requests.put(url=URL,data=json_data)

    data=r.json()
    print(data)


def delete_data():
    data={ 'id':'4',}
    json_data =json.dumps(data)

    r=requests.delete(url=URL,data=json_data)

    data=r.json()
    print(data)

# get_data()
post_data()
# update_data()
# delete_data()