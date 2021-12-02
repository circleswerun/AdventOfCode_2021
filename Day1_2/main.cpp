#include <iostream>
#include <fstream>
#include <vector>

/*
 * Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.
 * Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.
*/


int main(){
    int number;
    int first, second, third;
    int sum_prev = 0;
    int sum_current = 0;
    int counter = 0;


    std::ifstream infile("D:/AdventOfCode_2021/Day1/input.txt");

    infile >> first;
    infile >> second;
    infile >> third;

    sum_prev = first + second + third;

    while (infile >> number) {
        if(!infile.is_open() == 0) {
            std::cerr << "File is not open";
        }
        sum_current = sum_prev - first + number;
        std:: cout << "previous: " << sum_prev << " next: " << sum_current << std::endl;

        if (sum_current > sum_prev)
            counter++;

        sum_prev = sum_current;
        first = second;
        second = third;
        third = number;
    }
    infile.close();
    std:: cout << "final answer is: " << counter;
}

