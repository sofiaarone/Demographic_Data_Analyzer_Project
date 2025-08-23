import unittest
from demographic_data_analyzer import calculate_demographic_data

# test file to check if our function works correctly
class TestDemographicData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.results = calculate_demographic_data(print_data=False)

    
    def test_race_count(self):
        # check if race count exists and has at least these categories
        race_count = self.results['race_count']
        self.assertIsNotNone(race_count)
        self.assertIn('White', race_count.index)
        self.assertIn('Black', race_count.index)

    def test_average_age_men(self):
        # average age should be a number higher than 0
        avg_age = self.results['average_age_men']
        self.assertIsInstance(avg_age, float)
        self.assertGreater(avg_age, 0)

    def test_percentage_bachelors(self):
        # percentage must be between 0 and 100
        pct_bach = self.results['percentage_bachelors']
        self.assertIsInstance(pct_bach, float)
        self.assertGreaterEqual(pct_bach, 0)
        self.assertLessEqual(pct_bach, 100)

    def test_higher_education_rich(self):
         # checking percentage of rich people with higher education
        higher_rich = self.results['higher_education_rich']
        self.assertIsInstance(higher_rich, float)
        self.assertGreaterEqual(higher_rich, 0)
        self.assertLessEqual(higher_rich, 100)

    def test_lower_education_rich(self):
        # same thing but for people with lower education
        lower_rich = self.results['lower_education_rich']
        self.assertIsInstance(lower_rich, float)
        self.assertGreaterEqual(lower_rich, 0)
        self.assertLessEqual(lower_rich, 100)

    def test_min_work_hours(self):
         # the minimum working hours per week should be higher or = 0
        min_hours = self.results['min_work_hours']
        self.assertIsInstance(min_hours, int)
        self.assertGreaterEqual(min_hours, 0)

    def test_rich_percentage(self):
        # check percentage of people working min hours but making more than 50K
        rich_pct = self.results['rich_percentage']
        self.assertIsInstance(rich_pct, float)
        self.assertGreaterEqual(rich_pct, 0)
        self.assertLessEqual(rich_pct, 100)

    def test_highest_earning_country(self):
        # check which country has the highest percentage of rich people
        country = self.results['highest_earning_country']
        pct = self.results['highest_earning_country_percentage']
        self.assertIsInstance(country, str)
        self.assertIsInstance(pct, float)
        self.assertGreaterEqual(pct, 0)
        self.assertLessEqual(pct, 100)

    def test_top_IN_occupation(self):
        # check the top occupation in India 
        occupation = self.results['top_IN_occupation']
        self.assertIsInstance(occupation, str)
        self.assertGreater(len(occupation), 0)

if __name__ == "__main__":
    unittest.main()