print(10*"=")
print("Media")
print(10*"=")
soma_notas = pri = seg = 0
for notas in range(1,3):
    nota = float(input(f"Digite Sua {notas} nota:"))
    soma_notas += nota/2
    if notas == 1:
        pri = nota
    elif notas == 2:
        seg = nota
print(f"Sua Primeira Nota foi {pri:.1f}\nSua Segunda Nota foi {seg:.1f}\nLogo sua Media foi {soma_notas:.1f}")