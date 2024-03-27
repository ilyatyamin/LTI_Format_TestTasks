from scripts.toLTI import MultipleChoiceQuestion
import xml.etree.ElementTree as ElTree

from scripts.toLTI.conversion_formats import ConversionFormat


class MoodleXMLQuestion:
    def __set_parent_xml(self, parent, child):
        parent.append(child)

    @staticmethod
    def __is_correct(element):
        if isinstance(element, dict):
            return len(element) > 0
        if element is None:
            return False
        return True

    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question : ConversionFormat):
        if type_of_question == ConversionFormat.MultipleChoiceMoodleXML:
            question_tag = ElTree.Element("question")
            question_tag.set("type", "multichoice")

            name_tag = ElTree.Element('name')
            self.__set_parent_xml(question_tag, name_tag)
            if self.__is_correct(parsed_question.question_name):
                name_text_tag = ElTree.Element('text')
                self.__set_parent_xml(name_tag, name_text_tag)
                name_text_tag.text = parsed_question.question_name

            questiontext_tag = ElTree.Element("questiontext")
            self.__set_parent_xml(question_tag, questiontext_tag)
            if self.__is_correct(parsed_question.question_text):
                questiontext_tag.set("format", str(parsed_question.question_text['format']))

            questiontext_text_tag = ElTree.Element("text")
            self.__set_parent_xml(questiontext_tag, questiontext_text_tag)
            if self.__is_correct(parsed_question.question_text):
                questiontext_text_tag.text = parsed_question.question_text['text']

            generalfeedback_tag = ElTree.Element("generalfeedback")
            self.__set_parent_xml(question_tag, generalfeedback_tag)
            if self.__is_correct(parsed_question.general_feedback):
                generalfeedback_tag.set("format", str(parsed_question.general_feedback['format']))

            generalfeedback_text_tag = ElTree.Element('text')
            self.__set_parent_xml(generalfeedback_tag, generalfeedback_text_tag)
            if self.__is_correct(parsed_question.general_feedback):
                generalfeedback_text_tag.text = parsed_question.general_feedback['text']

            defaultgrade_tag = ElTree.Element('defaultgrade')
            self.__set_parent_xml(question_tag, defaultgrade_tag)
            if self.__is_correct(parsed_question.default_grade):
                defaultgrade_tag.text = parsed_question.default_grade

            penalty_tag = ElTree.Element('penalty')
            self.__set_parent_xml(question_tag, penalty_tag)
            if self.__is_correct(parsed_question.penalty):
                penalty_tag.text = parsed_question.penalty

            hidden_tag = ElTree.Element('hidden')
            self.__set_parent_xml(question_tag, hidden_tag)
            if self.__is_correct(parsed_question.hidden):
                hidden_tag.text = parsed_question.hidden

            idnumber_tag = ElTree.Element('idnumber')
            self.__set_parent_xml(question_tag, idnumber_tag)
            if self.__is_correct(parsed_question.course_id):
                idnumber_tag.text = parsed_question.course_id

            single_tag = ElTree.Element('single')
            self.__set_parent_xml(question_tag, single_tag)
            if str(parsed_question.is_single_answer) == '1':
                single_tag.text = 'true'
            else:
                single_tag.text = 'false'

            shuffleanswers_tag = ElTree.Element('shuffleanswers')
            self.__set_parent_xml(question_tag, shuffleanswers_tag)
            if str(parsed_question.shuffle_answer) == '1':
                shuffleanswers_tag.text = 'true'
            else:
                shuffleanswers_tag.text = 'false'

            answernumbering_tag = ElTree.Element('answernumbering')
            self.__set_parent_xml(question_tag, answernumbering_tag)
            if self.__is_correct(parsed_question.answer_numbering):
                answernumbering_tag.text = parsed_question.answer_numbering

            showstandartinstruction_tag = ElTree.Element('showstandardinstruction')
            self.__set_parent_xml(question_tag, showstandartinstruction_tag)
            if self.__is_correct(parsed_question.show_standard_instruction):
                showstandartinstruction_tag.text = parsed_question.show_standard_instruction

            correctedfeedback_tag = ElTree.Element('correctedfeedback')
            self.__set_parent_xml(question_tag, correctedfeedback_tag)
            if self.__is_correct(parsed_question.corrected_feedback):
                correctedfeedback_tag.set('format', parsed_question.corrected_feedback['format'])

            correctedfeedback_text_tag = ElTree.Element('text')
            self.__set_parent_xml(correctedfeedback_tag, correctedfeedback_text_tag)
            if self.__is_correct(parsed_question.corrected_feedback):
                correctedfeedback_text_tag.text = parsed_question.corrected_feedback['text']

            partiallycorrectfeedback_tag = ElTree.Element('partiallycorrectfeedback')
            self.__set_parent_xml(question_tag, partiallycorrectfeedback_tag)
            if self.__is_correct(parsed_question.particular_corrected_feedback):
                partiallycorrectfeedback_tag.set('format', parsed_question.particular_corrected_feedback['format'])

            partiallycorrectfeedback_text_tag = ElTree.Element('text')
            self.__set_parent_xml(partiallycorrectfeedback_tag, partiallycorrectfeedback_text_tag)
            if self.__is_correct(parsed_question.particular_corrected_feedback):
                partiallycorrectfeedback_text_tag.text = parsed_question.particular_corrected_feedback['text']

            incorrectfeedback_tag = ElTree.Element('incorrectfeedback')
            self.__set_parent_xml(question_tag, incorrectfeedback_tag)
            if self.__is_correct(parsed_question.incorrect_feedback):
                incorrectfeedback_tag.set('format', parsed_question.incorrect_feedback['format'])

            incorrectfeedback_text_tag = ElTree.Element('text')
            self.__set_parent_xml(incorrectfeedback_tag, incorrectfeedback_text_tag)
            if self.__is_correct(parsed_question.incorrect_feedback):
                incorrectfeedback_text_tag.text = parsed_question.incorrect_feedback['text']

            shownumcorrect_tag = ElTree.Element('shownumcorrect')
            self.__set_parent_xml(question_tag, shownumcorrect_tag)
            if self.__is_correct(parsed_question.show_num_correct):
                shownumcorrect_tag.text = str(parsed_question.show_num_correct)

            for option in parsed_question.options:
                option_tag = ElTree.Element('answer')
                self.__set_parent_xml(question_tag, option_tag)
                if self.__is_correct(option.text):
                    option_tag.set('format', option.text['format'])
                    option_tag.set('fraction', option.points)

                option_text_tag = ElTree.Element('text')
                self.__set_parent_xml(option_tag, option_text_tag)
                if self.__is_correct(option.text):
                    option_text_tag.text = str(option.text['text'])

                option_feedback_tag = ElTree.Element('feedback')
                self.__set_parent_xml(option_tag, option_feedback_tag)
                if self.__is_correct(option.feedback):
                    option_feedback_tag.set('format', str(option.feedback['format']))

                option_feedback_text_tag = ElTree.Element('text')
                self.__set_parent_xml(option_feedback_tag, option_feedback_text_tag)
                if self.__is_correct(option.feedback):
                    option_feedback_text_tag.text = str(option.feedback['text'])

            return ElTree.dump(question_tag)
