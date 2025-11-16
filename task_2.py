class Tester():

    def __init__(self, name, deadline):
        self.tester_name = name
        self.tester_deadline = deadline

    def work_hard(self):
        
        if self.tester_deadline == True:
            print(self.tester_name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.tester_name, 'Можно отдыхать')

tester_1 = Tester('tester_1', False)
tester_1.work_hard()  # 'tester_1 Можно отдыхать'
tester_2 = Tester('tester_2', True)
tester_2.work_hard()   # 'tester_2 Что ж, ещё часок поработаю!'