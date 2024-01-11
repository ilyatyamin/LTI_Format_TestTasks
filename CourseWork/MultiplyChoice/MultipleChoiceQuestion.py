import xml.etree.ElementTree as ET

from CourseWork.MultiplyChoice.MultiplyChoiceAnswer import MultiplyChoiceAnswer
from CourseWork.MultiplyChoice.QuestionEncoder import QuestionEncoder
import json


class MultiplyChoiceQuestion:
    """
        Class that introduced answer with one or multiply choice answer
    """
    def __init__(self):
        # Obligatory fields
        self.question_id = None #
        self.question_name = None #
        self.question_text: dict = {}
        self.is_single_answer = None
        self.text_style = None
        self.options: list = []
        self.is_needed_feedback = None
        self.is_always_correct = False

        # Optional fields. Depends on the platform
        self.defaultLocale = None
        self.creation_time = None
        self.shuffle_answer = None
        self.corrected_feedback:dict = {}
        self.particular_corrected_feedback:dict = {}
        self.incorrect_feedback:dict = {}
        self.default_grade = None
        self.penalty = None
        self.hidden = None
        self.answer_numbering = None
        self.show_standard_instruction = None
        self.show_num_correct = None
        self.video_link = None
        self.subtitle_files = None
        self.is_deprecated = None
        self.has_review = None
        self.preserve_order = None
        self.output_format = None
        self.general_feedback: dict = {} #
        self.course_id = None

    def __strip_file(self, path_to_file : str):
        lines = []
        with open(path_to_file, 'r+') as file:
            for line in file:
                if not line.isspace():
                    lines.append(line)
        with open(path_to_file, 'r+') as file:
            for line in lines:
                file.write(line)
            file.truncate()
            file.close()

    def __encoder(self, dictionary : dict):
        values_to_delete = []
        for item, value in dictionary.items():
            if value is None:
                values_to_delete.append(item)
        for value in values_to_delete:
            dictionary.pop(value)
        return dictionary


    def parseOneQuestionFromMoodleXML(self, path_to_file: str):
        self.__strip_file(path_to_file)

        parsed_file = ET.parse(path_to_file).getroot()
        file_as_txt = open(path_to_file).readlines()

        if parsed_file.tag != 'question' or parsed_file.attrib['type'] != 'multichoice':
            raise Exception("Not Multiply Choice Question.")

        self.question_name = parsed_file.find("name").find("text").text

        # Parsing question id (if file contains it)
        if any("<!-- question:" in x for x in file_as_txt):
            line_with_num = None
            for line in file_as_txt:
                if "<!-- question:" in line:
                    line_with_num = line
                    break
            self.question_id = "".join([x for x in line_with_num if x.isdigit()])
        else:
            self.question_id = self.__default_id

        # Parsing question's text and question's text style
        tag_text = parsed_file.find("questiontext")
        if tag_text is not None:
            if 'format' in tag_text.attrib.keys():
                self.question_text['format'] = tag_text.attrib['format']
            else:
                self.question_text['format'] = "text"
            self.question_text['text'] = tag_text.find("text").text

        # Parsing general feedback and it's format
        tag_general_feedback = parsed_file.find("generalfeedback")
        if tag_general_feedback is not None:
            if 'format' in tag_general_feedback.attrib.keys():
                self.general_feedback['format'] = tag_general_feedback.attrib['format']
            else:
                self.general_feedback['format'] = "text"
            self.general_feedback['text'] = tag_general_feedback.find("text").text

        # Parsing default grade
        tag_default_grade = parsed_file.find("defaultgrade")
        if tag_default_grade is not None:
            self.default_grade = tag_default_grade.text

        # Parsing penalty
        tag_penalty = parsed_file.find("penalty")
        if tag_penalty is not None:
            self.penalty = tag_penalty.text

        # Parsing hidden
        tag_hidden = parsed_file.find("hidden")
        if tag_hidden is not None:
            self.hidden = tag_hidden.text

        # Parsing course id
        tag_course_id = parsed_file.find("idnumber")
        if tag_course_id is not None:
            self.course_id = tag_course_id.text

        # Parsing is_single_answer
        tag_is_single_answer = parsed_file.find("single")
        if tag_is_single_answer is not None:
            if tag_is_single_answer.text == "true":
                self.is_single_answer = 1
            else:
                self.is_single_answer = 0

        # Parsing shuffleanswers
        tag_shuffleanswers = parsed_file.find("shuffleanswers")
        if tag_shuffleanswers is not None:
            if tag_shuffleanswers.text == "true":
                self.shuffle_answer = 1
            else:
                self.shuffle_answer = 0

        # Parsing answer numbering style
        tag_answernumbering = parsed_file.find("answernumbering")
        if tag_answernumbering is not None:
            self.answer_numbering = tag_answernumbering.text

        # Parsing showstandardinstruction
        tag_showstandardinstruction = parsed_file.find("showstandardinstruction")
        if tag_showstandardinstruction is not None:
            self.show_standard_instruction = tag_showstandardinstruction.text

        # Parsing correctfeedback: it's format and text
        tag_correctfeedback = parsed_file.find("correctfeedback")
        if tag_correctfeedback is not None:
            if 'format' in tag_correctfeedback.attrib.keys():
                self.corrected_feedback['format'] = tag_correctfeedback.attrib['format']
            else:
                self.corrected_feedback['format'] = "text"
            self.corrected_feedback['text'] = tag_correctfeedback.find("text").text

        # Parsing particullary correctfeedback: it's format and text
        tag_partcorrectfeedback = parsed_file.find("partiallycorrectfeedback")
        if tag_partcorrectfeedback is not None:
            if 'format' in tag_partcorrectfeedback.attrib.keys():
                self.particular_corrected_feedback['format'] = tag_partcorrectfeedback.attrib['format']
            else:
                self.particular_corrected_feedback['format'] = "text"
            self.particular_corrected_feedback['text'] = tag_partcorrectfeedback.find("text").text

        # Parsing incorrect feedback: it's format and text
        tag_incorrfeedback = parsed_file.find("incorrectfeedback")
        if tag_incorrfeedback is not None:
            if 'format' in tag_incorrfeedback.attrib.keys():
                self.incorrect_feedback['format'] = tag_incorrfeedback.attrib['format']
            else:
                self.incorrect_feedback['format'] = "text"
            self.incorrect_feedback['text'] = tag_incorrfeedback.find("text").text

        # Parsing shownumcorrect
        tag_shownumcorrect = parsed_file.find("shownumcorrect")
        if tag_shownumcorrect is not None:
            self.show_num_correct = 1
        else:
            self.show_num_correct = 0

        # Parsing all answers
        all_answers = parsed_file.findall("answer")
        if len(all_answers) != 0:
            for tag_answer in all_answers:
                result = MultiplyChoiceAnswer()
                if "format" in tag_answer.attrib.keys():
                    result.text['format'] = tag_answer.attrib['format']
                else:
                    result.text['format'] = "text"

                # Fraction in this case means points that you have if you will correctly answer on the question
                if "fraction" in tag_answer.attrib.keys():
                    result.points = tag_answer.attrib['fraction']
                else:
                    result.points = "1"

                text = tag_answer.find("text")
                if text is not None:
                    result.text['text'] = text.text

                feedback = tag_answer.find("feedback")
                if "format" in feedback.attrib.keys():
                    result.feedback['format'] = feedback.attrib['format']
                else:
                    result.feedback['format'] = "text"
                feedback_text = feedback.find("text")
                if feedback_text is not None:
                    result.feedback['text'] = feedback_text.text

                self.options.append(result)

    def saveToFormat(self, file_name: str):
        with open(file_name, 'w', encoding='utf-8') as f:
            # Serialize the data and write it to the file
            json.dump(self, f, default= lambda o: self.__encoder(o.__dict__), ensure_ascii=False)




