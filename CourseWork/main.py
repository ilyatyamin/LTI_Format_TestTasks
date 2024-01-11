import json
from CourseWork.MultiplyChoice.QuestionEncoder import QuestionEncoder

from CourseWork.MultiplyChoice.MultipleChoiceQuestion import MultiplyChoiceQuestion

quest1 = MultiplyChoiceQuestion()
quest1.parseOneQuestionFromMoodleXML("/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/MultipleChoice_Moodle.xml")


quest1.saveToFormat("new_file.json")

