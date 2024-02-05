from django import forms
from ConvertationFormats import ConvertationFormats as cf


class UserForm(forms.Form):
    choice = forms.ChoiceField(choices=
                               ((cf.MultipleChoiceMoodleXML, "MultipleChoice - Moodle XML"),
                                (cf.MultipleChoiceMoodleCSV, "MultipleChoice - Moodle CSV"),
                                (cf.MultipleChoiceMoodleWord, "MultipleChoice - Moodle Word"),
                                (cf.MultipleChoiceStepikStep, "MultipleChoice - Stepik Step"),
                                (cf.MultipleChoiceMoodleWord, "MultipleChoice - Testmoz Word")))
    file = forms.FileInput()
    name = forms.BooleanField()
