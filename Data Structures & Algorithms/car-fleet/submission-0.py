class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
            
        pairs = sorted(pairs, reverse=True)

        stack = [pairs[0]]
        i = 1
        while i< len(position):
            top_pos, top_speed = stack[-1]
            top_time_to_target = (target-top_pos)/top_speed

            curr_pos, curr_speed = pairs[i]
            curr_time_to_target = (target-curr_pos)/curr_speed
            if top_time_to_target < curr_time_to_target:
                stack.append(pairs[i])
            i+=1
        return len(stack)



