# To-Do List Manager

## Description  
This Python program is a simple to-do list manager that allows users to add, view, and remove tasks. Task information, including the name, date added, and due date, is stored in a text file (`tasks.txt`) for persistence.

## Features  
- Add tasks with an automatic timestamp and customizable due date.  
- View all tasks or detailed information about a specific task.  
- Remove tasks by selecting them from a list.  
- Automatically ensures the task file is formatted correctly.  

## Requirements  
- Python 3.x  
- A `tasks.txt` file in the program directory (auto-created if not present).

## How to Use  
1. Run the program:  
   ```bash
   python todo_app.py
   ```  
2. Follow the menu prompts to:  
   - Quit (`1`)  
   - Add a task (`2`)  
   - View tasks (`3`)  
   - Remove a task (`4`)  

3. Task data is stored and updated in `tasks.txt`.  

## File Structure  
The `tasks.txt` file stores tasks in the following format:  
```
Task               Date               Due Date
TaskName           YYYY-MM-DD         YYYY-MM-DD
```

## Notes  
- Tasks are stored in three arrays (`tasksName`, `tasksDate`, and `tasksDeadline`) during execution.  
- The due date is calculated based on the number of days specified by the user.  
- The application will continue running until you select the Quit option.

--- 

Let me know if you'd like to customize it further!
