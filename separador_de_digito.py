a = str(input("Numero 1 a 9999:"))
if a >"9999":
    exit()
else:
    if len(a)==1:
        print(f"Unidade:{a[0]}")
    elif len(a) == 2:
       print(f"Unidade:{a[-1]}\nDezena:{a[0]}")
    elif len(a) == 3:
     print(f"Unidade:{a[-1]}\nDezena:{a[1]}\nCentena:{a[0]}")
    elif len(a) == 4:
        print(f"Unidade:{a[-1]}\nDezena:{a[2]}\nCentena:{a[1]}\nMilhar:{a[0]}")
        
