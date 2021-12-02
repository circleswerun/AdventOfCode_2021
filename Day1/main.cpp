#include <iostream>
#include <fstream>

/*
 * The first order of business is to figure out how quickly the depth increases,
 * just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an
 * ocean current or a fish or something.
 * To do this, count the number of times a depth measurement increases from the previous measurement.
 */

int main(){
    int number;
    int number_temp;
    int counter = 0;

    std::ifstream infile("D:/AdventOfCode_2021/Day1/input.txt");
    infile >> number_temp;
    while (infile >> number) {
        if(number_temp < number) {
            counter++;
        }
        number_temp = number;
    }
    std::cout << counter;
}

