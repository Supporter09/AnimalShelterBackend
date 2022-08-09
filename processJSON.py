import json
result = {}
with open('D:\Code\AnimalShelterBackend\Datas.json', encoding="utf8") as f:
    data = json.loads(f.read())

    for key, value in data.items():
        value['name'] = str(key)
        result[key] = value

with open('result.json', 'w') as fp:
    json.dump(result, fp)