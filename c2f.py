temp = int(input("Please enter temperature--> "))

conv = str(input("Enter 2c if you would like to convert to celcius"
                 "\nEnter 2f if you would like to convert to Fahrenheit  "))

if conv == "2f":
    temp_2f = str(temp * 1.8 + 32)
    print("{} degrees c equals {} degrees f.".format(temp, temp_2f))

elif conv == "2c":
    temp_2c = str((temp - 32) / 1.8 )
    print("{} degrees f equals {} degrees c".format(temp, temp_2c))

else:
    print("invalid input")