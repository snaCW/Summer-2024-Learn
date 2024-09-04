strVar = "Hello World"
intVar = 20
floatVar = 20.5
complexVar = 1j
listVar = ["apple", "banana", "cherry"]
tupleVar = ("apple", "banana", "cherry")
rangeVar = range(6)
dictVar = {"name" : "John", "age" : 36}
setVar = {"apple", "banana", "cherry"}
frozensetVar = frozenset({"apple", "banana", "cherry"})
boolVar = True
bytesVar = b"Hello"
bytearrayVar = bytearray(5)
memoryviewVar = memoryview(bytes(5))
noneTypeVar = None

def printTypeOf(var):
    print(type(var))

print("x = \"Hello World\"")
printTypeOf(strVar)

print()
print("x = 20")
printTypeOf(intVar)

print()
print("x = 20.5")
printTypeOf(floatVar)

print()
print("x = 1j")
printTypeOf(complexVar)

print()
print("x = [\"apple\", \"banana\", \"cherry\"]")
printTypeOf(listVar)

print()
print("x = (\"apple\", \"banana\", \"cherry\")")
printTypeOf(tupleVar)

print()
print("x = range(6)")
printTypeOf(rangeVar)

print()
print("x = {\"name\" : \"John\", \age\" : 36}")
printTypeOf(dictVar)

print()
print("x = {\"apple\", \"banana\", \"cherry\"}")
printTypeOf(setVar)

print()
print("x = frozenset({\"apple\", \"banana\", \"cherry\"})")
printTypeOf(frozensetVar)

print()
print("x = True")
printTypeOf(boolVar)

print()
print("x = b\"Hello\"")
printTypeOf(bytesVar)

print()
print("x = bytearray(5)")
printTypeOf(bytearrayVar)

print()
print("x = memoryview(bytes(5))")
printTypeOf(memoryviewVar)

print()
print("x = None")
printTypeOf(noneTypeVar)