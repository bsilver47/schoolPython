def mile_counter(start_odo, end_odo):
    miles = end_odo - start_odo
    return miles

def miles_per_gallon(miles, fuel_usage):
    mpg = miles / fuel_usage
    return mpg

def lp100k_from_mpg(mpg):
    lp_hundred = ((235.215) / (mpg))
    return lp_hundred

def main():
    start_odo = float(input("What is the starting odometer number? "))
    end_odo = float(input("What is the ending odometer number? "))
    fuel_usage = float(input("How many gallons of fuel were used? "))

    miles = mile_counter(start_odo, end_odo)
    mpg = miles_per_gallon(miles, fuel_usage)
    lp_hundred = lp100k_from_mpg(mpg)

    print(f"Given that you have traveled {miles} miles, and used {fuel_usage} gallons,")
    print(f"you are getting about {mpg:.02f} miles per gallon of gas.")
    print(f"If you would prefer metric, the equivalent to that is:")
    print(f"{lp_hundred:.02f} Litres per Hundred Kilometers of petroleum.")

    pass

main()
