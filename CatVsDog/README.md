# Spotify Zipf's Song puzzle
My solution to spotify's catvsdog puzzle,
https://labs.spotify.com/puzzles/

## Cat Vs Dog
The latest reality show has hit the TV: “Cat vs. Dog”. In this show, a bunch of cats and dogs compete for the very prestigious Best Pet Ever title. In each episode, the cats and dogs get to show themselves off, after which the viewers vote on which pets should stay and which should be forced to leave the show.

Each viewer gets to cast a vote on two things: one pet which should be kept on the show, and one pet which should be thrown out. Also, based on the universal fact that everyone is either a cat lover (i.e. a dog hater) or a dog lover (i.e. a cat hater), it has been decided that each vote must name exactly one cat and exactly one dog.

Ingenious as they are, the producers have decided to use an advancement procedure which guarantees that as many viewers as possible will continue watching the show: the pets that get to stay will be chosen so as to maximize the number of viewers who get both their opinions satisfied. Write a program to calculate this maximum number of viewers.

## Note
I tried to solve this puzzle with c++ with a graph using the Hopcroft Karp algorithm
to find the maximum set of vertex, I could solve the test input but in the server I was getting runtime errors and time limit exceeded errors.
I am not a pro in c++, and i have no doubt it can in deed be solved with that approach, but I tried many many options to fix my code and solve the puzzle, but no success...
Then I tried python and again "time limit exceeded", again tried to optimize my code with no success.
After some time I decided to look arround for other ideas, I do feel guilty about borrowing ideas
from other people, I took a different approach after seeing Abel Pascual's solution.
Finally I managed to solve it. I did not intend to copy his solution I just wanted to try a different approach that could solve the problem in the server. Here are both versions, the successful one, and the Hopcroft Karp approach that returns time limit exceeded.

# In general the working algorithm goes as follows
1. Read number of test cases and votes
2. Store votes in a cat lovers or dog lovers list
3. Identify for each vote all conflicting votes
4. For each vote find one matching vote from all possible conflicting votes.
This last step is called recurrently to find the maximum set of matches.