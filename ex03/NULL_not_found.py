def NULL_not_found(obj: any) -> int:
    t = str(type(obj))

    if obj == None:
        print ("Nothing : " + str(obj) + " "  + t)
        return 0
    elif isinstance(obj, float) and obj != obj:
        print ("Cheese : " + str(obj) + " "  + t)
        return 0
    elif isinstance(obj, int) and obj == 0:
        print ("Zero : " + str(obj) + " "  + t)
        return 0
    elif isinstance(obj, str) and obj == "":
        print ("Empty : " + str(obj) + t)
        return 0
    elif isinstance(obj, bool) and obj == False:
        print ("Fake : " + str(obj) + " " + t)
        return 0
    else:
        print ("Type not found")
        return 1
