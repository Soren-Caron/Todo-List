import os
from datetime import datetime

tasksName = []
tasksDate = []
tasksDeadline = []

#Reads file to make sure it has correct structure and store information about the tasks in arrays
def readFile():
  with open("tasks.txt") as read_file:
    contents = read_file.read()

    #The part of the code that makes sure the file has correct structure
    if contents == '':
      pass
      with open("tasks.txt", 'w') as write_file:
        write_file.write("Task" + " "*15 + "Date" + " "*15 + "Due Date" + " "*15 +'\n')
    
    contents = contents.splitlines()
    #The part of the code that stores everything already written an array file
    index = 0
    for line in contents:
      if index == 0:
        index+=1
        continue
      else:
        tempArray = line.split()
        tasksName.append(tempArray[0])
        tasksDate.append(tempArray[2])
        tasksDeadline.append(tempArray[1])

def updateTask():
  with open("tasks.txt", 'w') as write_file:
    write_file.write("Task" + " "*15 + "Date" + " "*15 + "Due Date" + " "*15 +'\n')
  with open("tasks.txt", 'a') as append_file:
    for index in range(len(tasksName)):
      append_file.write("%-18s %-18s %s\n" % (tasksName[index], tasksDate[index], tasksDeadline[index]))


#Asks user for information then prints them into the tasks.txt file. It also stores new ddata into array
def addTask():
  task = input("\nWhat Task is it?")
  tasksName.append(task)

  #variables to measure current date
  currentYear = datetime.now().year
  currentMonth = datetime.now().month
  currentDay = datetime.now().day
  currentDate = str(currentYear)+'-'+str(currentMonth)+'-'+str(currentDay)
  tasksDate.append(currentDate)

  daysDue = int(input("\nIn how many days is it due?"))
  differenceInDaysDue = currentDay - daysDue
  daysDue = str(currentYear)+'-'+str(currentMonth)+'-'+str(differenceInDaysDue)
  dueDate = datetime.now()
  tasksDeadline.append(dueDate)

  with open("tasks.txt", 'a') as write_file:
        write_file.write("%-18s %-18s %s\n" % (task, currentDate, daysDue))

#Gives the reader a list of tasks, then asks them either to 1)go back 2)read more about a specific task
def readTask():
  index = 1
  for name in tasksName:
    print(f"{index} - {name}")
    index+=1
  choice = int(input("Which task number would you like to know more about"))

  #informs the user about the information they selected
  print(f"\nThe task is {tasksName[choice-1]}, it was uploaded on {tasksDate[choice-1]}, and it is due on {tasksDeadline[choice-1]}\n")

def removeTask():
  index = 1
  for name in tasksName:
    print(f"{index} - {name}")
    index+=1
  choice = int(input("Which task number would you like to delete"))

  #removes the task from the list
  tasksName.pop(choice-1)
  tasksDate.pop(choice-1)
  tasksDeadline.pop(choice-1)
  
  updateTask()

#Will act as an indefenite loop until user quits. Until then this function will operatre the entire program
def todo_app():
  while True:
    readFile()

    #Asks user for option input. if input is invalid, the system politely asks the user to try again
    while True:
      try:
        option = int(input("What would you like for today: \n  (1)Quit\n  (2)Add a task\n  (3)Read your tasks\n  (4)Remove a task\n"))
        break
      except:
        print("Not a valid input. Please try again:")

    #Allocate the different choices to different codes of result (functions)
    if option == 1:
      break
    elif option == 2:
      addTask()
    elif option == 3:
      readTask()
    elif option == 4:
      removeTask()
    else:
      print("Not a valid input. Please try again:")

#runs todo_app for
if __name__ == "__main__":
  todo_app()

