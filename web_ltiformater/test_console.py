from FormatsHandler import FormatsHandler
from scripts.toLTI.conversion_formats import ConversionFormat

handler = FormatsHandler()
question = (handler.process_request_based_question(8113749, 16190693, int(ConversionFormat.CanvasInstructure), int(ConversionFormat.LTI)))

print(handler.get_text(question))