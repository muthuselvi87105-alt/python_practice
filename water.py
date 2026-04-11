def trap_rain_water(height):
    n = len(height)
    water = 0

    for i in range(1, n-1):

        # find left max manually
        left_max = height[0]
        for j in range(i):
            if height[j] > left_max:
                left_max = height[j]

        # find right max manually
        right_max = height[i+1]
        for k in range(i+1, n):
            if height[k] > right_max:
                right_max = height[k]

        # find min manually
        if left_max < right_max:
            min_height = left_max
        else:
            min_height = right_max

        water += min_height - height[i]

    return water


# Example
print(trap_rain_water([4,2,0,3,2,5]))   # Output: 9
