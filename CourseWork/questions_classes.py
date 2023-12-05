import json

class MultiplyChoiceQuestion:
    def __init__(self, is_singl, is_html_enabld, optns, do_shuffle, corr_feed, part_corr_feed, incorr_feed):
        self.question_name = "multiply_choice"
        self.is_single_answer = is_singl
        self.is_html_enabled = is_html_enabld

        self.options = optns
        self.shuffle_answer = do_shuffle
        self.corrected_feedback = corr_feed
        self.particular_corrected_feedback = part_corr_feed
        self.incorrected_feedback = incorr_feed


class MultiplyChoiceAnswer:
    def __init__(self, txt, is_corr, feedb):
        self.text = txt
        self.is_correct = is_corr
        self.feedback = feedb


class QuestionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MultiplyChoiceQuestion):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)