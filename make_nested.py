

def make_nested(d):
    ret_d = {}
    for k, v in d.items():
        underscore_index = k.find("_")
        k1, k2 = k[:underscore_index], k[underscore_index+1:]
        if not k1 in ret_d:
            ret_d[k1] = {}
        ret_d[k1][k2] = v
    return ret_d


colors = {
'animal_bumblebee': ['yellow', 'black'],
'animal_elephant': ['gray'],
'animal_fox': ['orange', 'white'],
'food_apple': ['red', 'green', 'yellow'],
'food_cheese': ['white', 'orange']
}

result_dict = {
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

assert( make_nested(colors) == result_dict )
