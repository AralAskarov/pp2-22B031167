# Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print()
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")