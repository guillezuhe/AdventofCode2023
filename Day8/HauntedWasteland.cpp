// This is a translation of the HauntedWasteland.py file into C++.

#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(){
    string line;
    ifstream file("input_easy.txt");
    vector<string> data;
    vector<vector<string>> net;

    string lr;

    // Read de file and store the data in a vector
    if (file.is_open()){
        while (getline(file, line)){
            data.push_back(line);
        }
        file.close();
    }
    else cout << "Unable to open file";
    

    lr = data[0];
    cout << "The data is: " << lr << endl;

    // Remove the firs two lines of data
    data.erase(data.begin());
    data.erase(data.begin());

    for (int i = 0; i < data.size(); i++){
        cout << data[i] << endl;
    }

    // The rest of the lines are the instructions










    return 0;
}
