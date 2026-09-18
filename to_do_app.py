print("====== TO-DO APP =======")
class task_list:
     def __init__(self , personal, professional ):
          self.personal= personal 
          self.professional= professional

     def display_tasks(self):
          print("Personal:", self.personal)
          print("Professional:", self.professional)
task1= task_list(" Wake up at 5 ", "Writing Reports ")
task2=task_list(" Agility " , " Production & scale")
task3=task_list(" Public Portfolios ", "Governance")
task4=task_list(" GYM ", "Business impact")
task5=task_list(" Meditation ", "focus on Production-grade applications for businesses")


task1.display_tasks()
task2.display_tasks()
task3.display_tasks()
task4.display_tasks()
task5.display_tasks()



"""
list_of_task=[" 1. Wake up at 5 \n  2. study for 8 hours \n 3. Make python projects \n 4. Revise all previous topics \n 5. DSA \n 6. Gym \n "]

while True:
     
     user_input=input("1. Add task  \n 2. View task \n 3. Complete task \n 4. Delete task \n 5. Exit \n ")
     if user_input=="1":
          task=input("Enter your task :-")
          list_of_task.append(task)
          print(list_of_task)
     elif user_input=="2":
          print(list_of_task)

     elif user_input=="3":
          completed_task=input("Enter the task you have completed:- ").strip().lower()
          print(f"{completed_task} is completed! Wohh! Almost there!")

     elif user_input=="4":
          delete_task= input("Enter the task you want to delete:-")
          list_of_task.remove(delete_task)
          print(f"{delete_task} task is deleted")

     elif user_input=="5":
          end_program= input("Do you really want to delete this task?(yes/no)")
          if end_program=="yes":
               print("Program Ended!")
               exit()
          else:
               continue

"""
          
