# # Written by Kamran Bigdely
# # Example for Compose Methods: Extract Method.
# import math
import math

class Stat:
    def __init__(self, grades = []):
        self.grade_list = []

        for grade in grades:
            self.grade_list.append(grade)

    def inputs(self):
        n_students = 5
        for _ in range(0, n_students):
            self.grade_list.append(int(input('Enter a number: ')))
        return self.prints()
    
    def mean(self):
        total_grade = 0
        for grade in self.grade_list:
            total_grade += grade
        # calculate the mean
        return total_grade / len(self.grade_list)

    def stand_dev(self, mean):
        sum_of_sqrs = 0
        for grade in self.grade_list:
            sum_of_sqrs += (grade - mean) ** 2
        return math.sqrt(sum_of_sqrs / len(self.grade_list)) 

    def prints(self):
        mean = self.mean()
        sd = self.stand_dev(mean)
        print('\n****** Grade Statistics ******')
        print("The grades's mean is:", mean)
        print('The population standard deviation of grades is: ', round(sd, 3))
        print('****** END ******')

Stat().inputs()