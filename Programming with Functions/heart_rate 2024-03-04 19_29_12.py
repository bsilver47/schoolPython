##The below lines, ending with line 11, are copied from the BYUI Guide

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

age = int(input("How old are you? "))

max_rate = 220 - age
ideal_min = max_rate * .65
ideal_max = max_rate * .85

print(f"While exercising to strenghten your heart, the ideal range to keep your heartrate")
print(f"at is between {round(ideal_min)} and {round(ideal_max)} beats per minute.")
