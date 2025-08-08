import pickle

class ToDo:
    def __init__(self,title, important, category="Normal"):
        self.title=title
        self.important=important
        self.category=category

todos = [ToDo("Buy food",True)
         ,ToDo("Evening walk",False)
         ,ToDo("Cook dinner",True)
         ,ToDo("Watch movies",True,category="Low")]

todos_file = open("todos_datafile.txt","wb")
pickle.dump(todos,todos_file)
todos_file.close()

todos_file = open("todos_datafile.txt","rb")
saved_todos = pickle.load(todos_file)
todos_file.close()
print(saved_todos)