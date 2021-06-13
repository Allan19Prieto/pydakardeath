import json

class Employee(object):
    def __init__(self, name, work):
        self.name = name
        self.work = work

def jsonDefault(object):
    return object.__dict__

abder = Employee('Abder', 'Programadora')
jsonAbder = json.dumps(abder, default=jsonDefault)

print(jsonAbder)


