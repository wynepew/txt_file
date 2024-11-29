with open("./collected_info.txt", "a") as file:
    while True:
        full_name = input("Enter your full name: ")
        age = input("Enter your age: ")
        birthday = input("Enter your birthday: ")
        email_address = input("Enter your email: ")
        phone_number = input("Enter your number: ")

        file.write(f"Full Name: {full_name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Birthday: {birthday}\n")  
        file.write(f"Email Address: {email_address}\n")
        file.write(f"Phone Number: {phone_number}\n")

        add_person = input("\nDo you want to enter another info for a new person? (yes/no): ")
        if add_person != "yes":
            print("Thank you for your cooperation!")

            break