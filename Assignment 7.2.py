unique_words = set()

try:
    with open('romeo.txt', 'r') as file:
        for line in file:
            words = line.split()
            unique_words.update(words)

    
    unique_words = sorted(unique_words)


    for word in unique_words:
        print(word)

except FileNotFoundError:
    print("File 'romeo.txt' not found.")
except Exception as e:
    print("An error occurred:", e)
