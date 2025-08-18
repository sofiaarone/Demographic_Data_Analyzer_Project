import unittest
from demographic_data_analyzer import calculate_demographic_data

class TestDemographicData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.results = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        race_count = self.results['race_count']
        self.assertIsNotNone(race_count)
        self.assertIn('White', race_count.index)
        self.assertIn('Black', race_count.index)

    def test_average_age_men(self):
        avg_age = self.results['average_age_men']
        self.assertIsInstance(avg_age, float)
        self.assertGreater(avg_age, 0)

    def test_percentage_bachelors(self):
        pct_bach = self.results['percentage_bachelors']
        self.assertIsInstance(pct_bach, float)
        self.assertGreaterEqual(pct_bach, 0)
        self.assertLessEqual(pct_bach, 100)

    def test_higher_education_rich(self):
        higher_rich = self.results['higher_education_rich']
        self.assertIsInstance(higher_rich, float)
        self.assertGreaterEqual(higher_rich, 0)
        self.assertLessEqual(higher_rich, 100)

    def test_lower_education_rich(self):
        lower_rich = self.results['lower_education_rich']
        self.assertIsInstance(lower_rich, float)
        self.assertGreaterEqual(lower_rich, 0)
        self.assertLessEqual(lower_rich, 100)

    def test_min_work_hours(self):
        min_hours = self.results['min_work_hours']
        self.assertIsInstance(min_hours, int)
        self.assertGreaterEqual(min_hours, 0)

    def test_rich_percentage(self):
        rich_pct = self.results['rich_percentage']
        self.assertIsInstance(rich_pct, float)
        self.assertGreaterEqual(rich_pct, 0)
        self.assertLessEqual(rich_pct, 100)

    def test_highest_earning_country(self):
        country = self.results['highest_earning_country']
        pct = self.results['highest_earning_country_percentage']
        self.assertIsInstance(country, str)
        self.assertIsInstance(pct, float)
        self.assertGreaterEqual(pct, 0)
        self.assertLessEqual(pct, 100)

    def test_top_IN_occupation(self):
        occupation = self.results['top_IN_occupation']
        self.assertIsInstance(occupation, str)
        self.assertGreater(len(occupation), 0)

if __name__ == "__main__":
    unittest.main()