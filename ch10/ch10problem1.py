#create a class "programmer" for storing information for new programmers working at microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Dipika", 1200000, 711302)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Atrika", 1200000, 711302)
print(r.name, r.salary, r.pin, r.company)