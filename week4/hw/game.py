from random import randint
while True:
    try:
        n = int(input("Level: "))
        if n <= 0 or n > 100:
            raise ValueError
        break
    except ValueError:
        pass

Key = randint(1,n)
low , high = 1 , n
while True:
    try:
        guess = int(input("Guess: "))
        if guess < low or guess > high:
            raise ValueError
        if guess == Key:
            print("Just right!")
            break
        elif guess < Key:
            low = guess
            print("Too small!")
        else :
            high = guess
            print("Too large!")
    except ValueError:
        pass
