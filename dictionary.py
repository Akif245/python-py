# Dictonary is a combination of keys and values
name={"Akif":'human',"spoon":123}
print(name["Akif"])
# or
print(name.get("Akif"))
print(name.values())
print(type(name))
name.popitem()
print(name)
del name

