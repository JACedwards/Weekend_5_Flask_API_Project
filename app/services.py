import requests as r

def getabilities():
    able_dict = {}

    for i in range(1,21):
        data_able = r.get('https://pokeapi.co/api/v2/pokemon/' + str(i))
        # print(data)
        if data_able.status_code == 200:
            # print('test')
            data_able = data_able.json()
        else:
            return "Data source not responding"

        name_able = data_able['forms'][0]['name']
        # # print(name_name)
        ability =  data_able['abilities'][0]['ability']['name']
        # print(ability)   
        able_dict[name_able]=ability
        #print(able_dict)

        x = sorted(able_dict.items(), key =
             lambda kv:(kv[1], kv[0]))
        able_dict_sorted = dict(x)

    # print(able_dict_sorted)
    return able_dict_sorted
 
