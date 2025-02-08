from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
poker_hand = fetch_ucirepo(id=158) 
  
# data (as pandas dataframes) 
X = poker_hand.data.features 
y = poker_hand.data.targets 

# print X to a textfile
X.to_csv('poker-hand-data.txt', sep='\t', index=False)

# print y to a textfile
y.to_csv('poker-hand-targets.txt', sep='\t', index=False)

# print poker_hand to a textfile
poker_hand.to_csv('poker-hand.txt', sep='\t', index=False)
