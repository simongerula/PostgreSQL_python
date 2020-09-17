ctn = ()
ctn_list = list(ctn)
for i in range(2):
    var = input(": ")
    ctn_list.append(var)
ctn = tuple(ctn_list)
print(ctn)

print("hola %s") %(ctn_list)