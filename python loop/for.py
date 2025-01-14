a = "Hello"

for i in a:
    print(i)



# for loop with collections
list = ["Ajmal", "Fasil", "Nibras", "Zain", "Selman"]
for i in list:
    print(i)


# for loop with range:-
print("for loop with range:-")
for i in range(2,6): # print from 2 untle 6
    print(i)



i = 1
for _ in iter(int, 1):  # Infinite loop using iter
    if i > 5:
        break
    print("Hello")
    i += 1

