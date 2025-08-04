def main():
  user_input = input("Input a number between 1 and 50: ")
  intNum = int(user_input)

  # check if less than or equal to 0, raise a message
  if intNum <= 0:
    return "Invalid input. Give a number betwwen 1 and 50."
  else:
    # set initial values
    result = 0
    counter = 1
    
    # loop while less than or equal to input number
    while counter <= intNum:
      if counter % 2 == 0:
        print(counter)
        result = result + counter # add if even number
      counter = counter + 1
    
    print("The sum of positive even numbers from 1 to", intNum, "is:", result)


if __name__ == "__main__":
  main()