from patterns.rideBuilder import RideBuilder
#patron de diseño Builder
file = "taxi-data.csv"

def registerRides():
    rides = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            ride_builder = RideBuilder()
            ride_builder.set_taxi_id(row[0])
            ride_builder.set_pick_up_time(row[1])
            ride_builder.set_drop_of_time(row[2])
            ride_builder.set_passenger_count(row[3])
            ride_builder.set_trip_distance(float(row[4]))
            ride_builder.set_tolls_amount(float(row[5]))
            ride = ride_builder.build()
            rides.append(ride)

    return rides

def print_report(rides):
    print("Taxi report: \n")
    for ride in rides:
        _add_ride_to_builder(builder, ride)

    report = "".join(builder)
    print(report)


def _add_ride_to_builder(builder, ride):
    builder.append(f"{ride.taxi_id},{ride.pick_up_time},{ride.drop_of_time},{ride.passenger_count},{ride.trip_distance},{ride.tolls_amount}\n")