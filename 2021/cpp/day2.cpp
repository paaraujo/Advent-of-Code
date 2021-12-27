#include <iostream>
#include <fstream>
#include <string>
#include <days.h>

void day2::part1(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);
    std::string line, command, delimiter = " ";
    int pos, input, horizontal = 0, depth = 0;

    if (file.is_open()) {
        while (getline(file, line))
        {
            // Extracting commands and inputs
            pos = line.find(delimiter);
            command = line.substr(0, pos);
            input = std::stoi(line.substr(pos, line.length()));
            
            // Applying commands
            if (command.compare("forward") == 0) {
                horizontal += input;
            }
            else if (command.compare("down") == 0) {
                depth += input;
            }
            else if (command.compare("up") == 0) {
                depth -= input;
            }
        }
        std::cout << "Part 1: " << horizontal * depth << std::endl;
        file.close();
    }
    else std::cout << "Unable to open file" << std::endl;
}

void day2::part2(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);
    std::string line, command, delimiter = " ";
    int pos, input, horizontal = 0, depth = 0, aim = 0;

    if (file.is_open()) {
        while (getline(file, line))
        {
            // Extracting commands and inputs
            pos = line.find(delimiter);
            command = line.substr(0, pos);
            input = std::stoi(line.substr(pos, line.length()));

            // Applying commands
            if (command.compare("forward") == 0) {
                horizontal += input;
                depth += (aim * input);
            }
            else if (command.compare("down") == 0) {
                aim += input;
            }
            else if (command.compare("up") == 0) {
                aim -= input;
            }
        }
        std::cout << "Part 1: " << horizontal * depth << std::endl;
        file.close();
    }
    else std::cout << "Unable to open file" << std::endl;

}

void day2::run(std::string folder_path) {
    // Reading inputs
    std::string file_path = folder_path + "\\day2.txt";
    std::cout << "===== Day 2 =====" << std::endl;
    day2::part1(file_path);
    day2::part2(file_path);
}