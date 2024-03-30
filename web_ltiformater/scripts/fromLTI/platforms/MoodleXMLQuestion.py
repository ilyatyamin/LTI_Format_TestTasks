from scripts.fromLTI.platforms.AbstractPlatformQuestion import AbstractPlatformQuestion
from scripts.toLTI import MultipleChoiceQuestion

import xml.etree.ElementTree as ElTree
import xml.dom.minidom as minidom

from scripts.toLTI.conversion_formats import ConversionFormat


class MoodleXMLQuestion(AbstractPlatformQuestion):
    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question: ConversionFormat, presentation='string'):
        if type_of_question == ConversionFormat.MultipleChoiceMoodleXML:
            question_tag = ElTree.Element("question")
            question_tag.set("type", "multichoice")

            name_tag = ElTree.Element('name')
            self.set_parent_xml(question_tag, name_tag)
            if self.is_correct(parsed_question.question_name):
                name_text_tag = ElTree.Element('text')
                self.set_parent_xml(name_tag, name_text_tag)
                name_text_tag.text = parsed_question.question_name

            questiontext_tag = ElTree.Element("questiontext")
            self.set_parent_xml(question_tag, questiontext_tag)
            if self.is_correct(parsed_question.question_text, 'format'):
                questiontext_tag.set("format", str(parsed_question.question_text['format']))

            questiontext_text_tag = ElTree.Element("text")
            self.set_parent_xml(questiontext_tag, questiontext_text_tag)
            if self.is_correct(parsed_question.question_text, 'text'):
                questiontext_text_tag.text = parsed_question.question_text['text']

            generalfeedback_tag = ElTree.Element("generalfeedback")
            self.set_parent_xml(question_tag, generalfeedback_tag)
            if self.is_correct(parsed_question.general_feedback, 'format'):
                generalfeedback_tag.set("format", str(parsed_question.general_feedback['format']))

            generalfeedback_text_tag = ElTree.Element('text')
            self.set_parent_xml(generalfeedback_tag, generalfeedback_text_tag)
            if self.is_correct(parsed_question.general_feedback, 'text'):
                generalfeedback_text_tag.text = parsed_question.general_feedback['text']

            defaultgrade_tag = ElTree.Element('defaultgrade')
            self.set_parent_xml(question_tag, defaultgrade_tag)
            if self.is_correct(parsed_question.default_grade):
                defaultgrade_tag.text = parsed_question.default_grade

            penalty_tag = ElTree.Element('penalty')
            self.set_parent_xml(question_tag, penalty_tag)
            if self.is_correct(parsed_question.penalty):
                penalty_tag.text = parsed_question.penalty

            hidden_tag = ElTree.Element('hidden')
            self.set_parent_xml(question_tag, hidden_tag)
            if self.is_correct(parsed_question.hidden):
                hidden_tag.text = parsed_question.hidden

            idnumber_tag = ElTree.Element('idnumber')
            self.set_parent_xml(question_tag, idnumber_tag)
            if self.is_correct(parsed_question.course_id):
                idnumber_tag.text = parsed_question.course_id

            single_tag = ElTree.Element('single')
            self.set_parent_xml(question_tag, single_tag)
            if str(parsed_question.is_single_answer) == '1':
                single_tag.text = 'true'
            else:
                single_tag.text = 'false'

            shuffleanswers_tag = ElTree.Element('shuffleanswers')
            self.set_parent_xml(question_tag, shuffleanswers_tag)
            if str(parsed_question.shuffle_answer) == '1':
                shuffleanswers_tag.text = 'true'
            else:
                shuffleanswers_tag.text = 'false'

            answernumbering_tag = ElTree.Element('answernumbering')
            self.set_parent_xml(question_tag, answernumbering_tag)
            if self.is_correct(parsed_question.answer_numbering):
                answernumbering_tag.text = parsed_question.answer_numbering

            showstandartinstruction_tag = ElTree.Element('showstandardinstruction')
            self.set_parent_xml(question_tag, showstandartinstruction_tag)
            if self.is_correct(parsed_question.show_standard_instruction):
                showstandartinstruction_tag.text = parsed_question.show_standard_instruction

            correctedfeedback_tag = ElTree.Element('correctedfeedback')
            self.set_parent_xml(question_tag, correctedfeedback_tag)
            if self.is_correct(parsed_question.corrected_feedback, 'format'):
                correctedfeedback_tag.set('format', parsed_question.corrected_feedback['format'])

            correctedfeedback_text_tag = ElTree.Element('text')
            self.set_parent_xml(correctedfeedback_tag, correctedfeedback_text_tag)
            if self.is_correct(parsed_question.corrected_feedback, 'text'):
                correctedfeedback_text_tag.text = parsed_question.corrected_feedback['text']

            partiallycorrectfeedback_tag = ElTree.Element('partiallycorrectfeedback')
            self.set_parent_xml(question_tag, partiallycorrectfeedback_tag)
            if self.is_correct(parsed_question.particular_corrected_feedback, 'format'):
                partiallycorrectfeedback_tag.set('format', parsed_question.particular_corrected_feedback['format'])

            partiallycorrectfeedback_text_tag = ElTree.Element('text')
            self.set_parent_xml(partiallycorrectfeedback_tag, partiallycorrectfeedback_text_tag)
            if self.is_correct(parsed_question.particular_corrected_feedback, 'text'):
                partiallycorrectfeedback_text_tag.text = parsed_question.particular_corrected_feedback['text']

            incorrectfeedback_tag = ElTree.Element('incorrectfeedback')
            self.set_parent_xml(question_tag, incorrectfeedback_tag)
            if self.is_correct(parsed_question.incorrect_feedback, 'format'):
                incorrectfeedback_tag.set('format', parsed_question.incorrect_feedback['format'])

            incorrectfeedback_text_tag = ElTree.Element('text')
            self.set_parent_xml(incorrectfeedback_tag, incorrectfeedback_text_tag)
            if self.is_correct(parsed_question.incorrect_feedback, 'text'):
                incorrectfeedback_text_tag.text = parsed_question.incorrect_feedback['text']

            shownumcorrect_tag = ElTree.Element('shownumcorrect')
            self.set_parent_xml(question_tag, shownumcorrect_tag)
            if self.is_correct(parsed_question.show_num_correct):
                shownumcorrect_tag.text = str(parsed_question.show_num_correct)

            for option in parsed_question.options:
                option_tag = ElTree.Element('answer')
                self.set_parent_xml(question_tag, option_tag)
                if self.is_correct(option.text, 'format'):
                    option_tag.set('format', option.text['format'])
                if self.is_correct(option.points):
                    option_tag.set('fraction', str(option.points))

                option_text_tag = ElTree.Element('text')
                self.set_parent_xml(option_tag, option_text_tag)
                if self.is_correct(option.text, 'text'):
                    option_text_tag.text = str(option.text['text'])

                option_feedback_tag = ElTree.Element('feedback')
                self.set_parent_xml(option_tag, option_feedback_tag)
                if self.is_correct(option.feedback, 'format'):
                    option_feedback_tag.set('format', str(option.feedback['format']))

                option_feedback_text_tag = ElTree.Element('text')
                self.set_parent_xml(option_feedback_tag, option_feedback_text_tag)
                if self.is_correct(option.feedback, 'text'):
                    option_feedback_text_tag.text = str(option.feedback['text'])

            if presentation == 'string':
                answer = ElTree.tostring(question_tag, encoding='unicode')
                return minidom.parseString(answer).toprettyxml()
            elif presentation == 'xml':
                return question_tag
            else:
                raise Exception('Incorrect presentation tag!')

    def parse_questions(self, parsed_questions: list, type_of_question: ConversionFormat, presentation='string'):
        quiz_tag = ElTree.Element('quiz')

        for question in parsed_questions:
            xml_presentation = self.parse_one_question(question, ConversionFormat.MultipleChoiceMoodleXML, presentation='xml')
            self.set_parent_xml(quiz_tag, xml_presentation)

        if presentation == 'string':
            answer = ElTree.tostring(quiz_tag, encoding='unicode')
            return minidom.parseString(answer).toprettyxml()
        elif presentation == 'xml':
            return quiz_tag
        else:
            raise Exception('Incorrect presentation tag!')
