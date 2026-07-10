class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        max_area = heights[0]
        for i in range(n):
            if not st or st[-1][0] < heights[i]:
                st.append((heights[i],i))
            else:
                min_index = i
                while st and st[-1][0] > heights[i]:
                    area = (st[-1][0]) * (i - st[-1][1])
                    max_area = max(max_area, area)
                    min_index = st[-1][1]
                    st.pop()
                st.append((heights[i],min_index))

            
        while st:
            area = st[-1][0] * (n-st[-1][1])
            max_area = max(max_area, area)
            st.pop()
        return max_area

