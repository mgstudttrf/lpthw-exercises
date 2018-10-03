cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars * space_in_a_car
average_passengers_in_car = passengers / cars_driven
print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("Ther will be", cars_not_driven, "empty cars today")
print("we xan transfer", carpool_capacity, "people today")
print("we have", passengers, "to carpool tday")
print("We need to put about", average_passengers_in_car, "people in car today")
