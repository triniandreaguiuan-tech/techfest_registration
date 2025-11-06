# GUIUAN, Trini Andrea - APPDAET Midterms
# Fully committed to git! :)

participants = []

#task 1: registration setup
print("Welcome to SMIT TechFest!\nOrganized by Trini Andrea Guiuan of APPDAET BTCS1")
participants_count = int(input("How many participants will register? "))
if participants_count.isdigit():
    participants_count = int(participants_count)
    if participants_count <= 0:
        print("Invalid number of participants.")
        exit()
else:
    print("Invalid input. Please enter a number!\n")
