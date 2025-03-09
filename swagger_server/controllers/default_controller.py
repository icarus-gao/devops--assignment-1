import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds a student to the system # noqa: E501

    :param body: Student object to add
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_student(student_id):  # noqa: E501
    """Deletes a student

    Deletes a single student # noqa: E501

    :param student_id: The student ID
    :type student_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_student_by_id(student_id):  # noqa: E501
    """Gets student

    Returns a single student # noqa: E501

    :param student_id: The student ID
    :type student_id: int

    :rtype: Student
    """
    return 'do some magic!'
