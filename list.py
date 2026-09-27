import dataManeger

dataManeger.clear_terminal()

while True:
 print("/-------/stop to stop--------/")
 print("/-------/clear to reset-------/")
 print("/--------My Tasks--------/")
 for lista in dataManeger.addSave:
    print(f"{lista['num']}. {lista['list']}")

 toDo = input("What you have to do?: ")
 if toDo == "/stop":
   break
 
 elif toDo == "/clear":
   
   dataManeger.addSave.clear()
   dataManeger.clear_terminal()
   dataManeger.saveData(dataManeger.addSave)
   continue

 dataManeger.addSave.append({"list": toDo,
                             "num": len(dataManeger.addSave)+1})
 
 dataManeger.saveData(dataManeger.addSave)
 dataManeger.clear_terminal()