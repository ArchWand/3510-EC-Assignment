# DO NOT ADD ANY IMPORTS
from typing import *

class Solutions:
    # DO NOT MODIFY INIT
    def __init__(self):
        pass

    # Problem 1: Real Estate Profits
    # Explanation and Runtime:
    #
    #
    def realEstatePrices(values: List[int]) -> int:
        n = len(values)
        values.insert(0, 1)
        values.insert(n + 1, 1)
        dp = [(1, i) for i in range(n)]
        total = 0

        if n == 1:
            return values[1]

        # Calculate initial DP table, which holds tuples of the index in input and the value
        for i in range(n):
            dp[i] = (values[i] * values[i + 1] * values[i + 2], i + 1)

        # Sell one property at a time until DP is empty
        while len(dp) > 0:
            # Find max val in DP
            max_tuple = (0, 0)
            max_index = 0
            for j in range(len(dp)):
                if dp[j][0] > max_tuple[0]:
                    max_tuple = dp[j]
                    max_index = j
                if dp[j][0] == max_tuple[0] and values[dp[j][1]] < values[dp[max_index][1]]:
                    max_tuple = dp[j]
                    max_index = j
            
            total += max_tuple[0]
            idx = max_tuple[1]

            if len(dp) <= 2:
                dp.pop(max_index)
                return total + values[dp[0][1]]
            
            if max_index < len(dp) - 1:
                dp[max_index + 1] = (dp[max_index + 1][0] // values[idx] * values[dp[max_index - 1][1]], dp[max_index + 1][1])
            if max_index > 0:
                dp[max_index - 1] = (dp[max_index - 1][0] // values[idx] * values[dp[max_index + 1][1]], dp[max_index - 1][1])
            dp.pop(max_index)



    # Problem 2: Warehouse Package Stacking
    # Explanation and Runtime: O(n^2)
    # This is a modified LIS problem, where instead of just checking 1 strictly increasing
    # number in each cell, there are 2 numbers which both must be strictly increasing compared to
    # their respective numbers in the previous pair, at each cell. I implemented a normal LIS algorithm
    # using a linear search to replace the smallest pair greater than the newfound pair when we cannot
    # just append a new pair to the end of the subsequence. We do append the new pair if it is strictly
    # greater than the current end of the subsequence. This algorithm ensures that we always construct
    # a subsequence where each pair is strictly greater than the previous pair because if a new pair IS
    # greater, we simply append it, but if it is not greater, it is either discarded or used to "improve"
    # our current subsequence by making it more optimal. This is O(n^2) because we do a single pass
    # through the input array, but for each pair, we also iterate through the current subsequence to
    # replace a pair if needed. Note that for LIS to work, I have to sort the input array first.
    def maxPackages(packages: List[Tuple[int, int]]) -> int:
        if not packages:
            return 0
        
        # Sort by width and then by height in descending order
        packages.sort(key=lambda x: (x[0], -x[1]))
        
        n = len(packages)
        subseq = [packages[0]]
        for i in range(1, n):
            width, height = packages[i]
            if width > subseq[-1][0] and height > subseq[-1][1]:
                subseq.append(packages[i])
            else:
                for j in range(len(subseq)):
                    if width <= subseq[j][0] and height <= subseq[j][1]:
                        subseq[j] = packages[i]
                        break
        return len(subseq)
    
    # Problem 3: Building Blocks
    # Explanation and Runtime: O(n)
    # This simply iterates through both lists simultaneously and checks if there
    # is an element out of order in either list. If there is, we check if swapping
    # the elements would satisfy both lists' condition of being strictly increasing.
    # If it does, I increment the swap counter. If it doesn't, then there is nothing
    # else we can do, and so it is impossible, so I return -1. Because we can only
    # swap two elements at the same index i, we do not need to check any other
    # elements for swapping, and if swapping the two elements at index i doesn't
    # fix the out-of-order issue, then it is impossible to fix.
    def minSwap(nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        i = 1
        count = 0

        while i < n:
            a = nums1[i]
            b = nums2[i]
            pre_a = nums1[i - 1]
            pre_b = nums2[i - 1]

            if a <= pre_a:
                if b > pre_a and a > pre_b:
                    count += 1
                else:
                    return -1
            elif b <= pre_b:
                if a > pre_b and b > pre_a:
                    count += 1
                else:
                    return -1
            i += 1
        return count
    
    # Problem 4: Modular Two Sum 
    # Explanation and Runtime: O(n)
    # I used Two Sum and modified some of the logic for how we store and look for "target" values.
    # I created a dictionary of remainders for each number in the input array. I then iterate through 
    # the input array and increment the count of each remainder based on how many times it appears in
    # the array. Then I iterate through the remainders and calculate the number of combinations that
    # can be made with each remainder. If the remainder is 0, then we can combine the remainders with
    # themselves to get a number divisible by k. If a pair of remainders are equal (both k / 2), then
    # we can combine them with themselves to get a number divisible by k. If the remainders are not equal,
    # then we can combine the two remainders to get a number divisible by k. The runtime is O(n) because
    # we iterate through the input array once to count the remainders, and then we iterate through all
    # the possible remainders (all integers in the range from 1 to half of k) to calculate the number of 
    # combinations that can be made with each remainder.
    def modTwoSum(A: List[int], k: int) -> int:
        n = len(A)
        remainders = {i: 0 for i in range(k)}
        for i in range(n):
            remainders[A[i] % k] += 1

        # Combinations within num % k == 0 (adding together will be divisible by k)
        count = (remainders[0] * (remainders[0] - 1)) // 2

        # Combinations where the two remainders add to k
        for i in range(1, k // 2 + 1):
            if i != k - i:
                # i and the complement are different remainders
                count += remainders[i] * remainders[k - i]
            else:
                # i and the complement are the same remainder
                count += (remainders[i] * (remainders[i] - 1)) // 2

        return count

    # Problem 5: Maximum Magic Path Power
    # Explanation and Runtime: O(|V| + |E|)
    # I use DFS to traverse the graph and keep track of the max energy collected across all paths.
    # Only count energy once per node visited. The DFS function takes in the current node, the time
    # spent so far, the energy collected so far, and the set of visited nodes. If the time spent exceeds
    # the maxTime, then this path is invalid, so we return and let other recursive calls continue.
    # If the path is still valid, we update the global maxEnergy variable if the energy collected on this
    # path is greater than the current maxEnergy. This should find the maximum energy collected across all
    # possible paths. The runtime for DFS is O(|V| + |E|) but note that we may visit some nodes multiple
    # times, which can add a constant factor to the runtime.
    def maximumMagicPathPower(energies: List[int], edges: List[List[int]], maxTime: int) -> int:
        if not energies:
            return 0
        
        if not edges:
            return energies[0]
        
        if maxTime <= 0:
            return max(energies)

        # Create adjacency list of the graph
        adjList = {}
        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            if edge[1] not in adjList:
                adjList[edge[1]] = []
            adjList[edge[0]].append((edge[1], edge[2]))
            adjList[edge[1]].append((edge[0], edge[2]))

        # DFS to travel a bunch of different paths until maxTime exceeded,
        # keeping track of the max energy collected across all paths. Only
        # count energy once per node visited.
        def dfs(node, timeSpent, energyCollected, visited):
            nonlocal maxEnergy
            if timeSpent > maxTime:
                return
            visited.add(node)
            maxEnergy = max(maxEnergy, energyCollected)
            for neighbor, weight in adjList.get(node, []):
                newEnergyCollected = energyCollected + energies[neighbor] if neighbor not in visited else energyCollected
                dfs(neighbor, timeSpent + weight, newEnergyCollected, visited)

        maxEnergy = energies[0]
        visited = set([0])
        dfs(0, 0, energies[0], visited)
        return maxEnergy
    
    # Problem 6: Divide the Harvest
    # Explanation and Runtime: O(nlog(sum(quantity)))
    # This is a divide and conquer algorithm that uses binary search to find the minimum amount of fruit
    # that each person should get. The binary search is performed on the integer range from 0 to the total
    # amount of fruit. CanDivideFruitWithMin checks if the proposed min fruit amount per person can be divided into k + 1
    # groups. If it can, then we might be able to increase the minimum fruit per person. Otherwise, decrease
    # the minimum fruit per person because there is not enough to divide into k + 1 groups. The function returns
    # the j value, which is the 2nd to least amount of fruit in any group (i is the least). Since this is a 
    # binary search on the range from 0-sum(quantity), and then we also iterate through each basket for each
    # binary search iteration, the runtime is O(nlog(sum(quantity))), where n is the size of the quantity array.
    def divideTheHarvest(quantity: List[int], k: int) -> int:
        
        if not quantity:
            return 0
        
        if k == 0:
            return sum(quantity)

        if len(quantity) == 1:
            return quantity[0]
        
        # Check if the baskets can be divided into k+1 partitions given this minimum fruit per person
        def canDivideFruitWithMin(min_fruit):
            curr_fruit_in_division = 0
            division_count = 0
            # Iterate through each basket and keep track of how much fruit is in the current division.
            # Make a new division when we exceed the proposed minimum
            for basket in quantity:
                curr_fruit_in_division += basket
                if curr_fruit_in_division >= min_fruit:
                    division_count += 1
                    curr_fruit_in_division = 0
                # Return true when we reach k + 1 divisions
                if division_count == k + 1:
                    return True
            return False

        # Binary search on the integer range from 0 to total fruit
        i = 0
        j = sum(quantity)
        while i < j:
            # Mid point represents the minimum amount of fruit each person should get
            mid = (i + j + 1) // 2

            if canDivideFruitWithMin(mid):
                # If it can be divided into k+1 groups, then we might be able to increase the minimum fruit per person
                i = mid
            else:
                # Otherwise, decrease the minimum fruit per person because there is not enough to divide into k + 1 groups
                j = mid - 1

        return j
        

    # Problem 7: Coloring Sidewalks 
    # Explanation and Runtime: O(n)
    # I used DP with a 2D array (n x 3) where n is the number of sidewalks and there is a column
    # for each of the 3 colors. I set the first row to the time values of the first sidewalk. Then,
    # I iterate through each sidewalk and choose the optimal new color for each of the 3 color
    # scenarios, and keep track of the total accumulated time in the DP array. The final answer
    # is whatever the smallest of the 3 total accumulated times is for the last sidewalk. The runtime
    # is O(3n) because we iterate through each sidewalk once and do a 3 operations for each
    # sidewalk. This simplifies to O(n).
    def coloringSidewalks(time: List[int]) -> int:
        n = len(time)
        if n == 0:
            return 0
        
        # Create DP table of size n x 3 where n is the sidewalk ID and each column is a different color
        dp = [[0, 0, 0] for i in range(n)]

        # Set the first row (first sidewalk) time values
        dp[0] = [time[0][0], time[0][1], time[0][2]]

        # Iterate through each sidewalk. For each of the 3 columns/colors there are 2 options
        # to color the next sidewalk with (the other 2 colors). Choose the minimum time value
        # out of those 2, and add it to the current sidewalk's time value for this color column.
        for i in range(1, n):
            dp[i][0] = time[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = time[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = time[i][2] + min(dp[i - 1][0], dp[i - 1][1])

        # The answer is whatever the minimum total is out of the 3 colors for the last sidewalk
        return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


    # Problem 8: Chemical Concoctions
    # Explanation and Runtime: O(|V| + |E|) where |V| is the number of chemicals and |E| is the number of formulas
    # Using the formulas, I create a graph that we can then use a topological sort on
    # to find the necessary ordering in order to visit all nodes in their correct order.
    # To create the initial graph, I iterate through the formulas and add the nodes
    # and edges to an adjacency list based on the ordering of the chemicals in the formulas
    # provided on the input formula sheet. I also keep track of an in_degree count for each
    # node in a map to help with the topological sort. I use DFS to do a top sort, and keep
    # track of which nodes have been visited in this current path so that I can detect a
    # cycle if it occurs. If there's a cycle, then it is impossible to find the correct order
    # of chemicals, so I return an empty string. If there is no cycle, then I build the top
    # sort by pushing the nodes to the stack in order of when I finish visiting it, and then
    # the final answer is just the reversed order of that. The runtime is O(|V|+|E|) because
    # we iterate through the formulas once to build the graph, which is approximately O(|E|)
    # because we generally learn about one edge per formula. Then we do a top sort which
    # is O(|V| + |E|).
    def chemicalConcoctions(formulas: List[str]) -> str:
        
        # Create graph
        adjList = {}
        in_degrees = {}
        n = len(formulas)
        for i in range(n - 1):
            formula_1 = formulas[i]
            formula_2 = formulas[i + 1]
            smaller_len = min(len(formula_1), len(formula_2))

            for j in range(smaller_len):
                chemical_1 = formula_1[j]
                chemical_2 = formula_2[j]

                # add new chemical to adjList if not already in there
                if chemical_1 not in adjList:
                    adjList[chemical_1] = []
                    in_degrees[chemical_1] = 0
                if chemical_2 not in adjList:
                    adjList[chemical_2] = []
                    in_degrees[chemical_2] = 0

                # add edge from chemical_1 to chemical_2 if they are different chemicals
                if chemical_1 != chemical_2:
                    adjList[chemical_1].append(chemical_2)
                    in_degrees[chemical_2] += 1
                    break
            
        def dfs(node):
            if node in cycle_marker:
                return False # Cycle found
            if node in visited:
                return True # Already visited, no need to explore again
            
            cycle_marker.add(node)
            for neighbor in adjList[node]: # Explore the neighbors
                result = dfs(neighbor)
                if not result:
                    return False
            cycle_marker.remove(node)
            visited.add(node)
            stack.append(node) # Keep track of top sort order
            return True

        # Topological sort
        stack = []
        visited = set()
        cycle_marker = set()
        for chemical in in_degrees:
            if in_degrees[chemical] == 0 and chemical not in visited:
                result = dfs(chemical)
                if not result:
                    return "" # Cycle found
                
        return "".join(stack[::-1]) # Reverse the stack to get the actual order we need

    
    # Problem 9: Maximum Sum of Non-Adjacent Subsequences
    # Explanation and Runtime: O(n)
    # This is the House Robber problem. After handling the base cases where the list has <3 elements,
    # I create a DP array of size n. The value at DP[i] represents the max sum as of this index i.
    # When we find a new number, we can either add this number and disregard the immediate previous number,
    # so we use DP[i-1] + A[i], or we can ignore this current number and maintain the previous one DP[i-1].
    # This allows us to consider both cases of either adding or not adding this number to the sum. Continue
    # this process until we reach the end of the list, and whatever is the last number in DP must be the max
    # possible sum of non-adjacent subsequences. The runtime is O(n) because we iterate through the list once
    # to calculate the DP array and each step is a constant operation.
    def maxNonAdjSum(A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]
        if n == 2:
            return max(A[0], A[1])

        dp = [0] * n
        dp[0] = A[0]
        dp[1] = max(A[0], A[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i])

        return dp[n - 1]
    
    # Problem 10: DigitGPT
    # Explanation and Runtime:
    # 
    #
    def reviveStrings(n: int, ticket: str) -> bool:
        # Split the string into two halves
        half = n // 2
        first_half = ticket[:half]
        second_half = ticket[half:]
        
        # Calculate the current sum values of the two halves
        sum_left = 0
        sum_right = 0
        for i in range(half):
            if first_half[i] != '*':
                sum_left += int(first_half[i])
            if second_half[i] != '*':
                sum_right += int(second_half[i])
        
        # Count the number of * on each side
        num_stars_left = first_half.count('*')
        num_stars_right = second_half.count('*')
        amount_needed_to_make_equal = sum_left - sum_right
        max_adjustment = (num_stars_left - num_stars_right) * 9
        
        # If the difference can be adjusted to zero, Melon wins
        if abs(amount_needed_to_make_equal) <= max_adjustment:
            return True
        else:
            return False

    
    # Problem 11: Building a Brick Wall
    # Explanation and Runtime: O(|B|*l)
    # This is similar to the coin change problem, but here we keep track of how many unique
    # combinations there are for making the wall of length l out of bricks of different lengths.
    # I use DP to calculate the number of combinations for each length from 0 to l, and then
    # each subsequently large length depends on previously calculated combination counts from
    # the smaller wall lengths. Since each previous values in the DP array has the number of
    # ways to build the wall at that lesser length with the given brick lengths, we know DP[i] is 
    # just the sum of the number of ways to build the wall at length i - brick_length for each brick
    # length. The runtime is O(|B|*l) because we iterate through the brick lengths once and then iterate
    # through the length values from the brick length to l for each brick.
    def buildBrickWall(B: List[int], l: int) -> int:
        dp = [0] * (l + 1)
        dp[0] = 1

        for b in B:
            for i in range(b, l + 1):
                if b <= i: # This brick is small enough to fit in length i
                    dp[i] += dp[i - b]

        return dp[l]

    # Problem 12: Archipelagos
    # Explanation and Runtime: O(|V| + |E|)
    # This uses Tarjan's algorithm to find the edges which if removed cause the graph to
    # become disconnected. I first create an adjacency list of the graph, and then I use 
    # Tarjan's algorithm to find the bridges. I keep track of the discovery time and low
    # time for each node. The discovery time is the time when the node was first visited
    # and the low time is the lowest discovery time of all nodes reachable from the current node.
    # If the low time of a neighbor is greater than the discovery time of the current node, then
    # the edge between the current node and the neighbor is a bridge. This is because the neighbor
    # cannot reach any node with a discovery time less than the current node, so removing the
    # edge would disconnect the graph. The runtime is O(|V| + |E|) because we iterate through
    # each node and edge in the graph once since this effectively uses DFS.
    def findNeededBridges(n: int, edges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        
        # Create adjacency list for the graph
        adjList = {}
        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            if edge[1] not in adjList:
                adjList[edge[1]] = []
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        # Tarjan's algo to find bridges
        def dfs(node, parent, visited, low, disc, bridges):
            visited.add(node)
            disc[node] = low[node] = dfs_time[0]
            dfs_time[0] += 1

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor, node, visited, low, disc, bridges)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        bridges.append((node, neighbor))
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])
        
        # Set up Tarjan's algo with a low array of infinity and a discovery array of infinity
        dfs_time = [0]
        visited = set()
        low = [float('inf')] * n
        disc = [float('inf')] * n
        bridges = []
        for node in adjList:
            if node not in visited:
                dfs(node, -1, visited, low, disc, bridges)
        
        return bridges
    
    # Problem 13: Search Engineer 
    # Explanation and Runtime:
    # I use a modified LCS where the subsequence from text must match the entirety of pattern
    # rather than just a subsequence of pattern, and we keep track of the number of subsequennces
    # that match the pattern. I use a 2D DP array to keep track of the number of subsequences that
    # match the pattern up to the current index in text and pattern. If the current characters in
    # text and pattern match, then we choose to either include this char or to skip it. If we include
    # it, then we add the number of subsequences that match the pattern up to the previous index in
    # text and pattern. If we skip it, then we just add the number of subsequences that match the pattern
    # up to the previous index in text and the current index in pattern.
    def numDistinct(text: str, pattern: str) -> int:
                
                # Create (m+1) x (n+1) DP table
                m = len(text)
                n = len(pattern)
                dp = [[0] * (n + 1) for i in range(m + 1)]
                
                # Initialize the first column of the DP table to be 1. This is where
                # the pattern is empty, so there is always 1 subsequence that matches
                # (the empty subsequence of text).
                for i in range(m + 1):
                    dp[i][0] = 1
                
                for i in range(1, m + 1):
                    for j in range(1, n + 1):
                        if text[i - 1] == pattern[j - 1]: # Character match, add the include and skip counts
                            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                        else: # Character mismatch, skip count is only option
                            dp[i][j] = dp[i - 1][j]
                
                return dp[m][n]

    # Problem 14: Buzz's Bees
    # Explanation and Runtime: O(|V|^2)
    # This uses a modified Prim's algorithm which does not use a priority queue as we don't have access to heaps.
    # I keep track of the minimum cost to connect each node to the MST in a dist_map array. I start with
    # the first node and then find the smallest cost node which isn't yet in the MST. I then add this node
    # to the MST and update the cost of connecting the remaining nodes to the MST. I keep track of the total
    # cost of the MST and return this value. The runtime is O(|V|^2) because we iterate through each node and
    # for each node, we iterate through the remaining nodes to update the cost of connecting the remaining
    # nodes to the MST.
    def minNetworkCost(coords: list[tuple[int, int]]) -> int:
        n = len(coords)
        if n == 0:
            return 0
    
        dist_map = [float('inf')] * n
        mst = set()
        dist_map[0] = 0
        total_cost = 0
    
        # Prim's algo without a priority queue
        for x in range(n):
            # Find smallest cost node which isn't yet in MST
            u = -1
            for i in range(n):
                if i not in mst and (u == -1 or dist_map[i] < dist_map[u]):
                    u = i
    
            mst.add(u)
            total_cost += dist_map[u]
    
            # Update the cost of connecting the remaining nodes to the MST
            for v in range(n):
                if v not in mst:
                    cost = (coords[u][0] - coords[v][0]) ** 2 + (coords[u][1] - coords[v][1]) ** 2
                    if cost < dist_map[v]:
                        dist_map[v] = cost
    
        return total_cost