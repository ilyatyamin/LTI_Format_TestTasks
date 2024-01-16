from CourseWork.SystemManager import *

manager = MultipleChoiceManager()

# Moodle XML [bank]
manager.write_to_file("moodle_xml_bank.json", manager.load_bank_question('/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/moodle_xml.xml', SystemManager.MultipleChoiceEnum.MoodleXml))

# Moodle XML [one]
manager.write_to_file('moodle_xml_one.json', manager.load_one_question('/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/MultipleChoice_Moodle.xml', SystemManager.MultipleChoiceEnum.MoodleXml))

# Moodle Word [bank]
manager.write_to_file('moodle_word_bank.json', manager.load_bank_question('/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/moodle_word2010_v2.docx', SystemManager.MultipleChoiceEnum.MoodleWord))

# Moodle Word [one]
manager.write_to_file('moodle_word_one.json', manager.load_one_question('/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/moodle_word2010_v2.docx', SystemManager.MultipleChoiceEnum.MoodleWord))

# Moodle CSV [bank]
manager.write_to_file('moodle_csv_bank.json', manager.load_bank_question('/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/MoodleCSV_example3.csv', SystemManager.MultipleChoiceEnum.MoodleCSV))

# Stepik [one]
manager.write_to_file('stepik_bank.json', manager.load_one_question('/Users/mrshrimp.it/Downloads/1107748_2_choice-7.step', SystemManager.MultipleChoiceEnum.StepikStep))

# TestMoz Word [one], банк еще делаю
manager.write_to_file('testmoz_word.json', manager.load_one_question('/Users/mrshrimp.it/Desktop/testmoz_doc.docx', SystemManager.MultipleChoiceEnum.TestMozWord))
