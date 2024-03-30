from scripts.fromLTI.platforms.CanvasInstructureQuestion import CanvasInstructureQuestion
from scripts.fromLTI.platforms.MoodleXMLQuestion import MoodleXMLQuestion
from scripts.fromLTI.platforms.StepikStepQuestion import StepikStepQuestion
from scripts.toLTI import MultipleChoiceQuestion
from scripts.toLTI.Question import Question

from scripts.toLTI.conversion_formats import ConversionFormat


class PlatformsMultipleChoice:
    """
    Multiplatform manager. This manager is controlling all the managers that convert LTI format to another platform's format
    """

    def parse_questions(self, parsed_question: Question | list, type_of_question) -> str:
        """Returns a string-representation of parsed question (LTI) in format of any platform (in dependent of type_of_question param) """
        if type_of_question == int(ConversionFormat.MultipleChoiceMoodleXML):
            moodle_xml_formatter = MoodleXMLQuestion()
            if isinstance(parsed_question, Question):
                return moodle_xml_formatter.parse_one_question(parsed_question,
                                                               ConversionFormat.MultipleChoiceMoodleXML)
            elif isinstance(parsed_question, list):
                return moodle_xml_formatter.parse_questions(parsed_question, ConversionFormat.MultipleChoiceMoodleXML)
            else:
                raise Exception("You submit incorrect file. Error in PlatformsMultipleChoice.parse_questions")
        elif type_of_question == int(ConversionFormat.MultipleChoiceStepikStep):
            stepik_formatter = StepikStepQuestion()
            if isinstance(parsed_question, Question):
                return stepik_formatter.parse_one_question(parsed_question, ConversionFormat.MultipleChoiceStepikStep)
            elif isinstance(parsed_question, list):
                raise Exception('Now is available only 1 question. In development')  # TODO
            else:
                raise Exception("You submit incorrect file. Error in PlatformsMultipleChoice.parse_questions")
        elif type_of_question == int(ConversionFormat.CanvasInstructure):
            canvas_formatter = CanvasInstructureQuestion()
            if isinstance(parsed_question, Question):
                return canvas_formatter.parse_one_question(parsed_question, ConversionFormat.CanvasInstructure)
            elif isinstance(parsed_question, list):
                return canvas_formatter.parse_questions(parsed_question, ConversionFormat.CanvasInstructure)
            else:
                raise Exception('You submit incorrect file. Error in PlatformsMultipleChoice.parse_questions')
