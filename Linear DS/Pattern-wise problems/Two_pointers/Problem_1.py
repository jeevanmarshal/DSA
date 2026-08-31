def max_area(heights):

    L = 0
    R = len(heights)-1
    max_area = 0
    
    while L < R:
        width = R-L
        height = min(heights[L], heights[R])
        area = width * height
        max_area = max(max_area, area)
        
        if heights[L] < heights[R]:
            L += 1
        else:
            R -= 1

    return max_area

heights = [1,8,6,2,5,4,8,3,7]

print(max_area(heights))