import numpy as np

def start():
    # Convert the list to a NumPy array and print it
    rainfall_array = np.array(sample_rainfall)
    print("Rainfall as NumPy array:", rainfall_array)

    # Print the total rainfall for the week
    total_rainfall = np.sum(rainfall_array)
    print("Total rainfall:", np.round(total_rainfall, decimals=2))

    # Print the average rainfall for the week
    average_rainfall = np.mean(rainfall_array)
    print("Average rainfall for the week is", np.round(average_rainfall, decimals=2))

    # Count how many days had no rain (0 mm)
    # -- boolean_array = rainfall_array == 0  #returns a boolean array
    # -- count_zero_rain = np.count_nonzero(boolean_array)  #counts the number of TRUE
    count_zero_rain = np.count_nonzero(rainfall_array == 0)
    print(f"There are {count_zero_rain} days with no rain for the week.")

    # Print the days (by index) where the rainfall was more than 5 mm
    print("Days (by index) where the rainfall was more than 5 mm for the week:")
    more_than_5mm = np.where(rainfall_array > 5)[0]  #returns indices
    #print(np.where(rainfall_array > 5))
    print(more_than_5mm)

    # -- loop through more_than_5mm, index as workarea
    for index in more_than_5mm:
        print(f"***\t{index} - {days_of_the_week[index]} - {rainfall_array[index]} mm of raifall")


if __name__ == "__main__":
    sample_rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    print("Sample rainfall:", sample_rainfall)
    days_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    start()