from scripts.fromLTI.platforms.CanvasInstructureQuestion import CanvasInstructureQuestion
from scripts.fromLTI.platforms.MoodleXMLQuestion import MoodleXMLQuestion
from scripts.fromLTI.platforms.StepikStepQuestion import StepikStepQuestion
from scripts.toLTI import MultipleChoiceQuestion

from scripts.toLTI.conversion_formats import ConversionFormat


class PlatformsMultipleChoice:
    """
    Multiplatform manager. This manager is controlling all the managers that convert LTI format to another platform's format
    """
    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question) -> str:
        """Returns a string-representation of parsed question (LTI) in format of any platform (in dependent of type_of_question param) """
        if type_of_question == int(ConversionFormat.MultipleChoiceMoodleXML):
            moodle_xml_formatter = MoodleXMLQuestion()
            return moodle_xml_formatter.parse_one_question(parsed_question, ConversionFormat.MultipleChoiceMoodleXML)
        elif type_of_question == int(ConversionFormat.MultipleChoiceStepikStep):
            stepik_formatter = StepikStepQuestion()
            return stepik_formatter.parse_one_question(parsed_question, ConversionFormat.MultipleChoiceStepikStep)
        elif type_of_question == int(ConversionFormat.CanvasInstructure):
            canvas_formatter = CanvasInstructureQuestion()
            return canvas_formatter.parse_one_question(parsed_question, ConversionFormat.CanvasInstructure)