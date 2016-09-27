sum = 0;

user_input = input("Enter number of 50 euro banknotes: ")
sum += int(user_input) * 50
user_input = input("Enter number of 20 euro banknotes: ")
sum += int(user_input) * 20
user_input = input("Enter number of 10 euro banknotes: ")
sum += int(user_input) * 10
user_input = input("Enter number of 5 euro banknotes: ")
sum += int(user_input) * 5
user_input = input("Enter number of 2 euro coins: ")
sum += int(user_input) * 2
user_input = input("Enter number of 1 euro coins: ")
sum += int(user_input) * 1

print("You have", sum, "euros")
