class Hall:
    def __init__(self, seats=[[]]): #места - таблица с int-ами, где пустое место - ноль
        self.seats = seats


class Theater:
    def __init__(self):
        self.halls = []
        self.sessions = []

    def addHall(self, hall):
        self.halls.append(hall)

    def addSession(self, name, time, length):  #время и длительность в формате ЧЧ:ММ
        tim = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        leng = int(length.split(":")[0]) * 60 + int(length.split(":")[1])
        self.sessions.append([name, tim, leng])