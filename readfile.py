with open("merged.py","r") as file:
   content=file.read()
   print("file content \n")
   print(content)
  

with open("merged.py","r") as file:
   for line in file:
      if "list1" in line.lower():
        
       
        print("which only contain list1 \n")
        print(line,end=" ")

   