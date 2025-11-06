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
uniqueTracks_offered = {p["track"] for p in participants}

print("\nTracks offered in this event:\n", ", ".join(uniqueTracks_offered))
tracks_count = {track: 0 for track in uniqueTracks_offered}

#task 4: duplicate name detection
names = set()
duplicate = False

for p in participants:
    if p["name"] in names:
        print("\nDuplicate name found:", p["name"])
        duplicate = True
    else:
        names.add(p["name"])
if not duplicate:
    print("No duplicate names.")

#task 5: track summary report
print("\nParticipants per track:")
for p in participants:
    tracks_count[p["track"]] += 1

print()
for track, count in tracks_count.items():
    print(f"{track}: {count}")

if len(uniqueTracks_offered) < 2:
    print("\nNot enough variety in tracks.")