
def flatten(d):
    ret_dict = {}
    for k1, v1 in d.items():
        for k2, v2 in v1.items():
            combined_key = k1 + '_' + k2
            ret_dict[combined_key] = v2
    return ret_dict



colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

results_dict = {
'animal_bumblebee': ['yellow', 'black'],
'animal_elephant': ['gray'],
'animal_fox': ['orange', 'white'],
'food_apple': ['red', 'green', 'yellow'],
'food_cheese': ['white', 'orange']
}

assert(flatten(colors) == results_dict)