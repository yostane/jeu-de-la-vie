import json

data = [[y + x * 10 for y in range(4)] for x in range(5)]
dict = {'data': data, 'alive_count': 10}
json = json.dumps(dict)

with open("game_of_life_state.json", "w") as json_file:
    json_file.write(json)
