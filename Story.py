def repeat():
  print("---------------------------------------")
  print("Try to make the story as funny as you can")
  gender= input("Type M for male and F for female character")
  #adding words for story
  noun= input("Please type a name")
  name_of_company= input("Write a name of a company")
  disease= input("Write a name of a disease")
  days= int(input("Enter number of days"))
  money_lost= 50*days
  bad_job= input("Enter name of odd/bad jobs")
  type_of_house= input("Enter type of house")
  area= input("Enter the name of area the house is located")
  print("---------------------------------------")
  #executing the story with the given words
  if gender == "M":
      print(noun,"was very poor during those times.")
  elif gender == "F":
    print(noun,"was very poor during those times.")
  else:
    print("Enter valid Gender")
  if gender== "M":
      print(noun,"worked in a company called",name_of_company,"which paid him only 50 rupees per day.")
  elif gender=="F":
    print(noun,"worked in a company called",name_of_company,"which paid her only 50 rupees per day.")
  else: print("Enter valid Gender")
  if gender== "M":
    print("One day he got infected with",disease,"and got admitted in a Government hospital.")
  elif gender == "F":
    print("One day she got infected with",disease,"and got admitted in a Government hospital.")
  else: print("Enter valid Gender")
  if gender== "M":
   print(noun,"was in the hospital for", days, "days and lost",money_lost,"rupees as he did not work for",days,"days.")
  elif gender=="F":
    print(noun,"was in the hospital for", days, "days and lost",money_lost,"rupees as she did not work for",days,"days.")
  else: print("Enter valid Gender")
  if gender== "M":
   print("After",noun,"'s discharge from the hospital he left the job at",name_of_company,"and started using odd ways like",bad_job,"to earn money.")
  elif gender == "F":
    print("After",noun,"s discharge from the hospital she left the job at",name_of_company,"and started using odd ways like",bad_job,"to earn money.")
  else: print("Enter valid Gender")
  if gender== "M":
   print("He somehow earned 25000 rupees and invested it in the Stock Market.")
  elif gender == "F":
       print("She somehow earned 25000 rupees and invested it in the Stock Market."+"And now lives in a",type_of_house,"in",area,".")
  else: print("Enter Valid Gender")

  #Score
  import random
  if gender== "M":
     print("Your funny score is =", random.randint(75,100))
  elif gender=="F":
    print("Your funny score is =", random.randint(75,100))
  else:
    print("Enter Valid Gender")

  #if you want to play again or stop
  play_again = input("Type yes if you want to play more or no if you don't want to")
  if play_again== "yes" :
    repeat()
  elif play_again== "no" :
    print("Ok! Thank you for playing this game!!!")
  else:
    print("I didn't get it.....")
repeat()