#include <cmath>
#include <vector>
#include <string>

// Convert a binary number to decimal
long long bin_to_dec(long long bin) {
    long long dec = 0, i = 0, rem;
    while (bin != 0) {
        rem = bin % 10;
        bin /= 10;
        dec += rem * pow(2, i);
        ++i;
    }
    return dec;
}

// Convert a decimal number to binary
long long dec_to_bin(long long dec) {
    long long bin = 0;
    int rem, i = 1;
    while (dec != 0) {
        rem = dec % 2;
        dec /= 2;
        bin += rem * i;
        i *= 10;
    }
    return bin;
}

// Check the highest frequency between 1s and 0s in a list containing binary numbers
char check_binaries_frequency(std::vector<std::string> vect, int num_size, int pos) {
    std::vector<int> ones;
    std::vector<int> zeros;
    for (int i = 0; i < num_size; i++) {
        ones.push_back(0);
        zeros.push_back(0);
    }
    for (int i = 0; i < vect.size(); i++) {
        std::string elem = vect[i];
        for (int i = 0; i < num_size; i++) {
            char c = elem[i];
            if (c == '0')
                zeros[i]++;
            else if (c == '1')
                ones[i]++;
        }
    }
    if (ones[pos] > zeros[pos]) {
        return '1';
    }
    else if (ones[pos] < zeros[pos]) {
        return '0';
    }
    else {
        return '-1'; // Equal frequency
    }
}