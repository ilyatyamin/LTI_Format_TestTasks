from FormatsHandler import FormatsHandler
from scripts.fromLTI.platforms.StepikStepQuestion import StepikStepQuestion
from scripts.toLTI.conversion_formats import ConversionFormat

handler = FormatsHandler()
question = handler.process_question(
    '/Users/mrshrimp.it/Documents/ВШЭ учеба/2 курс/LTI_Format_TestTasks/examples of files/stepik_multiplychoices.step',
    int(ConversionFormat.MultipleChoiceStepikStep))

formatter_back = StepikStepQuestion()
print(formatter_back.parse_one_question(question))
