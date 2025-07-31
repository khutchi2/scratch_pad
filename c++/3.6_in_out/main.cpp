#include <iostream>

int main()
{
    std::cout << "Hello world!" << std::endl;

    std::cerr << "Error: All your base are belong to us" << std::endl;
    std::clog << "Logging is for lumberjacks" << std::endl;

    int age;
    std::string name;

    std::cout << "Please type your name and age: " << std::endl;
    // std::cin >> name;
    // std::cin >> age;
    std::cin >> name >> age;
    std::cout << "Hello " << name << "!  You are " << age << "." << std::endl;

    // Data with spaces
    std::string full_name;
    int age2;
    std::cout << "Please type your full name and age: " << std::endl;
    std::getline(std::cin, full_name);
    std::cin >> age2;
    std::cout << "Hello " << full_name << "!  You are " << age2 << "." << std::endl;
}
