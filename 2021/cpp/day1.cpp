#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <days.h>

void day1::part1(std::string file_path) {
    std::ifstream file(file_path);
    std::string line;
    int previous = 0, current = 0, increased = 0, other = 0;
    bool first = true;

    // Reading lines
    if (file.is_open())
    {
        while (getline(file, line))
        {
            // Initializing the system
            if (first)
            {
                previous = std::stoi(line);
                first = false;
            }
            // Checking conditions
            else
            {
                current = std::stoi(line);
                current > previous ? increased++ : other++;
                previous = current;
            }
        }
        std::cout << "Part 1: " << increased << std::endl;
        file.close();
    }
    else std::cout << "Unable to open file" << std::endl;
}

void day1::part2(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);

    // Initializing the array
    std::vector<int> measurements;

    // Filling the array
    std::string line;
    if (file.is_open())
        while (getline(file, line)) {
            measurements.push_back(std::stoi(line));
        }
    else std::cout << "Unable to open file" << std::endl;

    // Initializing variables
    int current = 0;
    std::size_t pos = 1, range = 3;
    int increased = 0, other = 0;
    int previous = std::accumulate(measurements.begin(), measurements.begin() + range, 0);

    // Looping the array
    while (pos < measurements.size()) {

        // Checking condition for the end of the vector
        if ((measurements.size() - pos) < range) {
            range = (measurements.size() - pos);
        }

        // Summing current third
        int current = std::accumulate(measurements.begin() + pos, measurements.begin() + pos + range, 0);

        // Checking condition
        current > previous ? increased++ : other++;
        previous = current;
        pos++;
    }
    std::cout << "Part 2: " << increased << std::endl;
    file.close();
}

void day1::run(std::string folder_path) {
    // Reading inputs
    std::string file_path = folder_path + "\\day1.txt";
    std::cout << "===== Day 1 =====" << std::endl;
    day1::part1(file_path);
    day1::part2(file_path);
}


