import sys

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
                words.append({'word': sentence, 'meaning': meaning})
        else:
            # Type (1): 英単語 日本語
            parts = line.split(' ', 1)
            if len(parts) == 2:
                word = parts[0]
                meaning = parts[1]
                words.append({'word': word, 'meaning': meaning})

    for word_entry in words:
        print(f"Word: {word_entry['word']}, Meaning: {word_entry['meaning']}")