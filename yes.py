def yes():
  while True:
    yield "sim"

print("".join(yes()))
