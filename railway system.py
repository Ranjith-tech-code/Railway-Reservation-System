class RailwayReservation:
    def _init_(self):
        self.passengers = []
        self.ticket_count = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100}
        self.trains = {
            1: {"name": "Gatiman Express", "time": "9:00 am", "price": 2500},
            2: {"name": "Shatabdi Express", "time": "11:30 am", "price": 2000},
            3: {"name": "Rajdhani Express", "time": "2:00 pm", "price": 1500},
            4: {"name": "Vande Bharat Express", "time": "4:00 pm", "price": 1200},
            5: {"name": "Duronto Express", "time": "9:00 pm", "price": 1000},
        }

    def menu(self):
        while True:
            print("\n\tRailway Reservation System")
            print("\t1. Book Ticket")
            print("\t2. Cancel Ticket")
            print("\t3. Search Passenger")
            print("\t4. Display Reservation Chart")
            print("\t5. Display Unbooked Tickets")
            print("\t6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.book_ticket()
            elif choice == 2:
                self.cancel_ticket()
            elif choice == 3:
                self.search_passenger()
            elif choice == 4:
                self.display_chart()
            elif choice == 5:
                self.display_unbooked()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")

    def book_ticket(self):
        print("\nAvailable Routes:")
        print("1. Ahmedabad - Mumbai")
        print("2. Ahmedabad - Delhi")
        print("3. Ahmedabad - Kolkata")
        print("4. Ahmedabad - Goa")
        print("5. Ahmedabad - Chennai")

        route_choice = int(input("Enter your route choice: "))
        if route_choice not in range(1, 6):
            print("Invalid route choice!")
            return

        print("\nAvailable Trains:")
        for key, train in self.trains.items():
            print(f"{key}. {train['name']} --- {train['time']} --- Rs {train['price']}")

        train_choice = int(input("Enter your train choice: "))
        if train_choice not in self.trains:
            print("Invalid train choice!")
            return

        num_tickets = int(input("Enter the number of tickets: "))
        if self.ticket_count[train_choice] >= num_tickets:
            for _ in range(num_tickets):
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                phone = input("Enter your phone number: ")
                self.passengers.append({
                    "name": name,
                    "age": age,
                    "phone": phone,
                    "train": self.trains[train_choice]["name"],
                })
                self.ticket_count[train_choice] -= 1

            total_price = self.trains[train_choice]["price"] * num_tickets
            print(f"\nTickets successfully booked! Total price: Rs {total_price}")
        else:
            print("Not enough tickets available!")

    def cancel_ticket(self):
        phone = input("Enter your phone number to cancel ticket: ")
        for passenger in self.passengers:
            if passenger["phone"] == phone:
                self.passengers.remove(passenger)
                train_name = passenger["train"]
                train_choice = next(
                    key for key, value in self.trains.items() if value["name"] == train_name
                )
                self.ticket_count[train_choice] += 1
                print("Ticket successfully cancelled!")
                return
        print("Passenger not found!")

    def search_passenger(self):
        phone = input("Enter passenger's phone number: ")
        for passenger in self.passengers:
            if passenger["phone"] == phone:
                print("\nPassenger Details:")
                print(f"Name: {passenger['name']}")
                print(f"Age: {passenger['age']}")
                print(f"Phone: {passenger['phone']}")
                print(f"Train: {passenger['train']}")
                return
        print("Passenger not found!")

    def display_chart(self):
        print("\nReservation Chart:")
        for train in self.trains.values():
            print(f"\nTrain: {train['name']}")
            print("Passengers:")
            count = 0
            for passenger in self.passengers:
                if passenger["train"] == train["name"]:
                    print(f"  Name: {passenger['name']}, Age: {passenger['age']}, Phone: {passenger['phone']}")
                    count += 1
            if count == 0:
                print("  No passengers")

    def display_unbooked(self):
        print("\nUnbooked Tickets:")
        for key, count in self.ticket_count.items():
            print(f"{self.trains[key]['name']}: {count} tickets available")


if _name_ == "_main_":
    system = RailwayReservation()
    system.menu()