from module6.league.identified_object import IdentifiedObject
from module6.league.exceptions import DuplicateOid, DuplicateEmail
from typing import Optional, Any


class TeamMember(IdentifiedObject):

    @property
    def name(self):
        """[prop]"""
        return self._name

    @property
    def email(self):
        """[prop]"""
        return self._email

    def __init__(self, oid, name, email):
        """-- initialization method that sets the oid, name
        and email properties as specified in the arguments
        (note: should call superclass constructor)"""
        super().__init__(oid)
        self._name = name
        self._email = email

    def send_email(self, emailer, subject, message):
        """-- use the emailer argument to email this member"""
        emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        """-- return a string like the following: "Name<Email>"""
        return f"{self.name} <{self.email}>"
