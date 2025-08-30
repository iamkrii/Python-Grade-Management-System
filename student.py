from typing import Literal

from typing import Tuple

StudentTuple = Tuple[int, str]

AssessmentType = Literal['TEST', 'ASSIGNMENT']

StudentWithMarks = Tuple[int, str, AssessmentType, int]

# Constants for grade weighting
ASSIGNMENT_WEIGHT = 0.4
TEST_WEIGHT = 0.6