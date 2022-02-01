# for num in range(1, 13):
#     print("2 x {0} = {1}".format(num, 2 * num))
#     print("*" * 80)


age = int(input("enter age = "))

if age>27:
    print("you need to earn 2 lakhs per month")
elif age==50:
    print("you should be earning 1 crore per month")
else:
    print("Congratulation")



answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time")


