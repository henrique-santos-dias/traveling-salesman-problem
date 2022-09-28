import csv  
import pandas
import numpy
import time

def check_same_signs(value1, value2):
    sign1 = numpy.sign(value1)
    sign2 = numpy.sign(value2)
    
    if (sign1 < 0 and (sign2 == 0 or sign2 > 0)): 
        return False
    if (sign2 < 0 and (sign1 == 0 or sign1 > 0)): 
        return False
    return True

def calculate_distance(x1, y1, x2, y2):

    #checking how to account for difference in longitude
    same_hemisphere = check_same_signs(x1, x2)
    if (same_hemisphere):
        delta_x = numpy.abs(x1 - x2)
    else:
        delta_x = numpy.abs(x1) + numpy.abs(x2)

    #checking how to account for difference in latitude
    same_hemisphere = check_same_signs(y1, y2)
    if (same_hemisphere):
        delta_y = numpy.abs(y1 - y2)
    else:
        delta_y = numpy.abs(y1) + numpy.abs(y2)
        
    distance = numpy.sqrt(delta_x**2 + delta_y**2)
    return distance

def timer(city1, city2):
    tic = time.perf_counter()
    x1 = city1[' Latitude ']
    y1 = city1[' Longitude ']
    x2 = city1[' Latitude ']
    y2 = city1[' Longitude '] 
    toc = time.perf_counter()
    return toc - tic
   
def main():

    data = pandas.read_csv('villes.csv')
    data = data.drop(data.columns[[1, 2, 3, 4, 7]], axis = 1)
    data = data.transpose()
    data = data.to_dict()

    print("As demonstraded in the 'Question 1' section of README, the total running time is approximately equal to (m).(m!).(time to calculate once).")
    print("This means it's usually impractical to calculate when input is equal to or more than '15', on today's average machine. (It's 2022)\n")

    # accessing dict values runs on O(n). average time happens on (sum(i)/n | 1 <= i <= n) = 20.5
    time_to_calc_once = timer(data[20], data[21])
    estimated_total_time = numpy.math.factorial(40) * 40 * time_to_calc_once
    print(f"If you wanted to calculate considering all 40 cities, it would take your computer, running as is, approximately {estimated_total_time:0.4f} seconds.")
    years = str(round(estimated_total_time / (60*60*24*30*12)))
    years_in_sci_not = years[:3]
    years_in_sci_not = (years_in_sci_not[:1] + "." + years_in_sci_not[1:]) + "e" + (str(len(years)-1))
    print(f"That equals to more than {years_in_sci_not} years.\n")

    while True:
        try:
            user_input = int(input("If you'd like an estimated running time for a number of cities of your choice, insert it below: \n"))
            break
        except ValueError:
            print('Sorry, integers only. Try again.\n')

    estimated_total_time = numpy.math.factorial(user_input) * user_input * time_to_calc_once
    print(f"If you wanted to calculate considering all {user_input} cities, it would take your computer, running as is, approximately {estimated_total_time:0.4f} seconds.")
    years = str(round(estimated_total_time / (60*60*24*30*12)))
    years_in_sci_not = years[:3]
    years_in_sci_not = (years_in_sci_not[:1] + "." + years_in_sci_not[1:]) + "e" + (str(len(years)-1))
    if(years_in_sci_not[0] == '0'):
        print("Good news! That doesn't amount to an entire year. Maybe some larger number...?\n")
    else:
        print(f"That equals to more than {years_in_sci_not} years.\n")
    
if __name__ == '__main__':
    main()