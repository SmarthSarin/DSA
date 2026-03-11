#include <iostream>
using namespace std;

int main() {
    double a, c;
    char b;

    cout << "Welcome to the calculator" << endl;
    
    // Input first number
    cout << "ENTER FIRST NUMBER: ";
    cin >> a;

    // Input the operator
    cout << "Choose an operator (+, -, *, /): ";
    cin >> b;

    // Input second number
    cout << "ENTER SECOND NUMBER: ";
    cin >> c;

    // Perform calculation based on the operator
    cout << "Result: ";
    switch(b) {
        case '+':
            cout << a + c;
            break;
        case '-':
            cout << a - c;
            break;
        case '*':
            cout << a * c;
            break;
        case '/':
            if (c != 0)
                cout << a / c;
            else
                cout << "Error: Division by zero!";
            break;
        default:
            cout << "Error: Invalid operator!";
            break;
    }

    cout << endl;
    return 0;
}
