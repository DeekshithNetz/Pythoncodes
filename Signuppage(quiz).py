#python 3.7.1

print("https://mabla.com\n\t\t\tfollow@tInstagram:\vDikshith12\n\n")
print("(*If this code not runned perfectly in dcoder then copy the code and run in other online Python compiler in chrome\n👆👆👆🙌)")
print("\t-----♥️Join our world sign up now!-----------")
print("\n\t____________Register____________\n")
print("\tHey welcome\n\t\t__________________________\n\t\tenter your E-mail id\n")
print("\t\tE-mail id ")
email=input("\t\t")
print("\t\tEnter your name")
name=input("\t\t")
print("\t\tEnter password")
password=input("\t\t")
captcha=int(input(" \t\tCaptcha verification\n \t\t5+4=\t"))

def login():
  print(" \t\t Login\n")
  print("\t\tenter name or id to login")
  idy=input("\t\t")
  print("\t\tenter password") 
  code=input("\t\t")
  if name==idy and password==code:
    dashboard()
  else:
    print("\t!!!!!!!!Oops!wrong login!!!!!!!!!!!!!\n")
    login()

#dashboard
def dashboard():  
   print("______________Dashboard______________")
   print("Press 1 to check your profile")
   print("Press 2 to play quiz\n")
   print("insert your choice\t")
   d=int(input())
   if d==1:
    openprf()
   else:
     if d==2:
       openqz()
   
#define profile
def openprf(): 
    print("________________\nheyyy\n\t\t"+name)
    print("________________\nE-mail id is   \t"+email)
    print("________________\npassword  is   \t"+password)
    print("\nClick X to return to dashboard")
    click=input()
    if click=='x' or click=='X':
      dashboard()
    else:
      openprf()
    
    

#define quiz
def openqz():
    print("------Welcome to Kaun Banega Mabla------\n")
    question()
#defined questions
def question():
    print("1.who is the developer of this game\na)Dikshith     b)mabla     c)Elon musk")    
    answer=str(input("your choice:\t"))
    if answer=='a':
      print("\nWow! 🏆correct answer")
      question1()   
    else:
       print ("\nwrong choice")
       question1()  
#define question1
def question1():
  print("\n2.In which country Delhi is located?\na)India     b) England     c)Europe")
  answer2=input("your choice:\t")
  if answer2=='a':
    print("\n🤩mind blowing")    
    question2()
  else:
    print("\nWrong choice")  
    question2()  
#define question 2
def question2():
  print("\n3.Which is my Instagram id\na)Dikshith12     b) dikshith12     c) dikshith one two\n")
  answer3=input("your choice:\t")
  if answer3=='a' or answer3=='b':
    print("\ncorrect answer\n\nFollow me on insta😅")
    question3()
  else:
    print("\nwrong choice")
    question3()
#define question 3
def question3():
  print("\n4.Who is the CEO of Tesla\na)Elon musk     b)jeff bezos     c) dikshith\n")
  answer4=input("your choice:\t")
  if answer4=='a':
    print("\n🏆correct answer\n")
    question4()
  else:
    print("\nwrong choice")
    question4()
#define question4
def question4():
  print("\n5.were is Burj Khalifa?\na)India     b)Dubai     c) America\n")
  answer5=input("your choice:\t")
  if answer5=='b':
    print ("\nYou are ginius⭐")
    print("Game ends here\n         Thank you for playing")
    print("Press A to play again\nPress x to return home") 
    press=input()
    if press=='A' or press=='a':
      openqz()
    else:
      if press=='X' or press=='x':
        dashboard()
  else:
    print("\nwrong choice\ndon't worry better luck next time♥️🏆\n")
    print("Game ends here\n         Thank you for playing") 
    print("Press A to play again\nPress x to return home") 
    press=input()
    if press=='A' or press=='a':
      openqz() 
    else:
      if press=='X' or press=='x':
        dashboard()    
#define login  
if captcha==9:
  print("\t\t_________________________")
  login()
else:
  print("finish")
 