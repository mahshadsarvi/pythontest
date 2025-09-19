import random
def main():
    n=get_level()
    score=0
    for i in range(10):
        try:
            f= int(generate_integer(n))
            s= int(generate_integer(n))
            z= f+s
            ans=int(input(f"{f} + {s} ="))
            if ans == z:
                score+=1
            else:
                print("EEE")
                for j in range(2):
                    ans=int(input(f"{f} + {s} ="))
                    if ans ==z:
                        break
                    else:
                        print("EEE")
                        j=j+1
                        if j==3:

                            score-=1
                print(f"{f} + {s}=",z)

        except ValueError:
            print("EEE")
            ans=int(input(f"{f} + {s} ="))
            continue
    print(score)
def get_level():
    while True:
        try:
            level=int(input(""))
            if 3>=level>0:
                break
        except:
            continue
    return level

def generate_integer(level):
    if level==1:
        x = random.randint(0,9)
        return x
    if level==2:
        x = random.randint(10,99)
        return x
    if level==3:
        x = random.randint(100,999)
        return x

if __name__=="__main__":
    main()

