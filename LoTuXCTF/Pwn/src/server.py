import random, sys

def main():
    round1()

def round1():
    password = random.randint(0, 10000000)
    print("Guess the number as soon as possible!")
    i = -1
    while(i!=password):
        try:
            i = int(input())
        except:
            break
        if(i == password):
            print("Round 1 clear!")
            round2()
        elif(i > password):
            print("lower!")
        elif(i < password):
            print("higher!")
        else:
            print("")

def round2():
    print("Answer 100 math questions.")
    for i in range(101):
        a = random.randint(1,10)
        b = random.randint(1,10)
        answer = int(input(f'{a}+{b}='))
        if(answer != a+b):
            break
        if(i == 100):
            print("LoTuX{THIS_IS_A_FAKE_FLAG}")

if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()
