import json
from CourseWork.MultiplyChoice.QuestionEncoder import QuestionEncoder

from CourseWork.MultiplyChoice.MultipleChoiceQuestion import MultiplyChoiceQuestion

paths = ["../examples of files/MultipleChoice_Moodle.xml",
         "../examples of files/MoodleCSV_example3.csv",
         "../examples of files/moodle_word2010_v2.docx"]
question1 = MultiplyChoiceQuestion()
question1.parseOneQuestionFromMoodleXML(paths[0])
question1.saveToFormat("fromMoodleXml.json")

question2 = MultiplyChoiceQuestion()
question2.parseOneQuestionMoodleCSV(paths[1])
question2.saveToFormat("fromMoodleCSV.json")

question2 = MultiplyChoiceQuestion()
question2.parseOneQuestionMoodleDocx(paths[2])
question2.saveToFormat("fromMoodleWordFirst.json")
