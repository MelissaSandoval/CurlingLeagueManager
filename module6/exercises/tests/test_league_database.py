import unittest
from module6.league.league_database import LeagueDatabase
from module6.league.team import Team


class TestLeagueDatabase(unittest.TestCase):

    def setUp(self):
        self.db = LeagueDatabase.instance()

        self.league1 = Team(oid=1, name='Flintstones')
        self.league2 = Team(oid=2, name='Curl Jam')
        self.db.add_league(self.league1)
        self.db.add_league(self.league2)

    def tearDown(self):
        self.db.leagues = []
        self.db._sole_instance = None

    def test_add_league(self):
        new_league = Team(oid=3, name='New League')
        self.db.add_league(new_league)
        self.assertIn(new_league, self.db.leagues)

    def test_remove_league(self):
        self.db.remove_league(self.league1)
        self.assertNotIn(self.league1, self.db.leagues)

    def test_import_league_teams(self):
        csv_file = 'teams.csv'
        self.db.import_league_teams(self.league1, csv_file)

    def test_export_league_teams(self):
        csv_file = 'output_teams.csv'
        self.db.export_league_teams(self.league1, csv_file)


if __name__ == '__main__':
    unittest.main()
