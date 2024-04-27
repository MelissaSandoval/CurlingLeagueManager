import unittest
from module6.league.team import Team
from module6.league.team_member import TeamMember
from module6.league.league import League
from module6.league.competition import Competition
from module6.league.exceptions import DuplicateOid, DuplicateEmail


class TestTeam(unittest.TestCase):
    def test_duplicate_oid(self):
        team = Team(1, "Team A")
        with self.assertRaises(DuplicateOid):
            team.oid = 1

    def test_duplicate_email(self):
        team = Team(1, "Team A")
        member1 = TeamMember(1, "Bob Smith", "bsmith@test.com")
        member2 = TeamMember(2, "Bill Smith", "Bsmith@test.com")
        team.add_member(member1)
        with self.assertRaises(DuplicateEmail):
            team.add_member(member2)


class TestLeague(unittest.TestCase):
    def test_add_competition_to_league(self):
        league = League(1, "Awesome League")
        team1 = Team(1, "Team A")
        team2 = Team(2, "Team B")
        competition = Competition(1, [team1, team2], "Wilson Park", None)
        league.add_team(team1)
        with self.assertRaises(ValueError):
            league.add_competition(competition)


if __name__ == '__main__':
    unittest.main()
