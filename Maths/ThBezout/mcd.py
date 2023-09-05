# Implementado por algoritmo de euclides
def mcd(a: int, b: int):
    if b == 0:
        mcd.table.append([a, b, None, None])
        table = {
            "mcd": a,
            "iterations": len(mcd.table) - 1,
            "table": mcd.table
        }
        mcd.table = []
        return table 

    mcd.table.append([a, b, a%b, a//b])
    return mcd(b, a%b)
mcd.table = [] 


if __name__ == "__main__":
    def format_matrix(matrix):
        string = "["
        for i in matrix:
            string += "  \n["
            for j in i:
                string += f" {j}"
                if j != i[-1]:
                    string += ","

            string += " ]"
        string += "\n]"
        print(string)
    
    print(mcd(11, 3))