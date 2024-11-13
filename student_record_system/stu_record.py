class UserRecord:
    def __init__(self,name,age,email,phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def display_record(self):
        print(f"name: {self.name}") #formate printing
        print(f"age: {self.age}")
        print(f"email: {self.email}")
        print(f"phone: {self.phone}")  


class UserRecordSystem:
    def __init__(self):
        self.records = []

    def add_record(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        record = UserRecord(name,age,email,phone)
        self.records.append(record)
        print("Record added successfully")

    def display_records(self):
        if not self.records:
            print("No records found!")
        else:
            for i, record in enumerate(self.records, start=1):
                print(f"Record {i}:")
                record.display_record()
                print()                

def main():
    system = UserRecordSystem()
    while True:
        print("=================================")
        print("USER RECORD SYSTEM")
        print("=================================")
        print("1. Add Record")
        print("2. Display Record")
        print("3. Exit")
        print("=================================")
        choice = input("Enter your choice: ")
        if choice == "1":
            system.add_record()
        elif choice == "2":
            system.display_records()
        elif choice == "3":
            break
        else:
            print("Invaild choice. please choose again.")


if __name__ == "__main__":
    main()