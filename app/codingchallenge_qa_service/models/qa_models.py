from enum import Enum
from typing import Dict, Any
from pydantic import BaseModel


class UserType(str, Enum):
    """
    Enum representing the type of user.

    This enum defines the possible types of users, such as student, tutor, developer, or unknown.

    Possible values:
        - STUDENT: Represents a student user.
        - TUTOR: Represents a tutor user.
        - DEVELOPER: Represents a developer user.
        - UNKNOWN: Represents an unknown user type.

    """

    STUDENT = "student"
    TUTOR = "tutor"
    DEVELOPER = "dev"
    UNKNOWN = "unknown"


class ClientCode(str, Enum):
    """
    Enum representing the code of the client.

    This enum defines the possible codes for different clients, such as MS Teams, Alexa, or native.

    Possible values:
        - MS_TEAMS: Represents the MS Teams client.
        - ALEXA: Represents the Alexa client.
        - NATIVE: Represents a native client.

    """

    MS_TEAMS = "ms_teams"
    ALEXA = "alexa"
    NATIVE = "native"


class User(BaseModel):
    """
    Model representing a user.

    This model defines the structure of a user, including their ID and user type.

    Attributes:
        id (str): The ID of the user.
        type (UserType): The type of the user.

    """

    id: str
    type: UserType


class Client(BaseModel):
    """
    Model representing a client.

    This model defines the structure of a client, including the client code and additional details.

    Attributes:
        code (ClientCode): The code representing the client.
        details (Dict[str, Any]): Additional details about the client.

    """

    code: ClientCode
    details: Dict[str, Any]


class Language(str, Enum):
    """
    Enum representing a language.

    This enum defines the possible language options, such as English (EN) or German (DE).

    Possible values:
        - EN: Represents the English language.
        - DE: Represents the German language.

    """

    EN = "en"
    DE = "de"
