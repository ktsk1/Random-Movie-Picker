import random

select = input("This is a random movie picker. ----- FOR RANDOM -> TYPE 1 , FOR RANDOM BY FIRST LETTER -> TYPE 2 ")
if select == "1":
    randomize = print("Picking a movie...")
    with open("movies.txt") as f:
        lines = f.readlines()
        print (random.choice(lines))
elif select == "2":
    letter = input("Choose a letter: ")
    with open("movies.txt") as f:
         movies = f.readlines()
         filtered_movies = list(filter(lambda m: m[0].lower() == letter.lower(), movies))
         print(random.choice(filtered_movies))
else:
    print("The options are only 1 and 2.")        