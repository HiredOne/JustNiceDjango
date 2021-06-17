##############
# Question 1 #
##############

# Your answer here.
# Q1
def pyramids(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n* pyramids(n-1) * pyramids(n-2)


# Tests
def test_q1():
    print(pyramids(1)==1)
    print(pyramids(2)==2)
    print(pyramids(3)==6)
    print(pyramids(4)==30)

# Uncomment to test question 1
test_q1()


##############
# Question 2 #
##############
import csv

def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of lists
    containing rows in the csv file and its entries.
    """
    with open(csvfilename, encoding='utf-8') as csvfile:
        rows = [row for row in csv.reader(csvfile)]
    return rows

# Your answer here.
# Q2

def top_k_timestamps(filename, date, k):
    rows = read_csv(filename)[1:]
    filtered = filter(lambda x: x[0] == date, rows)
    dic = {}
    kth = []
    for _, timestamp, players, viewers in filtered:
        players, viewers = int(players), int(viewers)
        ttl = players + viewers
        if timestamp not in dic:
            dic[timestamp] = ttl
    values = sorted(list(dic.values()), reverse = True)
    for value in values: #Sort the dic
        for timestamp, ttl in dic.items():
            if ttl == value:
                kth.append((timestamp, ttl))
    return kth[:k]



def player_daily_stats(filename, start_date, end_date):
    rows = read_csv(filename)[1:]
    filtered = filter(lambda x: (x[0] >= start_date and x[0] <= end_date), rows)
    dic = {}
    res = {}
    for date, timestamp, players, _ in filtered:
        players = int(players)
        hr = timestamp[:2]
        if date not in dic:
            dic[date] = {}
        if hr not in dic[date]:
            dic[date][hr] = [0, 0] #Count, players
        dic[date][hr][0] += 1 #Counting no. tstamps
        dic[date][hr][1] += players #Summing the players
        #print('Date, hr', dic[date][hr])
    #Get hrly averages
    for date in dic.keys():
        for hr in dic[date]:
            count = dic[date][hr][0]
            players = dic[date][hr][1]
            dic[date][hr] = round(players/count, 2)
    for date in dic.keys(): #initialise res and do for all dates
        if date not in res:
            res[date] = {}
        if 'max' not in res[date]:
            res[date]['max'] = ()
        if 'min' not in res[date]:
            res[date]['min'] = ()
        #Get max and min
        for hr, count in dic[date].items():
            if count == max(dic[date].values()):
                res[date]['max'] = (hr, count)
            if count == min(dic[date].values()):
                res[date]['min'] = (hr, count)
    return res


# Tests
def test_q2a():
    test1 = top_k_timestamps("among_us.csv", "2020-10-24", 1)
    print(test1)
    print(test1 == [('23:50', 263111)])
    test2 = top_k_timestamps("among_us.csv", "2020-10-24", 3)
    print(test2)
    print(test2 == [('23:50', 263111), ('23:40', 259451), ('23:30', 257646)])
    test3 = top_k_timestamps("among_us.csv", "2020-11-01", 5)
    print(test3)
    print(test3 == [('04:00', 440435), ('03:50', 420450), ('05:00', 418154), ('03:40', 417638), ('05:10', 414781)])

def test_q2b():
    test1 = player_daily_stats("among_us.csv", "2020-10-24","2020-10-25")
    print(test1)
    print(test1 == {
        '2020-10-24':{'max':('23', 148503.83), 'min':('22', 136173.0)},
        '2020-10-25':{'max':('05',  279875.67), 'min':('17', 83682.83)}
    })
    test2 = player_daily_stats("among_us.csv", "2020-10-26","2020-11-01")
    print(test2)
    print(test2 == {
        '2020-10-26':{'max':('04', 321269.17), 'min':('16', 68468.83)},
        '2020-10-27':{'max':('04', 281635.0),  'min':('16', 66024.17)},
        '2020-10-28':{'max':('04', 268729.33), 'min':('16', 64382.33)},
        '2020-10-29':{'max':('04', 263688.67), 'min':('16', 61390.17)},
        '2020-10-30':{'max':('04', 262891.17), 'min':('16', 59494.0)},
        '2020-10-31':{'max':('05', 313064.67), 'min':('17', 65617.5)},
        '2020-11-01':{'max':('05', 278808.17), 'min':('17', 70535.83)}
    })

# Uncomment to test question 2
test_q2a()
test_q2b()


##############
# Question 3 #
##############

# Your answer here.
# Q3
class Place:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks
        self.people = []

class Crewmate:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.tasks = {place.name: []}
        place.people.append(self)
        self.dead = False

    def move(self, place):
        self.place.people.remove(self) #Leave old place
        self.place = place
        place.people.append(self) #New place
        if place.name not in self.tasks: #First time going to place
            self.tasks[place.name] = []
        return f'{self.name} moves to {place.name}'

    def do_task(self, task):         
        place_name = self.place.name
        if task not in self.place.tasks:
            return f'No such task {task} in {self.place.name}'
        if task in self.tasks[place_name]:
            return f'Task {task} in {place_name} already done'
        else:
            self.tasks[place_name].append(task)
            return f'{self.name} does {task} in {place_name}'

class Impostor(Crewmate):
    def __init__(self, name, place):
        super().__init__(name, place)

    def do_task(self, task):
        return 'Impostors cannot do tasks'

    def kill(self):
        import random
        can_kill = False
        killable = []
        for person in self.place.people:
            if not (isinstance(person, Impostor)) and (not person.dead):
                killable.append(person)
        if killable == []:
            return 'Nobody to kill'
        else:
            number = random.randint(0,len(killable)-1)
            killed = killable[number]
            killed.dead = True #Kill person
            return f'{self.name} kills {killed.name} at {self.place.name}'


# Tests
def test_q3():
    cafe = Place("Cafeteria",  ["fix wires", "download data"])
    weapons = Place("Weapons", ["shoot asteroids", "fix wires"])

    ben = Impostor("@evilprof", cafe)
    waikay =  Impostor("@waisosus", cafe)
    kenghwee = Crewmate("@hweelingdead", cafe)
    jonathan = Crewmate("@lordjon", cafe)

    _=kenghwee.do_task("shoot asteroids"); print(_ == "No such task shoot asteroids in Cafeteria", "\tkenghwee.do_task(\"shoot asteroids\"):\t", _)
    _=jonathan.do_task("fix wires"); print(_ == "@lordjon does fix wires in Cafeteria", "\tjonathan.do_task(\"fix wires\"):\t", _)
    _=jonathan.do_task("fix wires"); print(_ == "Task fix wires in Cafeteria already done", "\tjonathan.do_task(\"fix wires\"):\t", _)
    _=jonathan.move(weapons); print(_ == "@lordjon moves to Weapons", "\tjonathan.move(weapons):\t", _)
    _=jonathan.do_task("fix wires"); print(_ == "@lordjon does fix wires in Weapons", "\tjonathan.do_task(\"fix wires\"):\t", _)
    _=waikay.move(weapons); print(_ == "@waisosus moves to Weapons", "\twaikay.move(weapons):\t", _)
    _=waikay.do_task("adjust aiming"); print(_ == "Impostors cannot do tasks", "\twaikay.do_task(\"adjust aiming\"):\t", _)
    _=kenghwee.move(weapons); print(_ == "@hweelingdead moves to Weapons", "\tkenghwee.move(weapons):\t", _)
    _=ben.kill(); print(_ == "Nobody to kill", "\tben.kill():\t", _)
    _=waikay.kill(); print(_ in ["@waisosus kills @hweelingdead at Weapons", "@waisosus kills @lordjon at Weapons"], "\twaikay.kill():\t", _)
    _=ben.move(weapons); print(_ == "@evilprof moves to Weapons", "\tben.move(weapons):\t", _)
    _=ben.kill(); print(_ in ["@evilprof kills @lordjon at Weapons", "@evilprof kills @hweelingdead at Weapons"], "\tben.kill():\t", _)
    _=ben.kill(); print(_ == "Nobody to kill", "\tben.kill():\t", _)
    _=kenghwee.move(cafe); print(_ == "@hweelingdead moves to Cafeteria", "\tkenghwee.move(cafe):\t", _)
    _=kenghwee.do_task("fix wires"); print(_ == "@hweelingdead does fix wires in Cafeteria", "\tkenghwee.do_task(\"fix wires\"):\t", _)

# Uncomment to test question 3
test_q3()
