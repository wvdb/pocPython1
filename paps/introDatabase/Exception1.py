try:
  f = open("demofile.txt", "r")
  for x in f:
    print(x, end='')
except Exception as e:
  print("Something went wrong when reading the file. Exception: ", e)
else:
  f.close()