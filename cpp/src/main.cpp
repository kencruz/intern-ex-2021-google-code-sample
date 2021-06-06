#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <vector>

#include "commandparser.h"
#include "videoplayer.h"
#include "helper.h"

int main()
{
    std::cout << "Hello and welcome to YouTube, what would you like to do? "
        "Enter HELP for list of available commands or EXIT to terminate." << std::endl;

    std::string userInput;
    std::string command;
    std::vector<std::string> commandList;
    VideoPlayer vp;
    CommandParser cp = CommandParser(std::move(vp));

    while(std::getline(std::cin, userInput)) {
        if(userInput.empty()){
            std::cout <<  "Please enter a valid command, type HELP for a list of available commands." << std::endl;
        }
        else {
            std::stringstream test(userInput);
            while(std::getline(test, command, ' '))
            {
                command = trim(command);
                commandList.push_back(command);
            }
            std::transform(commandList[0].begin(), commandList[0].end(),commandList[0].begin(), ::toupper);
            if (commandList[0] == "EXIT") {
                break;
            }
            cp.executeCommand(commandList);
            commandList.clear();
        }
    }
    std::cout << "YouTube has now terminated it's execution. Thank you and goodbye!" << std::endl;
}

