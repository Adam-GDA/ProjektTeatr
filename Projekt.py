#klasa Miejsca Teatralne
#Klasa bazowa

class TheaterSeats:
    def __init__(self,number,price,availability):
        self.number = number
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Seat number {self.number}, Price: {self.price}, Availability: {"available" if self.availability else "Reserved"}"


#klasy pochodne

class RegularSeats(TheaterSeats):
    def __init__(self,number,price,availability):
        super().__init__(number, price, availability)


class VIPSeats(TheaterSeats):
    def __init__(self,number,price,availability,extra_fee,VIP_amenities):
        super().__init__(number, price + extra_fee,availability)
        self.extra_fee = extra_fee
        self.VIP_amenities = VIP_amenities


class HandicapSeats(TheaterSeats):
    def __init__(self,number,price,availability, amenities):
        super().__init__(number, price,availability)
        self.amenities = amenities

    def __str__(self):
        return super().__str__() + f", Amenities: {self.amenities}"

#klasa Teatr

class Theater:
    def __init__(self):
        self.seat = []
        self.rezervasion = {}


    def add_seat (self,miejsce):
        self.seat.append(miejsce)

    def show_free_seats (self):
        return [booking for booking in self.seat if booking.availability]

    def seat_reservation(self, number, customer):
        for booking in self.seat:
            if booking.number == number and booking.availability:
                booking.availability = False
                if customer.id not in self.rezervasion:
                    self.rezervasion[customer.id] = []
                self.rezervasion[customer.id].append(booking)
                return True
        return False

    def seat_cancellation(self,number, customer):
        if customer.id in self.rezervasion:
            for booking in self.rezervasion[customer.id]:
                if booking.number == number:
                    booking.availability = True
                    self.rezervasion[customer.id].remove(booking)
                    return True
        return False

    def history_reservation(self,customer):
        if customer.id in self.rezervasion:
            return self.rezervasion[customer.id]
        return []


#Klasa Klient

class Customer:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname


    def __str__(self):
        return f"Customer's ID {self.id}, Name:{self.name} Surname:{self.surname}"


theater = Theater()

theater.add_seat(RegularSeats(1,50,True))
theater.add_seat(RegularSeats(2,50,True))
theater.add_seat(RegularSeats(3,50,True))
theater.add_seat(RegularSeats(4,50,True))
theater.add_seat(RegularSeats(5,50,True))
theater.add_seat(RegularSeats(6,50,True))
theater.add_seat(RegularSeats(7,50,True))
theater.add_seat(RegularSeats(8,50,True))
theater.add_seat(RegularSeats(9,50,True))
theater.add_seat(RegularSeats(10,50,True))

theater.add_seat(VIPSeats(11,50,True,50,"Drink + popcorn, more space"))
theater.add_seat(VIPSeats(12,50,True,50,"Drink + popcorn, more space"))
theater.add_seat(VIPSeats(13,50,True,50,"Drink + popcorn, more space"))
theater.add_seat(VIPSeats(14,50,True,50,"Drink + popcorn, more space"))
theater.add_seat(VIPSeats(15,50,True,50,"Drink + popcorn, more space"))

theater.add_seat(HandicapSeats(16,30,True,"more space, closer to exit"))
theater.add_seat(HandicapSeats(17,30,True,"more space, closer to exit"))
theater.add_seat(HandicapSeats(18,30,True,"more space, closer to exit"))
theater.add_seat(HandicapSeats(19,30,True,"more space, closer to exit"))
theater.add_seat(HandicapSeats(20,30,True,"more space, closer to exit"))

#utworzenie klienta
Customer1 = Customer(1969,"Monthy","Python")
Customer2 = Customer(1998,"Karol","Krawczyk")

available_seats = theater.show_free_seats()
for miejsce in available_seats:
    print(miejsce)

#Rezerwacja
theater.seat_reservation(10, Customer1)
theater.seat_reservation(12, Customer2)

history = theater.history_reservation(Customer1)
for booking in history:
    print(booking)

history = theater.history_reservation(Customer2)
for booking in history:
    print(booking)

