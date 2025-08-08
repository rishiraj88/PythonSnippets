import sys
import pickle

tasks_datafile_name="todo_datafile.txt"
tasks=[]

#read tasks from file
try:
    tasks_datafile = open(tasks_datafile_name,"rb")
    tasks= pickle.load(tasks_datafile)
    tasks_datafile.close()
except:
    pass
print(tasks)

#create tasks
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    tasks.append(f"{' '.join(sys.argv[2:])}\n")

#remove tasks from file
if len(sys.argv) >= 3 and sys.argv[1].lower() == "del":
    try:
        del_idx = int(sys.argv[2])
        if del_idx > 0:
            del_idx -= 1
            del(tasks[del_idx])
        else:
            print("wrong selection!")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

print(tasks)

#save tasks to the file
tasks_datafile = open(tasks_datafile_name,"wb")
pickle.dump(tasks,tasks_datafile)
tasks_datafile.close()

#print tasks
if len(tasks) == 0:
    print("No tasks to perform. Enjoy!")
else:
    print("\nHere are your next milestones:\n")
    for x in range(len(tasks)):
        print(f"{x+1}: {tasks[x]}",end="")

        
# Print Commands
print("\n*******************************\n")
print(f"To view task list:\n{sys.argv[0]}")
print(f"\nTo add a task:\n{sys.argv[0]} add Morning walk\n")
print(f"To remove or complete a task:\n{sys.argv[0]} del 2\n")
