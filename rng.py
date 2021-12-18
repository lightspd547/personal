import time

print("Random number generator")
first_input = int(input("Enter lowest number: "))
second_input = int(input("Enter highest number: "))

def random_number():
  timestamp = str(time.time())
  start = int(len(timestamp) - 2)
  first_value = int(timestamp[start:])
  second_value = str(first_value / 3.14159265359)
  second_start = int(len(second_value) - 2)
  output = int(second_value[second_start:])
  changed_output = ((second_input - first_input)/99) * output
  real_output = round(changed_output + first_input)
  return real_output

real_output = random_number()
print("Your number is: " + str(real_output))