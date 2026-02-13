# Program to determine if a given number is a Perfect Number

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a Perfect Number")
else:
    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  # Avoid adding square root twice
                divisor_sum += num // i

    if divisor_sum == num:
        print(f"{num} is a Perfect Number")
    else:
        print(f"{num} is not a Perfect Number")
