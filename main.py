
vowels=("a","e","i","o","u","y")#use tuple since this won't change and faster for using "in" method


message=input("What do you want to translate to pig latin?: ")
msg_list=message.split(" ")
#print(msg_list)

new_list=[]
for word in msg_list:
  first_letter=word[0]
  #separate non letters at the beginnig of word
  prefix_non_letters=""
  while len(word)>0 and not word[0].isalpha():
    prefix_non_letters+=word[0]
    word=word[1:]
  if len(word)==0:
    new_list.append(prefix_non_letters)
    continue
  #separate non letters at the end of the word
  suffix_non_letters=""
  while not word[-1].isalpha():
    suffix_non_letters+=word[-1]
    word=word[:-1]
  #create two variables to check if upper or title cases
  was_upper=word.isupper()
  was_title=word.istitle()
  word=word.lower()
  #words that starts with consonants
  prefix_consonant=""
  if not word[0] in vowels:
    prefix_consonant+=word[0]
    word=word[1:]
  if prefix_consonant!=0: #check to see if vowel, vowel means it is empty
    word+=prefix_consonant+"ay"
  else:
    word+="yay"
  if was_upper:
    word=word.upper()
  if was_title:
    word=word.title()
  #add non letters back to start and end of word
  new_list.append(prefix_non_letters+word+suffix_non_letters)
print(" ".join(new_list))