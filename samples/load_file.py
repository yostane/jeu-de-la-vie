import json

with open('game_of_life_state.json') as json_file:
    state = json.load(json_file)
    print("alive_count", state["alive_count"])
    print("Data", state["data"])
