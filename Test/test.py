notasMusicales = ["do", "re", "mi"]
notas = '-'.join(notasMusicales)
print(notas)

# ---------------------------------

strMeses1 = "Meses = {}, {}, {}".format("Enero", "Febrero", "Marzo")
strMeses2 = "Meses = {2}, {0}, {1}".format("Enero", "Febrero", "Marzo")
strMeses3 = "Meses = {feb}, {mar}, {ene}".format(ene = "Enero", feb = "Febrero", mar = "Marzo")
print(strMeses1)
print(strMeses2)
print(strMeses3)

# ---------------------------------------------------------------------------------------------

frase = "Aprendiendo a programar en Python"
print(frase[1:7] + frase[9:11])

# -----------------------------------------

numsImpares = []
for x in range(1, 10):
    if x % 2 != 0:
        numsImpares.append(x)

print(str(numsImpares))

# ---------------------------

cont = 0
while (cont < 5):
    print("Iteracion {}".format(cont + 1))
    cont += 1

# ---------------------------

def saludo(nombre = "Keni Galindo"):
    print("Hola " + nombre + ", bienvenid@.")

saludo("Fernando")
saludo()

# -------------------------------------------

def suma(*args):
    total = 0
    for a in args:
        total += a

print(suma(1, 2, 3, 4, 5))