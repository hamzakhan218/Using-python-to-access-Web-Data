import json
data='''{
    "name":"Hamza",
    "phone":{
        "type":"intl",
        "number":"+92 3435156497"
        },
    "email":{
        "hide":"yes"
        }
    }    '''

info=json.loads(data)
print('Name: ',info["name"])
print("Phone Number",info["phone"]["type"],info["phone"]["number"])
print("Email: ",info["email"]["hide"])