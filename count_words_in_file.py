word_count=0
freq={}


with open("merged.py","r")as file:
     for line in file:
          words=line.split()
          word_count+=len(words)


          for w in words:
               w=w.lower()
               freq[w]=freq.get(w,0)+1


most_repeated=max(freq,key=freq.get)

print("total words :",word_count)
print("most repeated word :",most_repeated,"-->",freq[most_repeated],"times")
               