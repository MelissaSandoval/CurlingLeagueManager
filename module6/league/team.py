from module6.league.identified_object import IdentifiedObject
from module6.league.exceptions import DuplicateOid, DuplicateEmail


class Team(IdentifiedObject):
    def name(self):
        """name of team member"""
        return self._name

    def members(self):
        """list of team members"""
        return self._members

    def __init__(self, oid, name):
        """initialization method that sets the oid and name properties
        as specified in the arguments (note: should call superclass constructor)"""
        super().__init__(oid)
        self.oid = oid
        self._name = name
        self._members = []

    def add_member(self, member):
        """ignore request to add team member that's already in members"""
        for existing_member in self._members:
            if existing_member.email.lower() == member.email.lower():
                raise DuplicateEmail(f"Team member with email {member.email} already exists")
        self._members.append(member)

    def member_named(self, s, none=None):
        """return member of this team whose name equals s or none if it doesn't exist"""
        for member in self._members:
            if member.name == s:
                return member
        return none

    def team_named(self, s, none=None):
        return none

    def remove_member(self, member):
        """remove the specified member from the team"""
        if member in self._members:
            self._members.remove(member)

    def send_email(self, emailer, subject, message):
        """use the emailer argument to email all members of a team except
        those whose email address is None.  This method should send a single email
        so if the team has N members, the recipient list will have N elements."""
        recipients = [member.email for member in self.members]
        emailer.send_plain_email(recipients, subject, message)

    def __str__(self):
        """return a string like the following: "Team Name: N members"""
        return f"Team Name: {self.name}\nMembers: {self.members()}"
