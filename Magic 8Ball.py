import random
import time

#Defined for loop
answerAgain = ("y")

print ("")
print ("Hello! Welcome to The Magic-8 Ball... ")
print ("The answers to you future awaits.")
print ("")
time.sleep (3)

#Loop as long as answerAgain = y
while answerAgain == ("y") :
  
  
  #Receive the question
  def question () :
    return (input ("Ask me a yes or no question : "))

  #Answers
  def getAnswer (answerNumber) :
    if answerNumber == 1:
      time.sleep (1.5)
      return ("Doesn't look good.")
    elif answerNumber == 2:
      time.sleep(1.5)
      return ("Yes")
    elif answerNumber == 3:
      time.sleep(1.5)
      return ("Outlook is not so good.")
    elif answerNumber == 4:
      time.sleep(1.5)
      return ("Answer is uncertain. Roll again.")
    elif answerNumber == 5:
      time.sleep(1.5)
      return ("No")
    elif answerNumber == 6:
      time.sleep(1.5)
      return ("Don't count on it.")

  question ()
  print ("...searching for the answer...")
  time.sleep(2)
  print (getAnswer(random.randint(1,6)))
  time.sleep(.75)

  answerAgain = input ("Would you like to ask another question? y/n : ")
  time.sleep (1)

  #Run the program again
  def playAgain (answerAgain) :
    if answerAgain == ("y") :
      print ("One moment please...")
      print ("")
      time.sleep (2)
    else:
      print ("Thanks for playing!")

  playAgain(answerAgain)