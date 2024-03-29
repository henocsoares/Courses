'''
Display the following message:

1) Square 
2) Triangle 

Enter a number: 

If the user enters 1, then it should ask them for the length of one of its sides and display
the area. If they select 2, it should ask for the base and height of the triangle and display
the are. If they type in anything else, it should give them a suitable error message.
'''
import math

choice = 0

while choice != 1 and choice != 2:
  choice = int(input("1) Square\n2) Triangle\n\nEnter a number: "))
  if choice == 1:
    sideLength = float(input("Provide now the length of one of its side: "))
    area = pow(sideLength, 2)
    print(f"Area: {area:.2f}")
  elif choice == 2:
    base = float(input("Provide the base value: "))
    height = float(input("Provide the height value: "))
    area = 0.5 * base * height
    print(f"Area: {area:.2f}")
  else:
    print("Invalid choice. Please choose between options 1 and 2: ")
