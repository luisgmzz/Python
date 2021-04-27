from random import randrange
formula = lambda nivel: nivel**(nivel / 3)

nivel = 1
exp = 0
mensajes = 0


while nivel < 100:
    msgexp = randrange(15, 35)
    mensajes += 1
    exp += msgexp
    if exp > formula(nivel):
        exp -= formula(nivel)
        nivel += 1

print(mensajes)
