# a = "Abobora"
# b = "Banana"
# c = 3.141592653589397
# string = "a= {}, b= {}, c= {:.2f}".format(a, b, c)
# formato = string.format(a, b, c)

# print(formato)

# //////////////////////////////////////////////////////

# a = "Abobora"
# b = "Banana"
# c = 3.141592653589397
# string = "a = {2:.2f}, b = {1}, c = {0}"
# formato = string.format(a, b, c)

# print(formato)

# //////////////////////////////////////////////////////

a = "Abacaxi"
b = "Banana"
c = 3.141592653589397
string = "a = {fruta1}, b = {fruta2}, c = {numero}"

formato = string.format(
    fruta1=a, fruta2=b, numero=c

)

print(formato)