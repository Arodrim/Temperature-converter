print("Temperature Converter")

while True:
    temperature = float(input("Enter the temperature:"))
    unit = input("Is the temperature in Celcius (\033[94mC\033[0m) or Farenheit (\033[94mF\033[0m)?")
    lowercase = unit.lower()
    if(lowercase == "c"):
        result = (temperature * 9/5) + 32
        print(result)
    elif(lowercase == "f"):
        result = (temperature - 32) * 5/9
        print(result)
    else:
        print("Wrong temperature unit, please try again.")


