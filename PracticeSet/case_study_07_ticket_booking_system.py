# List to store passengers
passengers = []

# Seats available
seats = 3

# Function to calculate fare
def fare_calc(age, distance):
    fare = distance * 2   # base fare

    if age < 12:
        fare = fare * 0.5   # child discount
    elif age > 60:
        fare = fare * 0.7   # senior discount

    return fare

# Booking function
def book():
    global seats

    if seats == 0:
        print("No seats available")
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance: "))

    fare = fare_calc(age, distance)

    # Store data in dictionary
    data = {"name": name, "fare": fare}
    passengers.append(data)

    seats -= 1   # reduce seat

    print("Booked! Fare:", fare)

# Run program
book()
book()

print("\nPassengers:", passengers)