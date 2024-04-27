from module6.league.identified_object import IdentifiedObject
from module6.league.exceptions import DuplicateOid, DuplicateEmail
from module6.league.team import Team
from module6.league.team_member import TeamMember

import pickle
import csv
import os


class LeagueDatabase:
    """A singleton class to manage leagues"""

    _sole_instance = None

    def __init__(self):
        self.leagues = []
        self._last_oid = 0

    @classmethod
    def instance(cls):
        """returns the sole instance of this database, creating one if it doesn't exist yet"""
        if cls._sole_instance is None:
            cls._sole_instance = LeagueDatabase()
        return cls._sole_instance

    @classmethod
    def load(cls, file_name):
        if not os.path.isfile(file_name):
            print(f"File does not exist: {file_name}. If available, will load from backup.")
            file_name += ".backup"

        try:
            with open(file_name, "rb") as file:
                cls._sole_instance = pickle.load(file)
        except Exception as e:
            print(f"Could not load file '{file_name}': {e}")
            backup_file = file_name + ".backup"
            if os.path.isfile(backup_file):
                try:
                    with open(backup_file, "rb") as backup:
                        cls._sole_instance = pickle.load(backup)
                except Exception as e:
                    print(f"Could not load backup file '{backup_file}': {e}")

    def save(self, file_name):
        backup_file_name = file_name + ".backup"
        if os.path.isfile(file_name):
            os.rename(file_name, backup_file_name)

        try:
            with open(file_name, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Could not save file '{file_name}': {e}")

    def add_league(self, league):
        self.leagues.append(league)

    def remove_league(self, league):
        if league in self.leagues:
            self.leagues.remove(league)

    def league_named(self, name):
        for league in self.leagues:
            if league.name == name:
                return league
        return None

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid

    def import_league_teams(self, league, file_name):
        """load the teams and team members in a league from a CSV formatted file."""
        try:
            with open(file_name, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    team_name = row['Team name']
                    member_name = row['Member name']
                    email = row['Member email']

                    team = league.team_named(team_name)

                    if not team:
                        team_oid = self.next_oid()
                        team = Team(team_oid, team_name)
                        league.add_team(team)

                    member_oid = self.next_oid()
                    member = TeamMember(member_oid, member_name, email)

                    team.add_member(member)

            print(f"Successfully imported from '{file_name}'")

        except Exception as e:
            print(f"Could not import league teams from '{file_name}: {e}")

    @staticmethod
    def export_league_teams(self, league, file_name):
        header = ['Team name', 'Member name', 'Member email']
        try:
            with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)

                for team in league.teams:
                    for member in team.members:
                        writer.writerow([team.name, member.name, member.email])
        except Exception as e:
            print(f"Could not export league teams to '{file_name}': {e}")
