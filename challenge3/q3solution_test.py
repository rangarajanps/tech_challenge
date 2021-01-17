from q3solution import get_from_nested

dictdata = {"a":{"b":{"c":"d"}}}
print("Object : ", dictdata)

print("key: a, value: ", get_from_nested(dictdata,"a","/"))
print("key: a/b, value: ", get_from_nested(dictdata,"a/b","/"))
print("key: a/b/c, value: ", get_from_nested(dictdata,"a/b/c","/"))
print("key: x, value: ", get_from_nested(dictdata,"x","/"))
print("key: a/c, value: ", get_from_nested(dictdata,"a/c","/"))
print("key: a/b/e, value: ", get_from_nested(dictdata,"a/b/e","/"))

print("\n")
dictdata = {"x":{"y":{"z":"a"}}}
print("Object : ", dictdata)

print("key:  x/y/z, value: ", get_from_nested(dictdata,"x/y/z","/"))
