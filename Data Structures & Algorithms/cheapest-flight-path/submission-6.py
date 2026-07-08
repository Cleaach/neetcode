class Airport:
    def __init__(self, name):
        self.name = name
        self.flights = [] # elements are (price, dest)
        self.dests = set()
    
    def add(self, to, price):
        if to in self.dests:
            return
        self.flights.append((price, to))
        self.dests.add(to)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # init DS
        airports = {}
        for flight in flights:
            if flight[0] not in airports:
                f = Airport(flight[0])
                airports[flight[0]] = f
            else:
                f = airports[flight[0]]
            if flight[1] not in airports:
                t = Airport(flight[1])
                airports[flight[1]] = t
            else:
                t = airports[flight[1]]
            
            f.add(flight[1], flight[2])

        # bfs
        memo = {}
        def bfs(curr, stopsmade):
            if curr.name == dst:
                return 0
            if stopsmade == k + 1:
                return 1000000
            if (curr.name, stopsmade) in memo:
                return memo[(curr.name, stopsmade)]
            
            res = 1000000
            for p, to in curr.flights:
                res = min(res, p + bfs(airports[to], stopsmade + 1))
            
            memo[(curr.name, stopsmade)] = res
            return res
        
        output = bfs(airports[src], 0) 
        return -1 if output == 1000000 else output

            