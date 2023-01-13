import requests
import json
# URL= 'http://127.0.0.1:8000/article/1'

# r=requests.get(url=URL)

# data=r.json()

# print(data)

# URL ="http://127.0.0.1:8000/create/"

# data={
#     'title':'Django',
#     'author':'Saru',
#     'email': 'saru@gmail.com',
#     'date':'2020-02-22'
# }
# json_data =json.dumps(data)

# r=requests.post(url=URL,data=json_data)

# data=r.json()
# print(data)

URL="http://127.0.0.1:8000/articleapi/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
        json_data =json.dumps(data)
        r=requests.get(url=URL,data=json_data)
        data =r.json()
        print(data)
# get_data()

def post_data():
    data={
    'title':'Node js',
    'author':'nobody',
    'email': 'nobody@gmail.com',
    'date':'2020-02-22'
    }
    json_data =json.dumps(data)

    r=requests.post(url=URL,data=json_data)

    data=r.json()
    print(data)
# post_data()
def update_data():
    data={
    'id':'4',
    'author':'sakuni',
    'email': 'sakuni@gmail.com',
    'date':'2022-02-22'
    }
    json_data =json.dumps(data)

    r=requests.put(url=URL,data=json_data)

    data=r.json()
    print(data)
# update_data()

def delete_data():
    data={ 'id':'4',}
    json_data =json.dumps(data)

    r=requests.delete(url=URL,data=json_data)

    data=r.json()
    print(data)
delete_data()