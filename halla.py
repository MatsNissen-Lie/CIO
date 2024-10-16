import random


solver = pywraplp.Solver.CreateSolver('SCIP')

##Define the indexes
#i = park
#l = transmission cable

## Define the constants

#Production of electricty from a wind turbine in park i
ElectricityProduction = 0 

#Cost per wind turbine
costPerWindmill = []

#Upper bound on number of windmill in each park
upperBound = []

#Different types of transmission cables
transmissionCablea = []

#Cost for tranmission cable L for wind turbine park i
costPerCable = []

#Transmission capacity of cable L
transmissionCapacity = 0#noe

#Requirement for quantum of delivered power
deliveredPower = 0

##Define the variables
#Number of windmills in park i, i = 1,2,3,4,...,n
X_i = 0 

#1 if cable l is used for park i, 0 otherwise, l = 1,2,3,4,...,L
S_il = 0

# Generate random annual kWh production value
random_kwh = random.uniform(21_000_000, 52_500_000)
print(f"Random annual kWh production: {random_kwh}")

# Generate random daily kWh production value
random_daily_kwh = random.uniform(57_500, 144_000)
print(f"Random daily kWh production: {random_daily_kwh}")
