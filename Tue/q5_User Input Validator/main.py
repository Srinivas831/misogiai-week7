# User Input Validator
try:
  inp = input("Enter the age:(1-120): ").strip()
  if not inp:
    raise ValueError("Input cannot be empty")
  val = int(inp)
  
  if val>1 and val <=120:
    print("Yo entered a vaild age")
  else:
    print("Out of range")

except ValueError as ve:
  print(f"Value Error: {ve}")
  
except Exception as e:
  print("Error",e)
