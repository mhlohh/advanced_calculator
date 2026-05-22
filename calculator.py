class AdvancedCalculator:
    def add(self,num1,num2):
        return num1 + num2
    
    def subtract(self,num1,num2):
        return num1 - num2
    
    def multiply(self,num1,num2):
        return num1 * num2
    
    def divide(self,num1,num2):
        return num1/num2
    
    def find_square_root(self,n):

        #1 Start with an arbitrary positive start value x (the closer to the root, the better).
        #2 Initialize y = 1.
        #3 3. Do following until desired approximation is achieved.
        #  a) Get the next approximation for root using average of x and y
        # b) Set y = n/x


        x = n
        y = 1
        e = 0.000001
        while x-y > e:
            x = (x + y)/2
            y = n/x
        return x

    
    def find_factorial(self,n):
        if n == 1 or n == 0:
            return 1
        return n * self.find_factorial(n-1)

    def find_power(self,base, exponent):
        if exponent == 0:
            return 1
        
        if exponent < 0:
            power = 1
            for i in range(exponent):
                power *= 1/base

        else:
            power = 1
            for i in range(exponent):
                power *= base
            return power
    def calculate_simple_interest(self,principle,rate,time):
        si = (principle * rate *time)/100
        return si
    
    def calculate_compound_interest(self,principle, rate, time,periods):
        rate = rate/100
        ci = principle * (self.find_power(1 + (rate/periods),periods*time)-1)
        return ci

    
user = AdvancedCalculator()

try:
    while True:
        print("")
        print("--------------------")
        print("")
        print("Please select an operation")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")
        print("5: find power")
        print("6: factorial")
        print("7: sqrt")
        print("8: Simple Interest")
        print("9: Compound Interest")
        print("10: Exit") 
        x = int(input("Enter choce(1-10): "))
        if x < 1 or x > 10:
            print("Error: The value should be between(1 - 8)")
        if x == 10:
            break
        elif x > 0 and x < 6:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        elif x > 5 and x < 8 :
            num = float(input("Enter number: "))

        if x == 1:
            print("")
            print(f"Result: {num1} + {num2} = {user.add(num1,num2)}")
            print("")
        elif x == 2:
            print("")
            print(f"Result: {num1} - {num2} = {user.subtract(num1,num2)}")
            print("")
        elif x == 3:
            print("")
            print(f"Result: {num1} * {num2} = {user.multiply(num1,num2)}")
            print("")
        elif x == 4:
            if num2 == 0:
                print("")
                print("Error: Cannot divide by zero please try again")
                print("")
            else:
                print("")
                print(f"Result: {num1} / {num2} = {user.divide(num1,num2)}")
                print("")
        elif x == 5:
            print()
            print(f"Result: base{num1} to power{num2} = {user.find_power(num1,num2)}")
            print()

        elif x == 6:
            print()
            print(f"Result: {user.find_factorial(num)}")
            print()
        elif x == 7:
            if num < 0:
                raise(ValueError)
            print("")
            result = user.find_square_root(num)
            print(f"Result: sqrt {num} = {result}")
            print()
        elif x == 8:
            p = int(input("Principle: "))
            r = int(input("Rate: "))
            t = int(input("Time: "))
            print()
            print(f"Principle Interest: {user.calculate_simple_interest(p,r,t)}")
        elif x == 9:
            p = int(input("Principle: "))
            r = int(input("Rate: "))
            t = int(input("Time: "))
            pd = int(input("Periods: "))
            print()
            print(f"Principle Interest: {user.calculate_compound_interest(p,r,t,pd)}")

                
except ValueError:
    raise(ValueError)
except TypeError:
    raise(TypeError)