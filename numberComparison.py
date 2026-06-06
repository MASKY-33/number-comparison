first_number = int(input("Give number: "))
sec_number = int(input("Give one more number: "))

if first_number > sec_number:
    print(f"{first_number} is bigger")
elif first_number < sec_number:
    print(f"{sec_number} is bigger")
else:
    print("Numbers are equal")
