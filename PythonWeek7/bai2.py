
class Job:
    def __init__(self, idJob, nameJob, majorJob, salaryJob):
        self.idJob = idJob
        self.nameJob = nameJob
        self.majorJob = majorJob
        self.salaryJob = salaryJob

    def evaluate(self, skills):
        average = sum(skills.values()) / len(skills)
        if average > 9.0:
            return "Rất phù hợp"
        elif average > 7.0:
            return "Phù hợp"
        elif average > 5.0:
            return "Tạm được"
        elif average > 3.0:
            list_skill = []
            for key, value in skills.items():
                if(value < 4.0):
                    list_skill.append(key)
            return f"Cần bổ sung kiến thức: {', '.join(list_skill)}"
        else:
            return "Cần học lại kiến thức base"

    def __str__(self):
        return f"ID: {self.idJob} || Tên: {self.nameJob} || Ngành: {self.majorJob} || Lương: {self.salaryJob}"

class AI(Job):
    def __init__(self, idJob, nameJob, majorJob, salaryJob, pythonSkill, mlSkill, deepSkill, mathSkill):
        super().__init__(idJob, nameJob, majorJob, salaryJob)
        self.pythonSkill = pythonSkill
        self.mlSkill = mlSkill
        self.deepSkill = deepSkill
        self.mathSkill = mathSkill

    def evaluate(self):
        skill = {"Python": self.pythonSkill, "ML": self.mlSkill, "Deep": self.deepSkill, "Math": self.mathSkill}
        result = super().evaluate(skill)
        print(result)


class Backend(Job):
    def __init__(self, idJob, nameJob, majorJob, salaryJob, sqlSkill, oopSkill, apiSkill, javaSkill):
        super().__init__(idJob, nameJob, majorJob, salaryJob)
        self.sqlSkill = sqlSkill
        self.oopSkill = oopSkill
        self.apiSkill = apiSkill
        self.javaSkill = javaSkill

    def evaluate(self):
        skill = {"SQL": self.sqlSkill, "OOP": self.oopSkill, "API": self.apiSkill, "Java": self.javaSkill}
        result = super().evaluate(skill)
        print(result)
    

class Frontend(Job):
    def __init__(self, idJob, nameJob, majorJob, salaryJob, htmlSkill, cssSkill, nodeJSSkill, UX, UI):
        super().__init__(idJob, nameJob, majorJob, salaryJob)
        self.htmlSkill = htmlSkill
        self.cssSkill = cssSkill
        self.nodeJSSkill = nodeJSSkill
        self.UX = UX
        self.UI = UI

    def evaluate(self):
        skill = {"HTML": self.htmlSkill, "CSS": self.cssSkill, "NodeJS": self.nodeJSSkill, "UX": self.UX, "UI": self.UI}
        result = super().evaluate(skill)
        print(result)
    def __str__(self):
        return f"Frontend: {self.idJob} - {self.nameJob} - {self.majorJob} - {self.salaryJob} - {self.htmlSkill} - {self.cssSkill} - {self.nodeJSSkill} - {self.UX} - {self.UI}"

class Fullstack(Frontend, Backend):
    def __init__(self, idJob, nameJob, majorJob, salaryJob, sqlSkill, oopSkill, apiSkill, javaSkill, htmlSkill, cssSkill,
                 nodeJSSkill, UX, UI):
        Backend.__init__(self, idJob, nameJob, majorJob, salaryJob, sqlSkill, oopSkill, apiSkill, javaSkill)
        Frontend.__init__(self, idJob, nameJob, majorJob, salaryJob, htmlSkill, cssSkill, nodeJSSkill, UX, UI)
        
    def evaluate(self):
        skill = {
            "SQL": self.sqlSkill, "OOP": self.oopSkill, "API": self.apiSkill, "Java": self.javaSkill,
            "HTML": self.htmlSkill, "CSS": self.cssSkill, "NodeJS": self.nodeJSSkill, "UX": self.UX, "UI": self.UI
        }
        result = super().evaluate(skill)
        print(result)

ai_job = AI(1, "AI", "Machine Learning", 1000000, 9.5, 9.2, 9.0, 8.8)
backend_job = Backend(2, "Backend", "Python", 200000, 8.0,3.0,4.0,5.0)
frontend_job = Frontend(3, "Frontend", "JavaScript", 3000000, 3.0, 4.0, 9.0, 8.0, 4.0)
fullstack_job = Fullstack(4, "Fullstack", "JavaScript", 4000000,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,9.8)


print("Thong tin AI job")
print(ai_job.__str__())
print("Danh gia AI job")
ai_job.evaluate()

print("Thong tin Backend job")
print(backend_job.__str__())
print("Danh gia Backend job")
backend_job.evaluate()

print("Thong tin Frontend job")
print(frontend_job.__str__())
print("Danh gia Frontend job")
frontend_job.evaluate()

print("Thong tin Fullstack")
print(fullstack_job.__str__())
print("Danh gia Fullstack")
fullstack_job.evaluate()



