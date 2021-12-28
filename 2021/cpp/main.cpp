
#include <iostream>
#include <fstream>
#include <string>
#include <days.h>

int main()
{
    // Getting the path of the directory containing the
    // input files with well-defined names
    std::string folder_path;
    std::cout << "Path to the input directory: ";
    std::getline(std::cin, folder_path);

    // Calling days
    day1::run(folder_path);
    day2::run(folder_path);
    day3::run(folder_path);
}
