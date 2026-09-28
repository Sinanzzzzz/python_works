# Dictionary Functions

d = {"name":"arjun","age":"23"}

d['course']='python'

print(d.keys())

print(d.values())

print(d.items())

print(d["name"])

print(d["age"])

print(d.get("age"))

print(d.get("name"))

(d.update({"place":"ekm","gender":"male"}))
print(d)

d.popitem()

d.pop("age")
print(d)