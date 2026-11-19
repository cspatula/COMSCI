def formatlist(arr):
  userinput = ""
  origlist = []

  while userinput != "done":
    userinput = input("what do you want in your list type "done" if finished: ")
    if userinput == "done":
      break
      
      else:
        userinput.append("")

print formatlist(userinput)
