class enter:
    def __init__(self,question,option1,option2,option3,option4,answer):
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 =option4
        self.answer = answer

    def json(self):
        return {
            "queston":self.question,
            "option1":self.option1,
            "option2":self.option2,
            "option3":self.option3,
            "option4":self.option4,
            "answer":self.answer
        }

