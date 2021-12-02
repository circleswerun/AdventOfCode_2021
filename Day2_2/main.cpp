#include <iostream>
#include <fstream>

int main() {
    std::ifstream infile("D:\\AdventOfCode_2021\\Day2\\data.txt");

    std::string direction;
    int x = 0, y = 0, aim = 0;
    int move;

    while (infile >> direction >> move){
        if(!infile.is_open()){
            std::cerr << "file closed unexpectedly" << std::endl;
        }
        if(direction.compare("up") == 0){
            aim -= move;
        }
        else if(direction.compare("down") == 0){
            aim += move;
        }
        else if(direction.compare("forward") == 0){
            x += move;
            y += (aim * move);
        }
        else{
            std::cerr << "invalid direction" << std::endl;
        }
    }
    infile.close();
    std::cout << "final position of submarine: " << x << "," << y << std::endl;
    std::cout << "final horizontal position multipled by final depth: " << x * y << std::endl;
}
