import abc

from scripts.toLTI import MultipleChoiceQuestion
from scripts.toLTI.conversion_formats import ConversionFormat


class AbstractPlatformQuestion(abc.ABC):
    """
    Interface that implements every class with methods for creating another platform questions
    (LTI -> MoodleXml, Stepik ...)
    """

    @abc.abstractmethod
    def parse_one_question(self, parsed_question: MultipleChoiceQuestion, type_of_question: ConversionFormat):
        """ Creates string-view of LTI-question for specific platform (in dependent of type_of_question param) """
        pass

    def __set_parent_xml(self, parent, child):
        """ Helpful method for XML-based platforms. Assign parent object as parent for child. """
        parent.append(child)

    @staticmethod
    def __is_correct(element, el_in_dict=None):
        """ Check correctness of element. This method tries to understand the type of object (dict, list, just string) and identify it's correctness """
        if isinstance(element, dict):
            if el_in_dict is not None:
                return len(element) > 0 and el_in_dict in element and element[el_in_dict] is not None
            return len(element) > 0
        if element is None:
            return False
        return True
