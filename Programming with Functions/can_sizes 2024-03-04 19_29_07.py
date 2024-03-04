from colorsys import TWO_THIRD
import math

pi = math.pi

def vol(can):
    can.v = pi * (can.r ** 2) * can.h
    return can

def sa(can):
    can.sa = 2 * pi * can.r * (can.r + can.h)
    return can

def se(can):
    can = vol(can)
    can = sa(can)
    can.se = can.v / can.sa
    return can

class Can_Dementions:
    def __init__(Can_Dementions, radius, height, cost_per_can, volume, surface_area, storage_efficiency):
        Can_Dementions.r = radius
        Can_Dementions.h = height
        Can_Dementions.c = cost_per_can
        Can_Dementions.v = volume
        Can_Dementions.sa = surface_area
        Can_Dementions.se = storage_efficiency

volu = 0
sura = 0
store = 0


def main():
    one_pic = Can_Dementions(6.83, 10.16, 0.28, volu, sura, store)
    one_tall = Can_Dementions(7.78, 11.91, 0.43, volu, sura, store)
    two = Can_Dementions(8.73, 11.59, 0.45, volu, sura, store)
    two_half = Can_Dementions(10.32, 11.91, 0.61, volu, sura, store)
    three_cylinder = Can_Dementions(10.79, 17.78, 0.86, volu, sura, store)
    five = Can_Dementions(13.02, 14.29, 0.83, volu, sura, store)
    six_zed = Can_Dementions(5.40, 8.89, 0.22, volu, sura, store)
    eight_zed = Can_Dementions(6.83, 7.62, 0.26, volu, sura, store)
    ten = Can_Dementions(15.72, 17.78, 1.53, volu, sura, store)
    two_eleven = Can_Dementions(6.83, 12.38, 0.34, volu, sura, store)
    three_hundred = Can_Dementions(7.62, 11.27, 0.38, volu, sura, store)
    three_o_three = Can_Dementions(8.10, 11.11, 0.42, volu, sura, store)

    can_list = [one_pic, one_tall, two, two_half, three_cylinder, five, six_zed, eight_zed, ten, two_eleven, three_hundred, three_o_three]

    for can in can_list:
        can = se(can)
        print(f"Can #{(can_list.index(can)) + 1} has a storage efficiency of {can.se:.02f}.")

main()

print("All is well!")