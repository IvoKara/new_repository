def add_task(tasks, id, title, deadline, priority, tags):
    tasks.append({
        'id': id,
        'title': title,
        'deadline': deadline,
        'priority': priority,
        'tags': tags,
        'completed': False
        })


def find_task(tasks, id):
    count=0
    while count<len(tasks):
        if tasks[count]['id']==id:
            return count
            break
        count+=1

def remove_task(tasks, id):
    sth = find_task(tasks, id)
    tasks.pop(sth)
    
def complete_task(tasks,id):
    sth = find_task(tasks, id)
    tasks[sth]['completed']=True

def uncomplete_task(tasks,id):
    sth = find_task(tasks, id)
    tasks[sth]['completed']=False

def get_completed(tasks):
    completed=[]
    i=1
    while i<=len(tasks):
        sth = find_task(tasks, str(i))
        if tasks[sth]['completed']==True:
            completed.append(tasks[sth])
        i+=1
    return completed

def get_uncompleted(tasks):
    uncompleted=[]
    i=1
    while i<=len(tasks):
        sth = find_task(tasks, str(i))
        if tasks[sth]['completed']==False:
            uncompleted.append(tasks[sth])
        i+=1
    return uncompleted

def clear_completed(tasks):
    lol = get_completed(tasks)
    tasks.pop(lol)

print("My file is called {}".format(__file__))
