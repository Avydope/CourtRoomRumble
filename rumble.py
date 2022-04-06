class Lawyer:
  def __init__(self,name,power):
    self.name = name
    self.power = power
    
  def grow(self):
    self.power += 2
    
  def suit(self, enemy):
    self.power -= 2 
    enemy.power -= 4
    
  def __repr__(self):
    return "You, {name} are a Lawyer. You have {power} power points \n".format( name = self.name, power = self.power)


class Judge:
  def __init__(self,name,exp):
    self.name = name
    self.exp = exp 
    self.biase = False

  def __repr__(self): 
    return "You, {name} are a Judge. You have {power} power points \n".format( name = self.name, power = self.power)

  def grow(self):
    self.exp += 2

  def defame(self):
    self.exp -= 2


inp1 = raw_input("Welcome to the game! Please enter a name for player one and hit enter: ")
inp2 = raw_input("Please enter a name for player two and hit enter: ")

lawyer_one = inp1
lawyer_two = inp2

inpx = int(input("Specify power points for P1 : "))
inpy = int(input("specify power points for P2 : "))

lawyer_one = Lawyer(lawyer_one, inpx)
lawyer_two = Lawyer(lawyer_two, inpy)

print("\nLet us commence!")
stat = "Status: Lawyer 1: {name1}, with {power1} points || \nLawyer 2: {name2}, with {power2} points".format(name1=lawyer_one.name,power1=lawyer_one.power,name2=lawyer_two.name,power2=lawyer_two.power)
print(stat)

judge_one = 'David'
judge_two = 'Trouy'

judge_one = Judge(judge_one, 2)
judge_two = Judge(judge_two, 4)

judge_chosen = Judge('judge_sam', 0);

dexp = int(judge_one.exp)
jexp = int(judge_two.exp)

hel = True
print("Judge D has {dexp} while J has {jexp} experience".format(dexp = judge_one.exp,jexp = judge_two.exp))
print("doesn't really matter yet")
while hel:
  input3 = int(input("Choose one (1 for D, 2 for J) : "))
  if input3 == 1: 
    print("You chose Dave!")
    hel=False
  elif input3 == 2:
    print("You chose Jack!")
    hel=False
  else:
    hel = True

# print("Lawyer 1: {power}".format(power=lawyer_one.power))
# print("Lawyer 2: {power}".format(power=lawyer_two.power))

# heli = True
# while heli:
#   input34 = int(input("Type 1 for Grow or 2 to Suit for Lawyer 1: "))
#   if input34 == 1: 
#     lawyer_one = Lawyer(lawyer_one, 3, 4)
#     lawyer_two = Lawyer(lawyer_two, 5, 6)
#     print("{name}, you chose to grow!".format(name=lawyer_one.name))
#     lawyer_one.grow()
#     heli=False
#   elif input34 == 2:
#     print("You chose to suit!")
#     lawyer_one.suit(lawyer_two)
#     heli=False
#   else:
#     heli= True

# print("Lawyer 1: {power}".format(power=lawyer_one.power))
# print("Lawyer 2: {power}".format(power=lawyer_two.power))

# cont = True
# while cont:
#   input45 = int(input("Type 1 for Grow or 2 to Suit for Lawyer 2: "))
#   if input45 == 1: 
#     # lawyer_one = Lawyer(lawyer_one, 3, 4)
#     # lawyer_two = Lawyer(lawyer_two, 5, 6)
#     print("You chose to grow!")
#     lawyer_two.grow()
#     cont=False
#   elif input45 == 2:
#     print("You chose to suit!")
#     lawyer_two.suit(lawyer_one)
#     cont=False
#   else:
#     cont= True

print("Lawyer 1: {power}".format(power=lawyer_one.power))
print("Lawyer 2: {power}".format(power=lawyer_two.power))


tyre = 0
while tyre%2 == 0:  
  while lawyer_one.power > 0 and lawyer_two.power > 0:
    # print(tyre)
    input36 = int(input("Type 1 for Grow or 2 to Suit for Lawyer 1: "))
    if input36 == 1: 
      print("{name}, you chose to grow!".format(name=lawyer_one.name))
      lawyer_one.grow()
      print("Lawyer 1: {power}".format(power=lawyer_one.power))
      print("Lawyer 2: {power}".format(power=lawyer_two.power))
    else:
      print("You chose to suit!")
      lawyer_one.suit(lawyer_two)  
      print("Lawyer 1: {power}".format(power=lawyer_one.power))
      print("Lawyer 2: {power}".format(power=lawyer_two.power))
    tyre += 1
    # print(tyre)
    break
  if lawyer_one.power <= 0 or lawyer_two.power <= 0:
    break
  # break  
  while tyre%2 == 1: 
    while lawyer_one.power > 0 and lawyer_two.power > 0:
      input48 = int(input("Type 1 for Grow or 2 to Suit for Lawyer 2: "))
      if input48 == 1: 
        print("{name}, you chose to grow!".format(name=lawyer_two.name))
        lawyer_two.grow()
      elif input48 == 2:
        print("You chose to suit!")
        lawyer_two.suit(lawyer_one)
      print("Lawyer 1: {power}".format(power=lawyer_one.power))
      print("Lawyer 2: {power}".format(power=lawyer_two.power))
      tyre -= 1  
      # print(tyre)
      break
  if lawyer_one.power <= 0 or lawyer_two.power <= 0:
      break
    # break


if lawyer_one.power <= 0 and lawyer_two.power >= lawyer_one.power:
  if lawyer_one.power < lawyer_two.power and lawyer_two.power > 0:
    print("lawyer 2 wins")
  else: 
    print("Draw Game Over")
else:
  print("lawyer 1 wins")

  
# helip = True
# input4 = int(input("Type g for Grow or s to Suit for P1: ")
# while helip == True:
#   if input4 == g:
#     print("I'm a dum")
#   elif input4 == s:
#     print("I suck")
#   else:
#     pass

# while heli:
#   inputg1 = input("\nPlayer 1 Choose your actions (Grow or Suit):"
#   if inputg1 == 'grow':
#     pass
#     print(int(lawyer_one.power))
#     lawyer_one.grow(inp1)
#   else:
#     pass

  #   h1 = False
  # elif inputg1 == "suit":
  #   lawyer_two.suit(lawyer_one)
  #   h1 = False
  # else:
  #   h1 = True

# print("Lawyer 1: {power}".format(power=lawyer_one.power))
# print("Lawyer 2: {power}".format(power=lawyer_two.power))
