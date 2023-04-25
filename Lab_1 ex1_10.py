number = int(input("Введите трехзначное число: "))
digit_sum = sum(int(digit) for digit in str(number))

if digit_sum % 3 == 0:
    print(f"Число {number} делится на 3, так как сумма его цифр ({digit_sum}) делится на 3")
else:
    print(f"Число {number} не делится на 3, так как сумма его цифр ({digit_sum}) не делится на 3")