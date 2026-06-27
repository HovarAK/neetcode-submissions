class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Notes:
        #   len(position) == len(speed) == n.
        #   position[i] == position of the ith car in miles.
        #   speed[i] == the speed of the ith car in miles per hour.
        #   destination is at position (target) miles.
        #
        #   car fleet => non-empty set of cars driving at the same position and same speed

        # keep track of the cars. This array will only contain the first car of each fleet.
        fleet = sorted(zip(position, speed))

        stack = []

        for pos, spd in reversed(fleet):
            time = (target - pos) / spd

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
                

            
