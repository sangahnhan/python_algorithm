import types

f = lambda x,y,z : x+y+z

print(f)
print(type(f))
print( type(f) == types.LambdaType)
print(dir(type))