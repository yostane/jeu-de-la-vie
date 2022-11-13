import json

data = [x for x in range(10)]
dict = {'data': data, 'alive_count': 10}
json = json.dumps(dict)

with open("game_of_life_state.json", "w") as json_file:
    json_file.write(json)
