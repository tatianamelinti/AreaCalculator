print ("The program is running")
def getshape(option): 
  print("You can choose circle, square, or triangle:")
  option=input("Enter C for Circle,S for Square, or T for Triangle:")
  if option=='C':
    radius = float(input("input the radius:"))
    area = 3.14159 * radius**2
    print ("Area: %f" % area)
  
  elif option =='T':
    base = float(input("input the base:"))
    height = float(input("input the height:"))
    area = 0.5 *base * height
    print ("Area: %f" % area)
    
  elif option =='S':
    side = float(input("input the side length:"))
    area = side**2
    print ("Area: %f" % area)
  else:
    print ("Error! Invalid shape.")
getshape("option") 
def getanswer(userinput):
  userinput=input("Type con to continue or ex to exit:")
  if userinput=="con":
    getshape("option")
  elif userinput=="ex":
    print ("Exiting...")
  else:
    print("error! Invalid input")
    
getanswer("userinput")
getanswer("userinput")
