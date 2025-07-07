import html

class QuizBrain:
    
    def __init__(self, questionBank):
        self.question_number = 0
        self.question_list = questionBank
        self.score = 0
        
    def still_has_question(self):
        if (self.question_number) < len(self.question_list):
            return True
        else:
            return False
        
    def next_question(self):
        currentNumber = self.question_number
        user_answer = input(html.unescape("Q.{nomersoal}: {soal} (True/False)? ".format(nomersoal = currentNumber + 1, soal = self.question_list[self.question_number].text)))
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number= self.question_number + 1
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.title() == correct_answer:
            print("You got it right")
            self.score = self.score + 1
            
        else:
            print("That's wrong")
            
        print("The correct answer was {ans}".format(ans = correct_answer))
        
        print("Your current score is: {score}/{currentQuestion}.".format(score = self.score, currentQuestion = self.question_number + 1))
        print("\n" * 2)
        
            