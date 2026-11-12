#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int *p1 = &a;
    int *p2 = &b;

    cout << "Before swapping: " << endl;
    cout << "a = " << a << ", b = " << b << endl;

    // Swapping using pointers
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;

    cout << "After swapping: " << endl;
    cout << "a = " << a << ", b = " << b << endl;

    int *ptr = &a; // Pointer to a
    cout << "Value of a using pointer: " << *ptr << endl;

    ptr++; // Incrementing the pointer to point to the next integer (b)
    cout << "Value of b using pointer: " << *ptr << endl;

    return 0;
}