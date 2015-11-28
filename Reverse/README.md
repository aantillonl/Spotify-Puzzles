# Spotify Zipf's Song puzzle
My solution to spotify's monkeys puzzle,
https://labs.spotify.com/puzzles/

## Description of the algorithm
###1. Initialize variables to be used later on the program:
	n = number of songs in the album
	m = number of top songs to take from the album
	Notice that there are more variables and arrays initialized later, but it is because they are
	in function of n and m, wich are input, so input must be read before being able to inizialize
	the rest of the variables.
###2. Define read input and define n and m
###3. Initialize the rest of variables:
	f[n]= array of size n, which will contain the times each song was listened
	q[n]= array of size n, which will contain the quality for each song.
###4. Read input for each song and calculate quality of each
	Notice that the expression to calculate q is q =(f[i]f[0])*i
###5. Select top songs 
	Next we proceed to take m top songs by looping through the array and comparing the quality
	of each song with an variable called max, which stores the previous maximum (and in each iteration is set to 0)