from module6.league.identified_object import IdentifiedObject
from module6.league.exceptions import DuplicateOid, DuplicateEmail


class League(IdentifiedObject):
    @property
    def name(self):
        """[prop] -- the league name"""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def teams(self):
        """[r/o prop] -- list of teams participating in this league"""
        return self._teams

    @property
    def competitions(self):
        """[r/o prop] -- list of competitions (games)"""
        return self._competitions

    def __init__(self, oid, name):
        """-- initialization method that sets the oid and name properties as specified
        in the arguments (note: should call superclass constructor)"""
        super().__init__(oid)
        self._name = name
        self._teams = []
        self._competitions = []

    def add_team(self, team):
        """-- add team to the teams collection unless they are already
        in it (in which case do nothing)"""
        for existing_team in self._teams:
            if existing_team.name == team.oid:
                raise DuplicateOid(f"Team {team.oid} already exists")
        self._teams.append(team)

    def remove_team(self, team):
        """-- remove the team if they are in the teams list, otherwise do nothing"""
        for competition in self._competitions:
            if team in competition.teams_competing:
                raise ValueError("Team {team.name} cannot be removed. It's in competition {competition}")
        if team in self._teams:
            self._teams.remove(team)

    def team_named(self, team_name):
        """-- return the team in this league whose name equals team_name
        (case-sensitive) or None if no such team exists"""
        for team in self._teams:
            if team.name == team_name:
                return team
        return None

    def add_competition(self, competition):
        """-- add competition to the competitions collection"""
        for team in competition.teams_competing:
            if team not in self._teams:
                raise ValueError(f"Competition contains team {team.name} that is not part of the league")
        self._competitions.append(competition)

    def teams_for_member(self, member):
        """-- return a list of all teams for which member plays"""
        teams = []
        for team in self._teams:
            if member in team.members:
                teams.append(team)
        return teams

    def competitions_for_team(self, team):
        """-- return a list of all competitions in which team is participating"""
        competitions = []
        for competition in self._competitions:
            if team in competition.teams_competing:
                competitions.append(competition)
        return competitions

    def competitions_for_member(self, member):
        """-- return a list of all competitions for which member played on one of the competing teams"""
        teams = self.teams_for_member(member)
        competitions = []
        for team in teams:
            competitions.extend(self.competitions_for_team(team))
        return competitions

    def __str__(self):
        """-- return a string resembling the following: "League Name: N teams, M competitions"
        where N and M are replaced by the obvious values"""
        teams_count = len(self._teams)
        competitions_count = len(self._competitions)
        return f"{self.name}: {teams_count} teams, {competitions_count} competitions"
