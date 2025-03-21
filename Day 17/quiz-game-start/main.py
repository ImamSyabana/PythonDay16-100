import question_model
import data
import quiz_brain

questionList = []

# ngebikin objek yang isinya property soal sama jawaban yang diambil dari dictionary
for x in range (len(data.question_data)):
    tempObjek = question_model.Question(data.question_data[x]["text"], data.question_data[x]["answer"])
    questionList.append(tempObjek)
    

quizObjek = quiz_brain.QuizBrain(questionList)
quizObjek.next_question()


print(questionList[0].text)
print(questionList[0].answer)