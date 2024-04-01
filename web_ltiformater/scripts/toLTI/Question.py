import abc


class Question(abc.ABC):
    def is_correct(self, element, el_in_dict=None):
        """ Check correctness of element. This method tries to understand the type of object (dict, list, just string) and identify it's correctness """
        if isinstance(element, dict):
            if el_in_dict is not None:
                return len(element) > 0 and el_in_dict in element and element[el_in_dict] is not None
            return len(element) > 0
        if isinstance(element, list):
            return len(element) > 0
        if isinstance(element, str):
            return element != ''
        if element is None:
            return False
        return True

