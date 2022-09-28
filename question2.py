import numpy

def metropolis(user_input):
    x = sigma0
    for i in user_input:
        t = t[i]
        sigma = x
        

def main():

    while True:
        try:
            user_input = int(input("Insert amount of iterations for simulation: \n"))
            break
        except ValueError:
            print('Sorry, integers only. Try again.\n')

    metropolis(user_input)
    
if __name__ == '__main__':
    main()