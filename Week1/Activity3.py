import numpy as np

def main():
    # user input, recorded temperatures of the week
    day1 = input("Input Mon temperature in Celsius:")
    c1 = float(day1)
    day2 = input("Input Tue temperature in Celsius:")
    c2 = float(day2)
    day3 = input("Input Wed temperature in Celsius:")
    c3 = float(day3)
    day4 = input("Input Thu temperature in Celsius:")
    c4 = float(day4)
    day5 = input("Input Fri temperature in Celsius:")
    c5 = float(day5)
    day6 = input("Input Sat temperature in Celsius:")
    c6 = float(day6)
    day7 = input("Input Sun temperature in Celsius:")
    c7 = float(day7)

    arrTempC = np.array([c1, c2, c3, c4, c5, c6, c7])
    print(arrTempC)
    
    # average temperature
    averageTemp = np.average(arrTempC)
    print("The average temperature in Celsius for the week is", np.round(averageTemp, decimals=2))

    # highest temperature
    # tempHighest = np.max(arrTempC)
    print("The highest recorded temperature of the week is", np.max(arrTempC), "Celsius.")
    # lowest temperature
    print("The lowest recorded temperature of the week is", np.min(arrTempC), "Celsius")

if __name__ == "__main__":
    
    main()
