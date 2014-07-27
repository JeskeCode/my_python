cars = 100
space_in_car = 4.0
drivers = 30
passenger = 90
cars_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passenger / cars_driven

print "There are", cars, "cars avalible"
print "There are only",  drivers, "drivers avalible"