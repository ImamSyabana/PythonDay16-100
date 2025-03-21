class QuizBrain:
    def __init__(self, questionBank):
        self.question_number = 0
        self.question_list = questionBank
        
    def next_question(self):
        currentQuestion = self.question_number
        self.question_number = self.question_number + 1
        input("Q.{nomersoal}: {soal} (True/False)?".format(nomersoal = currentQuestion, soal = self.question_list[currentQuestion].text))