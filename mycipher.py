import sys

shift =int(sys.argv[1])
message = ""
for line in sys.stdin:
    message += line.strip()
message = message.upper()

message = ''.join([char for char in message if char.isalpha()])

hidden_message = ""
for char in message:
    if 'A' <= char <= 'Z':
        new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        hidden_message += new_char

for i in range(0, len(hidden_message), 5):
    print(hidden_message[i:i+5], end=" ")
