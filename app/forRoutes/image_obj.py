from Constellation.dictC import lat_rus_dict, dict_constell, rus_lat_dict

def Image_obj(obj):
    if obj in lat_rus_dict:
        return [lat_rus_dict[obj]+' ('+obj+')']+['\n']+['<a href="/image/'+rus_lat_dict[el]+'">'+el+'</a>' for el in dict_constell[lat_rus_dict[obj]]]
    return [obj]
