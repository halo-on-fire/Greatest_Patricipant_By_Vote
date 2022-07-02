participants = []

numberOfParticipants = int(input("Please Enter number of participants: "))

for i in range(numberOfParticipants):
    participant = {}
    participantName = input("Enter Name of participant: ")
    participantAge = int(input("Age ov Participant: "))
    participantVote = int(input("Number of vote of participant : "))
    
    participant['name'] = participantName
    participant['age'] = participantAge
    participant['vote'] = participantVote
    
    participants.append(participant)
    
    
participants = sorted(participants, key = lambda i : i['vote'], reverse = True)

print(participants[0], participants[1])