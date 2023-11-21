from card import Card 
from deck import Deck 


#WRITE YOUR HAND CLASS BELOW
class Hand:
  def __init__(self):
    self.cards = []
  
  
  def add_card(self,a_card):
        self.cards.append (a_card)


  def __str__(self):
    s = ""
    for i in self.cards:
      s+= i.__str__() +"\n"
    return s
        
  def add_cards_from_deck(self,shuffle,integar):
    for C in range(integar):
      self.add_card(shuffle.deck_of_cards[C])
      shuffle.deck_of_cards.remove(shuffle.deck_of_cards[C])

      
  def get_rank_dictionary(self):
    self.rank = {}
    l = []
    for i in range(len(self.cards)):
      m = str(self.cards[i]).split(" of ")
      l.append(m[0])
      self.rank[m[0]] = 0
    for p in range(len(l)):
      if l[p] in self.rank:
        self.rank[l[p]] += 1
    return self.rank
    #   if self.hand[i] in self.hand:
    #     self.rank[self.hand[i].get_rank_name()]+=1
    #   else:
    #     self.rank[self.hand[i]]=1
    # return self.rank


      #MC TIPS
      #make an empty dictionary first
      # for loop through your cards
          #figure out what is meantby key here
          # if key in dict:
          #   dict[key]+=1
          # else:
          #   dict[key]=1
      #return dictionary 

  def check_one_pair(self):
    self.get_rank_dictionary()
    count = 0
    yes = 0
    for i in self.rank:
      if self.rank[i]>2:
        count +=1
      elif self.rank[i]==2:
        yes += 1
        if count ==0 and yes ==1:
          return True
        else:
          return False
      

  def check_two_pair(self):
    # self.get_rank_dictionary()
    # count = 0
    # yes = 0
    # for i in self.rank:
    #   if self.rank[i]>2:
    #     count +=1
    #   elif self.rank[i]==2:
    #     yes += 1
    #   if count ==0 and yes ==2:
    #     return True
    #   else:
    #     return False

    
    count = 0
    for i in self.get_rank_dictionary().values():
      if i == 2:
        count += 1
      if count == 2:
        return True 
    
    
  def check_three_of_a_kind(self): 
    threecount = 0
    twocount = 0
  
    for p in self.get_rank_dictionary().values():
      if p == 2:
        twocount += 1
    for p in self.get_rank_dictionary().values():
      if p == 3:
        threecount += 1
      
    if threecount == 1 and twocount == 0:
      return True
      
       # count = 0
      #  yes = 0
      #  for i in self.rank:
      #   if self.rank[i]>3 or self.rank[i]==2:
      #     count += 1
      #  elif self.rank[i]==3:
      #    yes+=1
      #  if count == 0 and yes ==1:
      #   return True
      #   else:
      #     return False
      # self.get_rank_dictionary()

  def check_four_of_a_kind(self):
    fourcount = 0
    for f in self.get_rank_dictionary().values():
      if f == 4:
        fourcount += 1
    if fourcount == 1:
      return True
      
            
            
      # self.get_rank_dictionary()
      # count = 0
      # yes = 0
      # for i in self.rank:
      #   if self.rank[i]>4:
      #     count +=1
      #   elif self.rank[i]==4:
      #     yes += 1
      #   if count ==1 and yes ==1:
      #     return True
      #   else:
      #     return False
      

  def check_full_house(self):
    threecount = 0
    twocount = 0
    for h in self.rank_dictionary().values():
      if h == 3:
        threecount += 1
      if h == 2:
        twocount += 1
      if threecount == 3 and twocount == 2:
        return True
      
      






      
      # self.get_rank_dictionary()
      # nope = 0
      # yes = 0
      # for i in self.rank:
      #   if self.ranks[i]!=3:
      #     nope+=1
      #   elif self.ranks[i]==3 and len(self.ranks)==2:
      #     yes+=1
      #   if nope==1 and yes==1:
      #     return True
        
    

  def check_straight(self):
      nums = []
      for i in self.cards:
        nums.append(i.rank)
        nums.sort()
      for o in range(len(nums)-1):
        if (nums[o]+1) == nums[o+1]:
          continue
        return True
          

  def check_flush(self):
      s = []
      count = 0
      for i in range(len(self.hand)):
        m = str(self.cards[i]).split(" of ")
        s.append(m[i])
      print(s)
      print(len(s))
      for i in range(len[s]-1):
        if s[i]==s[i+1]:
          count+=1
        if count ==4:
          if s[4]==s[0]:
            count+=1
          if count[i] ==s:
            return True
        

  def get_hand_type(self):
    if self.check_flush() == True and self.check_straight() == True:
      return 'straight_flush'
    elif self.check_four_of_a_kind() == True:
      return 'four of a kind'
    elif self.check_full_house() == True:
      return 'full house'
    elif self.check_flush() == True:
      return 'flush'
    elif self.check_straight() == True:
      return 'straight'
    elif self.check_three_of_a_kind() == True:
      return 'three_of_a_kind'
    elif self.check_two_pair() == True:
      return 'two pair'
    elif self.check_one_pair() == True:
      return 'one pair'
    else: 
      return 'high card'
    # Combocards = ['high card','one pair','two pair','three_of_a_kind','straight','flush','full house','four of a kind','straight flush'] 

    
    
    
  
