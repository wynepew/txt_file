with open("./collected_info.txt", "a") as file:
    while True:
        full_name = input("Enter your full name: ")
        age = input("Enter your age: ")
        birthday = input("Enter your birthday: ")
        email_address = input("Enter your email: ")
        phone_number = input("Enter your number: ")

        file.write(f"Full Name: {full_name}")
        file.write(f"Age: {age}")
        file.write(f"Birthday: {birthday}")  
        file.write(f"Email Address: {email_address}")
        file.write(f"Phone Number: {phone_number}")