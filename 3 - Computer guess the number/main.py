import random

def guess(x):
    num = 0
    low=1
    high=1000
    while num != x:
     print(f'Low: {low} & High: {high}')   
     if low!=high:    
        num = random.randint(low,high)
     else:
        num = low      
     inp = input(f"Is my guess, {num}, too high (H) or low (L) or correct (C) or 'reset'?").lower()
     if inp == 'h':
        high=num-1
        print('Updating high')
     elif inp == 'l':
        low=num+1
        print('Updating low')
     elif inp == 'reset':
        low=1
        high=1000
        print('Reseting range')   
     elif inp == 'c':
        print('Exiting')
        break        
    print(f"Yayy I correctly guessed your number as {num}")

if __name__ == "__main__":
    x=int(input('Give me a number to guess: '))
    guess(x)                