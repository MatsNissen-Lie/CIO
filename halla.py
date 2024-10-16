import random


solver = pywraplp.Solver.CreateSolver('SCIP')

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

electricityDemand = #noe

transferCapacityCable = 

# Generate random annual kWh production value
random_kwh = random.uniform(21_000_000, 52_500_000)
print(f"Random annual kWh production: {random_kwh}")

# Generate random daily kWh production value
random_daily_kwh = random.uniform(57_500, 144_000)
print(f"Random daily kWh production: {random_daily_kwh}")


