#include <iostream>
#include <fstream>
#include <string>
#include <days.h>

void day2::part1(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);
    std::string line;
    if (file.is_open())
        file.close();
    else std::cout << "Unable to open file" << std::endl;
}

void day2::part2(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);
    std::string line;
    if (file.is_open())
        file.close();
    else std::cout << "Unable to open file" << std::endl;

}

void day2::run(std::string folder_path) {
    // Reading inputs
    std::string file_path = folder_path + "\\day1.txt";
    std::cout << "===== Day 2 =====" << std::endl;
    day2::part1(file_path);
    day2::part2(file_path);
}