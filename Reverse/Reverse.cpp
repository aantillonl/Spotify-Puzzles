//============================================================================
// Name        : SpotifyReversePuzzle.cpp
// Author      : Alejandro A
// Version     :
// Copyright   : Your copyright notice
// Description : Reverse puzzle for spotify
//============================================================================

#include <iostream>
#include <math.h>       /* pow */
#include <list>
#include <vector>

using namespace std;

int main() {
	int input, output = 0; 			//	Initialize input
	std::list<bool> inputBitList; 	//	Initialize lit of bits used to store the binary value of input

	cin >> input;					//	Collects input

	//	Create list of bits
	int i = 0;
	while(pow(2,i)<=input){
		inputBitList.push_back(input & (1 << i) ? true : false);
		++i;
	}

	/* Loop in reverse through the list of bits, and accumulate in output variable
	 * Evaluate if the current bit is 1 and if the condition is true
	 * the numeric value of 2 to the power of the current iteration is accumulated in the output variable
	 */
	i = 0;
	for(std::list<bool>::reverse_iterator iterator = inputBitList.rbegin(); iterator != inputBitList.rend(); ++iterator){
		if(*iterator){
			output = output + pow(2, i);
		}
		++i;
	}
	cout << output; // prints Output on screen
}