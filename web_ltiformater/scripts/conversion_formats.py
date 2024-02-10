import enum


class ConversionFormat(enum.Enum):
    MultipleChoiceMoodleXML = 0,
    MultipleChoiceMoodleCSV = 1,
    MultipleChoiceMoodleWord = 2,
    MultipleChoiceStepikStep = 3,
    MultipleChoiceTestmozWord = 4

    def __int__(self):
        return self.value[0]

    @staticmethod
    def is_multiple_choice(value: int):
        return value in range(0, 33)


