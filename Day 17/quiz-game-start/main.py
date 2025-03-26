import question_model
import data
import quiz_brain

questionList = []

# ngebikin objek yang isinya property soal sama jawaban yang diambil dari dictionary
for x in range (len(data.question_data)):
    tempObjek = question_model.Question(data.question_data[x]["question"], data.question_data[x]["correct_answer"])
    questionList.append(tempObjek)
    
quizObjek = quiz_brain.QuizBrain(questionList)

while quizObjek.still_has_question() == True:
    
    quizObjek.next_question()
    
print("You've completed the quiz")
print("Your final score was: {score}/{outOf}".format(score = quizObjek.score, outOf = quizObjek.question_number))

print("reboisasi")
print("reboisasi")
print("reboisasi")
print("reboisasi")