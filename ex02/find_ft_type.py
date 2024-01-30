def all_thing_is_obj(obj: any) -> int:
    t = str(type(obj))

    if 'str' in t:
        print (obj + " is in the kitchen : " + t)
    elif isinstance(obj, object) and not 'int' in t:
        print (t.split("'")[1].capitalize() + " : " + t)
    else:
        print ("Type not found")

    return 42

