immutable_var = (1, "barabash", True )
print(immutable_var)
# immutable_var[0] = 2 выдаст ошибку, так как кортеж не поддерживает подобное измененя
mutable_list = ["яблоко", "банан", 10 , False]
mutable_list.append(True)
mutable_list.extend("груша")
mutable_list.remove("банан")
print (mutable_list)
