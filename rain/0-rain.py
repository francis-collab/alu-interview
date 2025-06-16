#!/usr/bin/python3
"""Calculate the amount of rain that will be captured after it rains."""


def rain(walls):
    """Determine how much rainwater can be trapped between walls."""
    if not walls or len(walls) < 3:
        return 0

    total_rain = 0
    for i in range(1, len(walls) - 1):
        left_max = max(walls[:i])
        right_max = max(walls[i + 1:])
        min_wall = min(left_max, right_max)

        if walls[i] < min_wall:
            total_rain += min_wall - walls[i]

    return total_rain
