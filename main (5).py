#Hillel homework
#TASK: Implement a digital counter class. Provide the ability to set the maximum and minimum values,
# increment the counter by 1, return the current value.



class Counter:
    name = 'counter'

    def __init__(self, minval, maxval, currentval):
        self.minval = minval
        self.maxval = maxval
        self.currentval = currentval

    def print_counter(self):
        print('min =', self.minval, 'max =', self.maxval, 'current =', self.currentval)

    def plus(self):
        if self.currentval < self.maxval:
            self.currentval += 1
        else:
            print('Error: counter cannot be greater than: ', self.maxval)
    def minus(self):
        if self.currentval > self.minval:
            self.currentval -= 1
    def reset(self):
        self.currentval = self.minval
        return self.reset


minval1 = int(input('Enter the minimum value:'))
maxval1 = int(input('Enter the maximum value:'))
currentval1 = 0

counter1 = Counter(minval1, maxval1, currentval1)

for minval1 in range(maxval1):
    counter1.plus()
    counter1.print_counter()
counter1.reset()
print('Returning the original value, current: ', counter1.currentval)











