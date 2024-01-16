#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        Node* next;

        // Default Constructor
        Node(){
            data = 0;
            next = nullptr;
        }

        // Parameterized Constructor
        Node(int data){
            this->data = data;
            this->next = nullptr;
        }
};