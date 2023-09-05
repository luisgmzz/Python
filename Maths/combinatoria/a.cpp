#include <iostream>
#include <string>
using namespace std;

struct nums {
    int data[1000] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};;
    int cont = 10;
};

bool tienen_en_comun(string n, string m) {
    for (char i: n) {
        for (char j: m) {
            if (i == j) return true;
        }
    }
    return false;
}

int main() {
    nums n;
    for (int i = 10; i<1000; i++) {
        for (int j: n.data) {
            if (!tienen_en_comun(to_string(i), to_string(j)))
                n.data[cont]

        }
    }
    return 0;
}
        



