def NULL_not_found(object: any) -> int:
    t = str(type(object))

    if object == None:
        print ("Nothing : " + str(object) + " "  + t)
        return 0
    elif isinstance(object, float) and object != object:
        print ("Cheese : " + str(object) + " "  + t)
        return 0
    elif isinstance(object, int) and object == 0:
        print ("Zero : " + str(object) + " "  + t)
        return 0
    elif isinstance(object, str) and object == "":
        print ("Empty : " + str(object) + t)
        return 0
    elif isinstance(object, bool) and object == False:
        print ("Fake : " + str(object) + " " + t)
        return 0
    else:
        print ("Type not found")
        return 1
