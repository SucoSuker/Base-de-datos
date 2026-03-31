U = input()
C = input()
i = 3
while i > 0:
    if C == "123":
        print("Bienvenid@")
        i = 0
    else:
        print("Error, Tienes ", i - 1, "intentos ")
        i = i -1
        if i !=0:
        	C = input()
        else:
        	print("Usuario bloqueado")
