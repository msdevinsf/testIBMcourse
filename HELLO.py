message = input("> ")
words = message.split(' ')
emojis = {
    ":-)":"😊smile",
    ":-(":"😒sad"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)










