from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n % groupSize :
            return False
        count=Counter(hand)

        for card in sorted(count):
            if count[card]>0:
                freq=count[card]

                for nextCard in range(card,card + groupSize):
                    if count[nextCard]<freq:
                        return False
                    
                    count[nextCard] -=freq
        return True