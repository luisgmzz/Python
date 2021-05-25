def show_indices(equation: str):
    equation = equation.split(" ")

    for i in range(len(equation)):
        if equation[i] == "x":
            if not equation[i-1].isdigit():
                equation.insert(i, "1")
                continue

    return "".join(equation).split("=")


def classify(equation: list):
    classificated = {"x0": 0, "n0": 0, "x1": 0, "n1": 0}

    assistant = ""

    for i in range(2):
        half = equation[i].strip()
        for j in range(len(half)):
            num = half[j]
            if num.isdigit():
                assistant += num
                if j != len(half) - 1:
                    if half[j+1].isdigit():
                        continue
                    elif half[j+1] == "x":
                        classificated["x" + str(i)] += int(assistant)
                        assistant = ""
                    else:
                        classificated["n"+str(i)] += int(assistant)
                        assistant = ""
                else:
                    classificated["n" + str(i)] += int(assistant)
                    assistant = ""
            elif num == "-":
                assistant += num

    return classificated


def simplify(equation: dict):
    simplified = [equation["x0"] - equation["x1"],
                  equation["n0"] - equation["n1"]]

    return simplified


def get_equation(equation: str):
    return simplify(classify(show_indices(equation)))


def calculate(equation: list):
    a = list[0]
    b = list[1]
    return -b/a
