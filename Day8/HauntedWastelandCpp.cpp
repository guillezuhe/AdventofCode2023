#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

ifstream file("input.txt");
string lr;
string line;
vector<vector<string>> net;


int main(){

    // Read the file
    if (file.is_open()){
        // Read the first line
        getline(file, line);
        lr = line;

        // Read the rest of the lines
        while (getline(file, line)){
            stringstream ss(line);
            string item;
            vector<string> row;

            // Split the line by =, ( and ,
            while (getline(ss, item, '=')){
                string key = item.substr(0, 3);
                row.push_back(key);
                
                // Separate the elements (BBB, CCC)
                getline(ss, item, ',');
                key = item.substr(2, 3);
                row.push_back(key);

                getline(ss, item, ')');
                key = item.substr(1, 3);
                row.push_back(key);
            }
            
            if (!row.empty()) {
                net.push_back(row);
            }
        }
        file.close();

    }
    else {
        std::cout << "Unable to open file" << endl;
    }

    // File read

    bool found = false;
    string target = "AAA";
    int step = 0;
    int index = 0;

    while (!found){
        // Look for target in the net
        if (target == "ZZZ") { // Finished, exit from while loop
            found = true;
            break;
        }
        for (int i = 0; i < net.size(); i++){
            if (net[i][0] == target){
                // Get if we should read the left or right value
                if (lr[index] == 'L') {
                    target = net[i][1];
                }
                else {
                    target = net[i][2];
                }
                
                index = (index + 1) % (lr.length());
                step++;
                break;
            }
        }
    }

    std::cout << "Number of steps: " << step << endl;
    
    return 0;
}
