// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <list>
using namespace std;

int main () {
  int n, m;     //  Declare variables. n is number of songs in album. m is number of songs to pick from the album
  string line;  //  variable to store each line of the file through the iterations
  
  
  
  cin >> line;
  //  Extract n from first line, is a substring starting from the first char
  //  to the point where it finds a space, and m similar, from space to end
  n = stoi(line.substr(0, line.find(" "))); 
  m = stoi(line.substr(line.find(" ") , line.size()- line.find("")));

  //  Now that n and m are known we can initialize f and q vectors, which will
  //  store the information of frequency palyed and quality
  //  names is a vector that stores the names of the songs
  int f[n];
  double q[n];
  string names[n];

  //  Loop through the rest of the lines in the file to read the frequency,
  //  names, and compute the quality which is normalized to the freq of the frist track.
  for (int i=0; i<n; ++i)
  {
    cin >> line;
    f[i] = stoi(line.substr(0, line.find(" ")));
    names[i] = line.substr(line.find(" ") , line.size()- line.find(""));
    q[i] = (double)f[i]/(double)f[0]*(i+1);
  }

  //  Initialize imax, vector that will store the index of the best songs
  //  max is a value that will hold the max value during iterations
  //  The main idea is to iterate through the vectors m times, which as many songs we
  //  have to pick. and evaluate if the quality is greater than var max, then we
  //  assign the q of that track to max, and store 
  int imax[m];
  double max;
  for(int i=0;i<m;++i){
  max =0;
    for(int j=0;j<n;++j){
      if(q[j] >= max && (i == 0 || q[imax[i-1]]>q[j])){
        imax[i]= j;
        max = q[j];
      }
    }
  }

  for(int i=0;i<m;++i){
    cout<<names[imax[i]]<<"\n";
  }       

  return 0;
}