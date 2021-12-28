#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <days.h>
#include <utils.h>

#define N 12

void day3::part1(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);
    std::string line, command, delimiter = " ";
    std::vector<std::string> vect;

    // Reading inputs and getting frequency per position
    if (file.is_open()) {
        while (getline(file, line))
        {
            vect.push_back(line);
        }
        file.close();
    }
    else std::cout << "Unable to open file" << std::endl;

    // Building binaries
    std::string gamma_rate = "";
    std::string epsilon_rate = "";

    for (int i = 0; i < N; i++) {
        if (check_binaries_frequency(vect, N, i) == '1') {
            gamma_rate += "1";
            epsilon_rate += "0";
        } else if (check_binaries_frequency(vect, N, i) == '0'){
            gamma_rate += "0";
            epsilon_rate += "1";
        }
        else {
            // Equal frequency: do nothing!
        }
    }

    // Converting numbers to binaries
    long long gr_bin = std::stoll(gamma_rate);
    long long er_bin = std::stoll(epsilon_rate);

    long long gr_dec = bin_to_dec(gr_bin);
    long long er_dec = bin_to_dec(er_bin);

    std::cout << "Part 1: " << gr_dec * er_dec << std::endl;
}

void day3::part2(std::string file_path) {
    // Reading inputs
    std::ifstream file(file_path);
    std::string line; 
    std::vector<std::string> O2;
    std::vector<std::string> CO2;

    // Reading inputs and getting frequency per position
    if (file.is_open()) {
        while (getline(file, line))
        {
            O2.push_back(line);
            CO2.push_back(line);
        }
        file.close();
    }
    else std::cout << "Unable to open file" << std::endl;

    // O2
    int pos = 0;
    while (O2.size() > 1 && pos < N) {
        // Most frequent number
        char c = check_binaries_frequency(O2, N, pos);
        if (c == '-1')
            c = '1';
          
        // Removing numbers that do not comply with the rule
        for (int i = O2.size() - 1; i >= 0; i--) {
            std::string current = O2[i];
            if (current[pos] != c)
                O2.erase(O2.begin() + i);
        }
        pos++;
    }

    // Getting rate in decimal
    std::string O2_rate = "";
    for (int i = 0; i < N; i++)
        O2_rate += O2[0][i];
    long long O2_bin = std::stoll(O2_rate);
    long long O2_dec = bin_to_dec(O2_bin);

    // CO2
    pos = 0;
    while (CO2.size() > 1 && pos < N) {
        // Least frequent number
        char c = check_binaries_frequency(CO2, N, pos);
        if (c == '1' || c == '-1')
            c = '0';
        else if (c == '0')
            c = '1';
        
        // Removing numbers that do not comply with the rule
        for (int i = CO2.size() - 1; i >= 0; i--) {
            std::string current = CO2[i];
            if (current[pos] != c)
                CO2.erase(CO2.begin() + i);
        }
        pos++;
    }

    // Getting rate in decimal
    std::string CO2_rate = "";
    for (int i = 0; i < N; i++)
        CO2_rate += CO2[0][i];
    long long CO2_bin = std::stoll(CO2_rate);
    long long CO2_dec = bin_to_dec(CO2_bin);

    std::cout << "Part 2: " << O2_dec * CO2_dec << std::endl;
}

void day3::run(std::string folder_path) {
    // Reading inputs
    std::string file_path = folder_path + "\\day3.txt";
    std::cout << "===== Day 3 =====" << std::endl;
    day3::part1(file_path);
    day3::part2(file_path);
}