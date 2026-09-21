Name= "ANANTA PANDEY"
print("====== TO-DO APP =======")
print(f"Welcome {Name} here are your tasks for today")
while True:
   menu=(input(" 1. Show all the tasks \n  2. Marked completed tasks \n 3. exit \n " ))
   
   if menu=="1": 
         class task_list:
          def __init__(self , personal, professional ):
            self.personal= personal 
            self.professional= professional

          def display_tasks(self):
            print("Personal:", self.personal)
            print("Professional:", self.professional)
         task1= task_list(" Wake up at 5 ", "Writing Reports ")
         task1.display_tasks()
         task2=task_list(" Agility " , " Production & scale")
         task2.display_tasks()
         task3=task_list(" Public Portfolios ", "Governance")
         task3.display_tasks()
         task4=task_list(" GYM ", "Business impact")
         task4.display_tasks()
         task5=task_list(" Meditation ", "focus on Production-grade applications for businesses")
         task5.display_tasks()

         user_input=input("do you want to save this file?(yes/no) \n").strip().lower()
         if user_input=="yes":
  
          with open ("tasks.txt" , "w") as f:
           f.write("\n ===== TO-DO APP ====== \n ")
           f.write(f"persoanl - {task1.personal}" + "\n")
           f.write(f"professional - {task1.professional}" + "\n")
           f.write("-"*30 + "\n")
           f.write(f"personal - {task2.personal}" + "\n")
           f.write(f"professional - {task2.professional}" + "\n")
           f.write("-"*30 + "\n")
           f.write(f"personal - {task3.personal}" + "\n" )
           f.write(f"perfessional - {task3.professional}" + "\n")
           f.write("-"*30 + "\n")
           f.write(f"personal - {task4.personal}" + "\n")
           f.write(f"professional - {task4.professional}" + "\n ")
     
          print("file saved successfully!")
         else:
           exit()
           break
   elif menu=="2":
     user_input=input("Enter the tasks you have complete:- ").strip().lower()
     print(f"woohoo! {user_input} completed")
     break
   elif menu=="3":
     user_input=input("Do you want to exit this app? (yes/no)")
     if user_input=="yes":
       print("Program Ended!")
       exit()
     else:
       continue