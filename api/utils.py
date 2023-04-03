def genfunc(name):
    return "@app.post(\"/api/" + name + "\") \nasync def " + name + "(payload: dict= Body(...)):\n     return {\"value\": \"Error: not implemented yet\"}"


print(genfunc("button"))
print(genfunc("keypad"))
print(genfunc("simon"))
print(genfunc("whosonfirst"))
print(genfunc("memory"))
print(genfunc("morse"))
print(genfunc("compwires"))
print(genfunc("wireseq"))
print(genfunc("maze"))
print(genfunc("knobs"))