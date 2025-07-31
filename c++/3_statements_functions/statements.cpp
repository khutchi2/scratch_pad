#include <iostream>

int add_numbers(int first_number, int second_number)
{
    int sum = first_number + second_number;
    return sum;
}

int main(int argc, char **argv)
{
    int first_number = 12;
    int second_number = 9;

    int sum = first_number + second_number;
    int sum_2 = add_numbers(5, 15);

    std::cout << "The sum of the two numbers is: " << sum << std::endl;
    std::cout << "The sum of the other two numbers is: " << sum_2 << std::endl;
    std::cout << "The sum of another two numbers is: " << add_numbers(21, 3) << std::endl;

    return 0;
}