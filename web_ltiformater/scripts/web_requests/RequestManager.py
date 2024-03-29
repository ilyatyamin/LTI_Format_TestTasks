import requests

from scripts.web_requests.RequestPlatform import RequestPlatform


class RequestManager:
    @staticmethod
    def __token():
        return '7~dD2pttvuJBP63gn3gMh1HFTQ4rVZNL3G66mnZIJJDi6dImZDtq2s4moEzusPQd7m'

    @staticmethod
    def get_all_courses(platform: RequestPlatform):
        if platform == RequestPlatform.Canvas:
            return requests.get(f'https://canvas.instructure.com/api/v1/courses?access_token={RequestManager.__token()}')

    @staticmethod
    def get_all_assignments_in_course(courseId: int, platform: RequestPlatform):
        if platform == RequestPlatform.Canvas:
            return requests.get(
                f'https://canvas.instructure.com/api/v1/courses/{courseId}/assignments?access_token={RequestManager.__token()}')

    @staticmethod
    def get_assignment_info(courseId: int, assignmentId: int, platform: RequestPlatform):
        if platform == RequestPlatform.Canvas:
            return requests.get(
                f'https://canvas.instructure.com/api/v1/courses/{courseId}/quizzes/{assignmentId}/questions?access_token={RequestManager.__token()}')

    @staticmethod
    def get_quiz_info(courseId: int, quizId: int, platform: RequestPlatform):
        if platform == RequestPlatform.Canvas:
            return requests.get(
                f'https://canvas.instructure.com/api/v1/courses/{courseId}/quizzes/{quizId}/questions?access_token={RequestManager.__token()}')
