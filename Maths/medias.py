from statistics import mean

def sele():
    #Lengua, Historia, Mates, Fisica, Dibujo, Filosofia, TIC, Ciudadania, Ingels, EF
    first_evaluation = mean([10, 10, 8, 8, 8, 9, 8, 10, 9, 9])
    #second_evaluation = mean([8, 9, 6, 8, 10, 6, 4, 8, 8, 7, 8])
    #third_evaluation = mean([])

    #general = mean([8, 10, 7, 8, 10, 8, 7, 9, 8, 8, 8])
    print(first_evaluation)

def uni1():
    notas_segundo_cuatri = {
        "fisca": 6.4,
        "algebra": 7.9,
        "mdl": 6.04,
        "compu": 9,
        "progra": 10
    }
    primer_cuatri = 8
    for i in range (5, 11):
        print(i)
        notas_segundo_cuatri["progra"] = i
        notas_pairs = list(notas_segundo_cuatri.items())
        notas = []
        for j in notas_pairs:
            notas.append(j[1])
        segundo_cuatri = mean(notas)
        print("MEDIA: ", segundo_cuatri)

uni1()