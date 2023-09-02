

def water_collection(rainfall, runOff, catchmentArea):
    waterAmount = rainfall * runOff * catchmentArea
    return round(waterAmount, 2)

def annual_demand(population, dailyConsumption):
    annualDemand = population * dailyConsumption * 365
    return annualDemand


rainfall = [2382.4, 2125, 2007.4, 1731, 1983.7, 1259, 1588.7, 1439.5, 1668.9, 2193.8, 2391.8, 1759.3]
runOff = 0.8
catchmentArea = 83967.6

for data in rainfall:
    print(water_collection(data, runOff, catchmentArea))


# print(annual_demand(70, 15))

