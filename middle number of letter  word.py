

#middl number of word letter 
word=input("enter word: ")

letter_count=len(word)

mid = letter_count//2

if(letter_count %2==0):
    print(word[mid-1]+word[mid])
else:
  print(word[mid])
    