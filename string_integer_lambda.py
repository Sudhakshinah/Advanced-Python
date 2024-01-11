data = ["a", 1, 2, 3, "str", "b"]

# lambda function will evaluate the type of every member in the integer and int if member
# is an integer and returns str if the member is a string

result = map(lambda x: f"{x}  int" if type(x) is int else f"{x} str", data)
print(list(result))
