print("Possible PINs are:")

for i in range(10000):
    pin = str(i).zfill(4)   # Makes numbers like 23 into 0023

    # Convert each digit to integer
    d1 = int(pin[0])
    d2 = int(pin[1])
    d3 = int(pin[2])
    d4 = int(pin[3])

    # Check if all digits are even
    if d1 % 2 == 0 and d2 % 2 == 0 and d3 % 2 == 0 and d4 % 2 == 0:
        # Check if sum of digits is 16
        if d1 + d2 + d3 + d4 == 16:
            print(pin)