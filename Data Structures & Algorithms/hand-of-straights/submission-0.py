class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, groupSize + first):
                if i not in count:
                    return False
                
                count[i] -= 1
                if not count[i]:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        
        return True


        
            