with open("./find_full_name", "a") as file:
    while True:
        full_name = input("Enter your name: ")

        file.write(f"Full Name: {full_name}\n")
        file.write("-" * 60 + "\n")

        add_name = input("\nDo you want to enter another name? (yes/no): ")
        if add_name != "yes":
            print("Thank you for your cooperation!")

            break

with open("./find_full_name", "r") as file:
    lines = (file.readlines())
    for line in lines:
        print(line)


