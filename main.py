consonants=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
vowels=["A","E","I","O","U"]


message=input("What do you want to translate to pig latin?: ")
msg_list=message.split(" ")
print(msg_list)
new_word=""
new_list=[]
for word in msg_list:
  first_letter=word[0]
  
  if first_letter.upper() in consonants:
    if first_letter.isupper():
      new_word=word[1:].capitalize()+first_letter.lower()+"ay"
    else:
      new_word=word[1:]+first_letter+"ay"
    #print(new_word)
  elif first_letter.upper() in vowels:
    new_word=word+"yay"
    #print(new_word)
  new_list.append(new_word)
  new_string=(" ").join(new_list)
print(new_string)
