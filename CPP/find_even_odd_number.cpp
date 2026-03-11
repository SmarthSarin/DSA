#include <iostream>
using namespace std;
int main (){ 
    int a;
    cout << "enter a number to check its odd or even\n";
    cin >> a;
    if ( a%2==0){
        cout << "number is even\n";
    }else {
        cout << "number is odd\n";
    }
    return 0;

}