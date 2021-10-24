import random

def guess(x):
    random_numer = random.randint(1,x)
    num = 0
    print(f"Guess a number between 1 and {x}")
    while abs(num - random_numer) >= 0.001:
        num = int(input("Guess the number: "))
        if abs(num - random_numer)<= 10:
            print("Hot")
        elif abs(num - random_numer)<= 100:
            print("Warm")
        elif abs(num - random_numer)> 100:
            print("Cold")
    print(f"Yayy you correctly guessed the number as {random_numer}")

if __name__ == "__main__":
    guess(1000)                