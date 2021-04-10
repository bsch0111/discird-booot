import requests

my_app_id = "826617293131218960"

url = 'https://discord.com/api/v8/applications/830152161966030960/commands'

json = {
    "name" : "blep",
    "description": "Send a random adorable animal photo",
    "options": [
        {
            "name" : "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices":[
                {
                    "name":"Dog",
                    "value":"animal_dog"
                },
                {
                    "name":"Cat",
                    "value":"animal_cat"
                },
                {
                    "name":"Penguin",
                    "value":"animal_penguin"
                }
            ]
        },
        {
            "name" : "only_smol",
            "description":"Whether to show only baby animals",
            "type": 5,
            "required":False
        }
    ]
}

headers = {
    "Authorization": "Bot ODMwMTUyMTYxOTY2MDMwOTYw.YHChcg.7kHosmn44j65Y2QYXFoLiW8TVJI"
}

r = requests.post(url, headers=headers, json=json)
print(r)