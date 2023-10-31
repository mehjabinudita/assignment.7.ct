senders = []

try:
    with open('mbox.txt', 'r') as file:
        for line in file: 
            if line.startswith('From ') and not line.startswith('From:'):
                words = line.split()
                sender = words[1]
                senders.append(sender)
    for sender in senders:
        print(sender)
    print("Total",(len(senders)),"lines were printed")

except FileNotFoundError:
    print("File 'mbox.txt' not found.")
except Exception as e:
    print("An error occurred:", e)
