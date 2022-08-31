'''In the game of cribbage you have 5 cards with rank numbers between 1 and 13. Here you must output the number of pairs of equal ranked cards.
Input
5 lines containing the rank numbers of CARDs you hold.
Output
Line 1: The number of pairs of equal ranked cards.
Constraints
1 <= CARD <= 13
Example
Input
1       [12341] o:1     [10,8,6,4,2] o:0    [3,5,3,6,3] o:3
1
5
5
7
Output
2
'''



c=0
d=[]
card=[int(input()) for i in range(5)]
for j in card:
    if card.count(j) > 2:
        print(card.count(j))
        break
    elif card.count(j)>=2 and j not in d:
        d.append(j)
        print(len(d))