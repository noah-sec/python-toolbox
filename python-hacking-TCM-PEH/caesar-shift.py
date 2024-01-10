def caesar(message, key, mode):
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  translated = ''
  message = message.upper()
  key = key % 26

  for i in message:
    templetter = LETTERS.find(i)
    if mode == 'encrypt':
      templetter += key
    elif mode == 'decrypt':
      templetter -= key
    if templetter >= len(LETTERS):
      templetter -= len(LETTERS)
    elif templetter < 0:
      templetter += len(LETTERS)
      
    translated += LETTERS[templetter]
  return translated

print(caesar("NoahDawg", 6, 'encrypt'))
print(caesar("TUGNJGCM", 6, 'decrypt'))