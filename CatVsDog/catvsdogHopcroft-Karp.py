import sys
import pdb
from sets import Set
class Voter:
   def __init__(self, keep, remove, id):
      self.id = id
      self.keep = keep
      self.remove = remove
      self.isFree = 1
      self.evaluated = 0
   def __eq__(self, other): 
      return self.keep == other.keep and self.remove == other.remove
   def __ne__(self, other):
      return self.keep != other.keep and self.remove != other.remove
class Conflict:
   def __init__(self, cl, dl):
      self.cl = cl
      self.dl = dl
   def __eq__(self, other): 
      return self.cl.id == other.cl.id and self.dl.id == other.dl.id
   def __ne__(self, other):
      return self.cl.id != other.cl.id or self.dl.id != other.dl.id
   def __hash__(self):
      return int(str(self.cl.id) + str(self.dl.id))
def findUnmatched(unmatched, cl, alternating):
   for v in unmatched:
      if v.cl == cl:
         alternating.append(v)
         return 1
   return 0

def findMatched(match, dl, alternating):
   for v in match:
      if v.dl == dl:
         alternating.append(v)
         return 1
   return 0     

nTestCases = input()
for _ in range(nTestCases):
   nCats, nDogs, nVoters = map(int, raw_input().split(" "))

   catLovers = []
   dogLovers = []
   catLoversConflict = []
   dogLoversConflict = []
   for _ in range(nVoters):
      keep, remove = raw_input().split(" ")
      newVoter = Voter(keep, remove, _)
      if keep[0] == 'C':
         if not newVoter in catLovers:
            catLovers.append(newVoter)
      else:
         if not newVoter in dogLovers:
            dogLovers.append(newVoter)
   print len(catLovers)
   unmatched = set([])
   for cl in catLovers:
      for dl in dogLovers:
         if cl.remove == dl.keep or cl.keep == dl.remove:
            unmatched.add(Conflict(cl, dl))
            catLoversConflict.append(cl)
            dogLoversConflict.append(dl)
   print len(unmatched)
   m = set()
   while True:
      alternating = []
      foundAlternating = 0
      for cl in catLoversConflict:
         if cl.isFree and not cl.evaluated:
            alternating = []
            cl.evaluated = 1
            endCat = "";
            alternating = []
            while True:
               if len(alternating):
                  endCat = alternating[-1].cl
               else:
                  endCat = cl
               if not findUnmatched(unmatched, endCat, alternating):
                  break
               endDog = alternating[-1].dl
               if not findMatched(m, endDog, alternating):
                  break
            if len(alternating) > 0:
               foundAlternating = alternating[0].cl.isFree and alternating[-1].dl.isFree
            else:
               foundAlternating = 0 
            if foundAlternating:
               m = m ^ set(alternating)
               unmatched = unmatched - m
              
               for v in m:
                  v.dl.isFree = 0
                  v.cl.isFree = 0
               break;

      if not foundAlternating: 
         break
   print nVoters - len(m)