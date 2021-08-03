class Calculator:

    def __init__(self, milesTravelled, litresOfFuel):

        self.milesTravelled = milesTravelled
        self.litresOfFuel = litresOfFuel


    def mpgcalculator(self):
        litresInGallon = 4.546

        milesTravelled = int(input("Enter the number of miles travelled: "))
        litresOfFuel = int(input("Enter the number of litres added: "))

        numberOfGallons = litresOfFuel / litresInGallon
        mpg = milesTravelled / numberOfGallons

        print("Your MPG is: ", mpg)



