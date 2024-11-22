import time, os

def clear(): 
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')

clear()

def load_sentences(file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

def typing_test(sentences):
    print("Typing Test: Type the following sentences as quickly and accurately as you can.")
    total_time = 0
    total_chars = 0

    for sentence in sentences:
        print("\nType this sentence:")
        print(sentence)
        input("Press Enter when you are ready to start...")

        start_time = time.time()
        user_input = input()
        end_time = time.time()

        elapsed_time = end_time - start_time
        total_time += elapsed_time
        total_chars += len(sentence)

        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Your input: {user_input}")
        print(f"Correct: {user_input == sentence}")

    typing_speed = total_chars / (total_time + 0.000000000000000001)*60
    print(f"\nYour typing speed is {typing_speed:.2f} characters per minute.")

if __name__ == "__main__":
    sentences = load_sentences('sentences.txt')
    typing_test(sentences)
