import json
from questions_classes import *

with open("/Users/mrshrimp.it/Downloads/1107748_2_choice-3.step") as p:
    print(p)

quest1 = MultiplyChoiceQuestion(True, True, [MultiplyChoiceAnswer("Test Quiestion", False, "No")], True, "", "", "")
print(json.dumps(quest1, default=lambda o: o.__dict__))
