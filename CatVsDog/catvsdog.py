import sys

#  Voter class
#  keep stores the animal they want to keep e.g. C1
#  remove is the animal they want to remove e.g. D1
#  evaluated is a flag to check if the voter has been evaluated in the matching algorithm
#  evaluated is required due to recursion of the matching algorithm.
#  to prevent from using the same object twice
#  conflicts is a list of all other votes that would confilct with the vote
#  match is a single vote that is assigned as match to the vote
class Voter:
   def __init__(self, keep, remove):
      self.keep = keep
      self.remove = remove
      self.evaluated = 0
      self.conflicts = []
      self.match = None

#  Function matchVoter is a recursive function that seeks a non-matched vote in the conclicts list
#  for the vote used as argument, in case a possible matching is already matched to another vote
#  it is called again to try to re assign the matches in order to obtain a larger set of matching elements
def matchVoter(voter):
   for confv in voter.conflicts:
      if not confv.evaluated:
         confv.evaluated = 1
         if not confv.match  or matchVoter(confv.match):
            voter.match = confv
            confv.match = voter
            return 1
   return 0

#  Read number of test cases
nTestCases = input()
#  For each test case read numbre of cats, dogs and voters
for _ in range(nTestCases):
   nCats, nDogs, nVoters = map(int, raw_input().split(" "))

   #  Initialize catLovers and dogLovers lists
   catLovers = []
   dogLovers = []

   #  Loop through the input nVoters times to collect each vote
   #  This loop also reads the first letter to place the vote 
   #  either on catLovers or dogLovers
   for _ in range(nVoters):
      keep, remove = raw_input().split(" ")
      newVoter = Voter(keep, remove)
      if keep[0] == 'C':
         if not newVoter in catLovers:
            catLovers.append(newVoter)
      else:
         if not newVoter in dogLovers:
            dogLovers.append(newVoter)

   #  for each cat lover it will fill up the list of conflicting votes
   #  a vote is conflictive if the animal they want to keep is the animal the other wants out
   #  or vice versa
   for cl in catLovers:
      for dl in dogLovers:
         if cl.remove == dl.keep or cl.keep == dl.remove:
            cl.conflicts.append(dl)

   #  For each cat lover it will try to find a doglover with conflict and match them together
   for cl in catLovers:
      for dl in dogLovers:        
         dl.evaluated = 0
      matchVoter(cl)
   m = 0

   #  Count number of matches in the total graph
   for cl in catLovers:
      if cl.match:
         m += 1
   print nVoters - m