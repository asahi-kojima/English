import sys
import random

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_practice.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

    lines = [line for line in content.split('\n') if line.strip()]

    words = []

    for line in lines:
        if line.startswith('"'):
            # Type (2): "英文" 日本語
            parts = line.split('" ')
            if len(parts) == 2:
                sentence = parts[0][1:]  # Remove leading "
                meaning = parts[1]
                words.append([sentence,meaning])
        else:
            # Type (1): 英単語 日本語
            parts = line.split(' ', 1)
            if len(parts) == 2:
                word = parts[0]
                meaning = parts[1]
                words.append([word,meaning])

    if len(words) == 0:
        print("no entries available")
        exit()

    print(f"loaded {len(words)} words. Press Enter to reveal Japanese, Q to quit.")
    idx = random.randrange(len(words))
    current_eng, current_jp = words[idx]
    print(f"\n{current_eng}",end="")

    while True:
        user_input = input("").strip()
        if user_input.lower() == "q":
            print("bye")
            break

        print(f"{current_jp}")
        user_input = input("").strip()
        idx = random.randrange(len(words))
        current_eng, current_jp = words[idx]
        print(f"\n\n\n\n{current_eng}",end="")