# GUIUAN, Trini Andrea - APPDAET Midterms
# Fully committed to git! :)

participants = []

#task 1: registration setup
print("Welcome to SMIT TechFest!\nOrganized by Trini Andrea Guiuan of APPDAET BTCS1")

participants_count = int(input("\nHow many participants will register? "))
if participants_count <= 0:
    print("Invalid number of participants.")
    exit()

#task 2: collect participant information
for i in range(participants_count):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")

    participants_info = {
        "name": name,
        "track": track
    }

    participants.append(participants_info)

print("\nRegistered Participants:")
for i in range(len(participants)):
    print(f"{i + 1}. {participants[i]['name']} - {participants[i]['track']}")
