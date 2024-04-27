from module6.league.identified_object import IdentifiedObject
from datetime import datetime
from module6.league.exceptions import DuplicateOid, DuplicateEmail


class Competition(IdentifiedObject):
    @property
    def teams_competing(self):
        return self._teams_competing.copy()

    @property
    def date_time(self):
        return self._date_time

    @property
    def location(self):
        return self._location

    def __init__(self, oid, teams_competing, location, datetime):
        super().__init__(oid)
        self._teams_competing = teams_competing
        self._location = location
        self._date_time = datetime

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        if self._oid != value:
            raise DuplicateOid(value)
        self._oid = value

    def send_email(self, emailer, subject, message):
        """use the emailer argument to send an email to all members of all teams in this
        competition without duplicates. That is, a team member may be on multiple teams
        that may be competing against each other. Only send one email to each team member
        on all of the teams in this competition.  This method should send a single email
        so if the teams have N and M members respectively, the recipient list will have
        N+M elements assuming all of the members were distinct.  If the teams have S "shared"
        members then we'd expect a single email with N+M-S recipients."""

        # If a member has a non-empty email address,
        # it is added to the recipients set to make sure that it's diff.
        recipients = set()
        for team in self._teams_competing:
            for member in team.members:
                if member.email:
                    recipients.add(member.email)
            for recipient in recipients:
                emailer.send_email(recipient, subject, message)

    def __str__(self):
        """return a string like the following: "Competition at location on date_time with N teams"
        (note: date_time may be None in which case just omit the "on date_time" part.  If present,
        format the date_time property similar to the following example "12/31/1995 19:30"."""
        date_time_string = self._date_time.strftime("%m/%d") if self._date_time else None
        teams_count = len(self._teams_competing)
        return (f"Competition at {self._location}" + (f" on {date_time_string}" if date_time_string else "")
                + f" with {teams_count} teams")

