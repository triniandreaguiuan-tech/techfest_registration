# GUIUAN, Trini Andrea - APPDAET Midterms
# Fully committed to git! :)
from multiprocessing.reduction import duplicate

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

#task 3: track diversity report
print("\nTracks offered in this event: \nCybersecurity, Data, Game Dev, Information\n")
csec = 0
data = 0
gameDev = 0
inform = 0

for p in participants:
    if p["track"] == "Cybersecurity":
        csec += 1
    elif p["track"] == "Data":
        data += 1
    elif p["track"] == "Game Dev":
        gameDev += 1
    elif p["track"] == "Information":
        inform += 1

#task 4: duplicate name detection
names = set()
duplicate = False

for p in participants:
    if p["name"] in names:
        print("Duplicate name found:", p["name"])
        duplicate = True
    else:
        names.add(p["name"])
if not duplicate:
    print("No duplicate names.")