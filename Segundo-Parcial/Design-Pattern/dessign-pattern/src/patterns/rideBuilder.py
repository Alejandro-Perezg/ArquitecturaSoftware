from patterns.csv_utils import Ride


class RideBuilder:
    def __init__(self):
        self.taxi_id = None
        self.pick_up_time = None
        self.drop_of_time = None
        self.passenger_count = None
        self.trip_distance = None
        self.tolls_amount = None

    def set_taxi_id(self, taxi_id):
        self.taxi_id = taxi_id

    def set_pick_up_time(self, pick_up_time):
        self.pick_up_time = pick_up_time

    def set_drop_of_time(self, drop_of_time):
        self.drop_of_time = drop_of_time

    def set_passenger_count(self, passenger_count):
        self.passenger_count = passenger_count

    def set_trip_distance(self, trip_distance):
        self.trip_distance = trip_distance

    def set_tolls_amount(self, tolls_amount):
        self.tolls_amount = tolls_amount

    def builder(self):
        ride = Ride(
            taxi_id=self.taxi_id,
            pick_up_time=self.pick_up_time,
            drop_of_time=self.drop_of_time,
            passenger_count=self.passenger_count,
            trip_distance=self.trip_distance,
            tolls_amount=self.tolls_amount,
        )
        return ride