class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        h = Counter(hand)
        s = sorted(hand)

        for num in s:
            if h[num]:
                print('making group' + str(num))
                for n in range(num, num + groupSize):
                    if not h[n]:
                        return False
                    print(str(n) + 'found')
                    h[n] -= 1
        
        return True

