import random


def show(random_numbers):
    for number in random_numbers:
        print(":)")
        print(number)
        print("=======graphs========")

def random_generator(limit):
    random_numbers=[]
    for i in range(limit):
        number=random.randint(1,10)
        random_numbers.append(number)
    return random_numbers


def start():
    limit=int(input("Ingrese el límite de números aleatorios: "))
    random_numbers=random_generator(limit)
    show(random_numbers)

def run():
    start()


if __name__=='__main__':
    run()