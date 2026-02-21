#include <iostream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cout << "Invalid arguments\n";
        return 1;
    }

    float cpu = stof(argv[1]);
    float memory = stof(argv[2]);

    cout << "Processed Data:\n";
    cout << "CPU Usage: " << cpu << "%\n";
    cout << "Memory Usage: " << memory << "%\n";

    if (cpu > 85) {
        cout << "⚠ High CPU Usage!\n";
    }

    if (memory > 80) {
        cout << "⚠ High Memory Usage!\n";
    }

    return 0;
}