def get_from_nested(dict, keystr,delim):    
    try:
        for key in keystr.split(delim):
            dict = dict[key]
        return dict
    except (KeyError, IndexError):
        return "No Match Found"

if __name__ == '__main__':
    dictdata = {"a":{"b":{"c":"d"}}}
    print("Object : ", dictdata)
    key = input("Enter the key : ")
    delim = input("Enter the delimitor : ")
    print("value : " , get_from_nested(dictdata,key,delim))
