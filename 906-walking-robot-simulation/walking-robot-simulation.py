# A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:
#
#
# 	-2: turn left 90 degrees
# 	-1: turn right 90 degrees
# 	1 <= x <= 9: move forward x units
#
#
# Some of the grid squares are obstacles. 
#
# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
#
# If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)
#
# Return the square of the maximum Euclidean distance that the robot will be from the origin.
#
#  
#
# Example 1:
#
#
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
#
#
#
# Example 2:
#
#
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
#
#
#
#  
#
# Note:
#
#
# 	0 <= commands.length <= 10000
# 	0 <= obstacles.length <= 10000
# 	-30000 <= obstacle[i][0] <= 30000
# 	-30000 <= obstacle[i][1] <= 30000
# 	The answer is guaranteed to be less than 2 ^ 31.
#
#


class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        curr = [0, 0]
        m = 0
        direction = "N"
        d = {'N-2':'W', 'N-1':'E', 
             'S-2':'E', 'S-1':'W',
             'W-2':'S', 'W-1':'N',
             'E-2':'N', 'E-1':'S'}
        obstacles = set(map(tuple, obstacles))
        for c in commands:
            if c in (-1,-2):
                direction = d[direction + str(c)]
            else:
                if direction == "N":
                    tmp = c
                    for i in range(1, c+1):
                        if (curr[0], curr[1]+i) in obstacles:
                            tmp = i - 1
                            break
                    curr[1] += tmp
                elif direction == "S":
                    tmp = c
                    for i in range(1, c+1):
                        if (curr[0], curr[1]-i) in obstacles:
                            tmp = i - 1
                            break
                    curr[1] -= tmp
                elif direction == "W":
                    tmp = c
                    for i in range(1, c+1):
                        if (curr[0]-i, curr[1]) in obstacles:
                            tmp = i - 1
                            break
                    curr[0] -= tmp
                elif direction == "E":
                    tmp = c
                    for i in range(1, c+1):
                        if (curr[0]+i, curr[1]) in obstacles:
                            tmp = i - 1
                            break
                    curr[0] += tmp
                m = max(m, curr[0] ** 2 + curr[1] ** 2)
       
        return m
                
