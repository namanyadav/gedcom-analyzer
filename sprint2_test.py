import unittest
from datetime import datetime
from project_03 import Person, Family, Classification
from project_03 import valid_date

classify = Classification('./test_results.ged')
nadia_sprint3_test = Classification('./nadia_sprint3_test.ged')
katya_sprint4_test = Classification('./katya_sprint4_test.ged')
maram_sprint4_test = Classification('./maram_sprint4_test.ged')
rucha_sprint4_test = Classification('./print_output.ged')
nadia_sprint4_test = Classification('./nadia_sprint4_test.ged')

class StoryTest(unittest.TestCase):

    def test_us01(self):
        'US01 test Dates (birth, marriage, divorce, death) should not be after the current date'

        day = '24 Sep 2019'
        d1= datetime.strptime(day, '%d %b %Y')
        us01= classify.us01_before_current_dates(d1)
        expect = ['INDI BIRTH ERROR', 'INDI DEAT ERROR', 'FAM MARR ERROR', 'FAM DIVO ERROR']   

        self.assertEqual(us01, expect)
    
    def test_us02(self):
        'Function that tests us02_birth_before_marriage(): US02 Birth should occur before marriage of an individual'      
        us02 = list(classify.us02_birth_before_marriage())
        expect = ["ERROR: FAMILY: US02: ID: @I1@ - Wife's birth date 2020-11-05 on line 22 occurs after her marriage date 1978-07-08 on line 458",
                  "ERROR: FAMILY: US02: ID: @I1@ - Wife's birth date 2020-11-05 on line 22 occurs after her marriage date 2020-04-24 on line 468",
                  "ERROR: FAMILY: US02: ID: @I4@ - Husband's birth date 2019-09-17 on line 53 occurs after his marriage date 2016-08-11 on line 477",
                  "ERROR: FAMILY: US02: ID: @I5@ - Wife's birth date 2019-09-18 on line 63 occurs after her marriage date 2006-07-14 on line 488"]
        self.assertEqual(us02,expect)
       
    def test_us03(self):
        'US03 test Birth should occur before death of an individual'
        
        us03 = list(classify.us03_birth_before_death())
        expect = ['ERROR: INDIVIDUAL: US03: @I2@: Died on 30 SEP 1943: line (34): before born on 22 FEB 1944']

        self.assertEqual(us03,expect)

    def test_us04(self):
        """Function that tests us04_marriage_before_divorse()"""
        marriage_divorse = list(classify.us04_marriage_before_divorse())
        expect = ['ERROR: FAMILY: US04: @F4@: Divorced on 13 DEC 2005 (line 490) before married on 14 JUL 2006 (line 488)']
        print(marriage_divorse)
        self.assertEqual(marriage_divorse, expect)
        
    def test_us05(self):
        """Function that tests us05_marriage_before_death()"""
        marriage = list(classify.us05_marriage_before_death())
        expect =["ERROR: FAMILY: US05: @F1@: Married on 1978-07-08 (line 458) after Death of Husband on 1943-09-30 (line 34)","ERROR: FAMILY: US05: @F13@: Married on 2019-07-08 (line 557) after Death of Wife on 2000-06-12 (line 324)"]
        print(marriage)
        self.assertEqual(marriage, expect)

    def test_us06(self):
        """Function that tests us06_divorce_before_death()"""
        divorse = list(classify.us06_divorce_before_death())
        expect = ["ERROR: FAMILY: US06: @F2@: Divorced on 2021-03-23 (line 470) after Death of Husband on 2020-11-30 (line 44)","ERROR: FAMILY: US06: @F12@: Divorced on 2016-03-10 (line 549) after Death of Wife on 2000-09-30 (line 303)"]
        print(divorse)
        self.assertEqual(divorse, expect)

    def test_us07(self):
        """Function tests us07_over150()"""
        us07 = list(classify.us07_over150())
        print(us07)
        expect = ['ERROR: INDIVIDUAL: US07: @31@ More than 150 years old: Birthday 16 DEC 1770 (line 281)', 
                'ERROR: INDIVIDUAL: US07: @32@ More than 150 years old at death: Birthday 31 MAR 1685 (line 286), Death date 31 MAR 1887 (line 288)',
                'ERROR: INDIVIDUAL: US07: @33@ More than 150 years old: Birthday 31 MAR 1685 (line 293)']          
        self.assertEqual(us07, expect)

    def test_us8(self):
        """ """
        us08 = list(classify.us08_birth_before_marriage_of_parents())
        expect = ['ERROR:US08: child @I8@ birthday 10 AUG 1997: occure before marriage 24 APR 2020 on (line 96)',
                  'ERROR:US08: child @I9@ birthday 3 NOV 1995: occure before marriage 24 APR 2020 on (line 106)',
                  'ERROR:US08: child @I17@ birthday 15 JUN 2013: occure before marriage 24 NOV 2014 on (line 172)',
                  'ERROR:US08: child @I13@ birthday 23 JUL 2012: occure after 9 months of parents divorced date 13 DEC 2005 on (line 140)',
                  'ERROR:US08: child @I14@ birthday 19 DEC 2009: occure after 9 months of parents divorced date 13 DEC 2005 on (line 147)',
                  'ERROR:US08: child @I15@ birthday 12 DEC 2014: occure after 9 months of parents divorced date 13 DEC 2005 on (line 154)']
        self.assertEqual(us08, expect)
    
    def test_us10(self):
        """Function that tests us10_marriage_after14() US10: parents must be at least 14 years old at the time of marriage""" 
        us10 = list(classify.us10_marriage_after14())
        expect = ["ERROR: FAMILY: US10: ID: @F1@: wife's age is less than 14 years old at the time of marriage 8 JUL 1978 (line 458)",
                  "ERROR: FAMILY: US10: ID: @F2@: wife's age is less than 14 years old at the time of marriage 24 APR 2020 (line 468)",
                  "ERROR: FAMILY: US10: ID: @F3@: husband's age is less than 14 years old at the time of marriage 11 AUG 2016 (line 477)",
                  "ERROR: FAMILY: US10: ID: @F4@: wife's age is less than 14 years old at the time of marriage 14 JUL 2006 (line 488)"]
        self.assertEqual(us10, expect)
    
    def test_us12_parents_not_too_old(self):
        """Function that tests us12_parents_not_too_old() US12: Mother should be less than 60 years older than her children and father should be less than 80 years older than his children"""
        us12 = list(classify.us12_parents_not_too_old())
        expect = ["ERROR: FAMILY: US12: ID: @I47@ Father's birthday 21 NOV 1914 (line 423) occurs more than 80 years before his child's birthday 31 OCT 1995 (line 435)",
                  "ERROR: FAMILY: US12: ID: @I47@ Father's birthday 21 NOV 1914 (line 423) occurs more than 80 years before his child's birthday 1 NOV 1996 (line 441)",
                  "ERROR: FAMILY: US12: ID: @I48@ Mother's birthday 19 OCT 1934 (line 429) occurs more than 60 years before her child's birthday 31 OCT 1995 (line 435)",
                  "ERROR: FAMILY: US12: ID: @I48@ Mother's birthday 19 OCT 1934 (line 429) occurs more than 60 years before her child's birthday 1 NOV 1996 (line 441)"]
        self.assertEqual(us12, expect)
    
    def test_us14_multiple_siblings(self):
        """Funciton that tests us14_multiple_siblings() US14: Family should not have more than 5 siblings with the same birthday"""
        us14 = list(classify.us14_multiple_siblings())
        expect = ['ERROR: FAMILY: US14: Family with ID @F14@ on line 558 has more than 5 siblings with the same birthday']
        self.assertEqual(us14, expect)

    def test_us15_fewer_than_15_siblings(self):
        """Function that tesdts user story 15: there sould nbe less that 15 siblings in a family"""
        us15 = list(nadia_sprint4_test.us15_fewer_than_15_siblings())
        expect = ['ERROR: FAMILY: US15: Family with ID @F22@ on line 356 has 15 or more children', 
                'ERROR: FAMILY: US15: Family with ID @F23@ on line 375 has 15 or more children']
        self.assertEqual(us15, expect)
    
    def test_us16_male_last_names(self):
        """Function that tests us16_male_last_names()"""
        us16 = list(katya_sprint4_test.us16_male_last_names())
        expect = ['ERROR: US16: Last names of male members of the family are not the same (Family Line #677)',
                  'ERROR: US16: Last names of male members of the family are not the same (Family Line #686)',
                  'ERROR: US16: Last names of male members of the family are not the same (Family Line #702)',
                  'ERROR: US16: Last names of male members of the family are not the same (Family Line #721)',
                  'ERROR: US16: Last names of male members of the family are not the same (Family Line #741)']
        self.assertEqual(us16, expect)

    def test_us17_no_marriage_to_childeren(self):
        """Function tests user story 17 which returns an error for parents married to children"""
        us17 = list(nadia_sprint3_test.us17_no_marriage_to_childeren())
        expect = ['ERROR: FAMILY: US17: Family with ID @F17@ on line 143 is a marriage between father and a child', 
                   'ERROR: FAMILY: US17: Family with ID @F18@ on line 148 is a marriage between mother and a child']
        self.assertEqual(us17, expect)

    def test_us18_siblings_marriage(self):
        """Function tests user story 18 which returns an error for marriage between siblings"""
        us18 = list(nadia_sprint3_test.us18_siblings_marriage())
        expect = ['ERROR: FAMILY: US18: Family with ID @F19@ on line 153 is a marriage between siblings',
                    'ERROR: FAMILY: US18: Family with ID @F20@ on line 160 is a marriage between siblings']
        self.assertEqual(us18, expect)
    
    def test_us21_correct_gender(self):
        'function that tests us21_correct_gende(),Husband in family should be male and wife in family should be female'
        us21 = list(classify.us21_correct_gender())
        expect = ['ERROR: US21: wife ID @I5@: on line# 61, has incorrect gender M', 'ERROR: US21 husband ID @I4@: on line# (51), has incorrect gender F']
        self.assertEqual(us21, expect)
    
    def test_us23_uniquename_and_birthdate(self):
        'test us23_uniquename_and_birthdate() No more than one individual with the same name and birth date should appear in a GEDCOM file'
        us23 = list(classify.us23_uniquename_and_birthdate())
        expect = ['ERROR: US23 Individual name Johann /Bach and birthday 31 MAR 1685: on name_line# (290) , birth_line# (293), already exist']
        self.assertEqual(us23,expect)
    
    def test_us25_unique_first_names_in_families(self):
        'No more than one child with the same name and birth date should appear in a family'
        us25 = list(maram_sprint4_test.us25_unique_first_names_in_families())
        expect = ['ERROR: US25: Child name Gene /Belcher/ and birthday 1 NOV 1994 with ID @I56@ on family (@F16@) already exist in the family']
        self.assertEqual(us25, expect)

    def test_us27(self):
        """Function that tests us27_individual_ages()"""
        individual_ages = list(classify.us27_individual_ages())
        expect =  [('@I3@', 71), ('@I4@', 0), ('@I5@', 0), ('@I6@', 39), ('@I7@', 35), ('@I8@', 22), ('@I9@', 24),
                    ('@I10@', 39), ('@I11@', 3), ('@I12@', 36), ('@I13@', 7), ('@I14@', 9), ('@I15@', 4),
                    ('@I16@', 42), ('@I17@', 6), ('@I18@', 3), ('@I19@', 4), ('@I20@', 28), ('@I21@', 1),
                    ('@I23@', 1), ('@I24@', 39), ('@I25@', 34), ('@I26@', 0), ('@I27@', 40), ('@28@', 69), 
                    ('@29@', 69), ('@30@', 40), ('@31@', 248), ('@32@', 202), ('@33@', 334), ('@I33@', 49), ('@I34@', 75),
                    ('@I35@', 49), ('@I36@', 79), ('@I38@', 47), ('@I39@', 58), ('@I40@', 28), ('@I41@', 28),
                    ('@I42@', 28), ('@I43@', 28), ('@I44@', 28), ('@I45@', 28), ('@I46@', 0), ('@I47@', 104),
                    ('@I48@', 85), ('@I49@', 24), ('@I50@', 23),('@I51@', 68)]
        self.assertEqual (individual_ages, expect)
        
    def test_us28(self):
        """Function that tests us28_siblings_by_age()"""
        sorted_siblings = list(rucha_sprint4_test.us28_siblings_by_age().items())
        expect = [('@F1@', [('@I6@', 39), ('@I7@', 35), ('@I4@', 0), ('@I5@', 0)]), ('@F2@', [('@I9@', 24), ('@I8@', 22)]), ('@F3@', [('@I11@', 3)]), ('@F4@', [('@I14@', 9), ('@I13@', 7), ('@I15@', 4)]), ('@F5@', [('@I17@', 6), ('@I19@', 4), ('@I18@', 3), ('@I26@', 0)]), ('@F6@', []), ('@F7@', []), ('@F8@', [('@I21@', 1)]), ('@F9@', []), ('@F10@', [('@I23@', 1)]), ('@F12@', []), ('@F13@', []), ('@F14@', [('@I40@', 28), ('@I41@', 28), ('@I42@', 28), ('@I43@', 28), ('@I44@', 28), ('@I45@', 28)]), ('@F15@', [('@I49@', 24), ('@I50@', 23)]), ('@F16@', [('@I55@', 25), ('@I64@', 25), ('@I54@', 23)]), ('@F17@', []), ('@F18@', []), ('@F19@', [('@I52@', 59), ('@I4@', 0)]), ('@F20@', [('@I52@', 59), ('@I4@', 0)]), ('@F21@', [('@I58@', 9), ('@I59@', 9)]), ('@F22@', [('@I3@', 71), ('@I16@', 42), ('@I6@', 39), ('@I10@', 39), ('@I12@', 36), ('@I7@', 35), ('@I9@', 24), ('@I8@', 22), ('@I14@', 9), ('@I13@', 7), ('@I15@', 4), ('@I11@', 3), ('@I4@', 0), ('@I5@', 0)]), ('@F23@', [('@I3@', 71), ('@I6@', 39), ('@I10@', 39), ('@I12@', 36), ('@I7@', 35), ('@I9@', 24), ('@I8@', 22), ('@I14@', 9), ('@I13@', 7), ('@I15@', 4), ('@I11@', 3), ('@I4@', 0), ('@I5@', 0)]), ('@F24@', [('@I63@', 39), ('@I62@', 29)])]
        self.assertEqual (sorted_siblings, expect)
    
    def test_us29_list_deceased(self):
        'US29 test deceased individual'

        us29 = classify.us29_list_deceased()
        expect = [('Robert /Kardashian/', '30 SEP 1943'), ('Johann /Bach', '31 MAR 1887'), ('Jeny /Jenner/', '30 SEP 2000'), ('Yan /Jenner/', '12 JUN 2000'), ('Gomez /Addams/', '25 OCT 2019')]
        self.assertEqual (us29, expect)

    def test_us30_list_living_married(self):
        'US30 test living_married'
        
        us30 = classify.us30_list_living_married()
        expect = [('@I1@', 'Kris /Jenner/'), ('@I6@', 'Kim /Kardashian/'),
                  ('@I16@', 'Kaney /West/'), ('@I8@', 'Kylie /Jenner/'), 
                  ('@I22@', 'Travis /Scott/'), ('@I39@', 'Cindy /Potter/'), ('@I38@', 'Cory /Potter/'),  ('@I48@', 'Morticia /Addams/'), ('@I47@', 'Gomez /Addams/')]
 
        self.assertEqual (us30,expect)

    def test_us31(self):
        """Function that tests us31_living_singles()"""
        #classify = Classification('/Users/katya/Documents/Fall19/555/revised_gedcom/us31_us32.ged')
        living_singles_list = classify.us31_living_singles()
        expect =  [('@28@', 'Smith /Joseph'), ('@29@', 'Sasquatch /Kyle'), ('@30@', 'Birch /Cynthia'), ('@31@', 'Ludwig /Beethoven'), ('@33@', 'Johann /Bach'), ('@I36@', 'Chris /Kardashian/')]
        self.assertEqual (living_singles_list, expect)
    
    def test_us32(self):
        """Function that tests multiple_births()"""
        #classify = Classification('/Users/katya/Documents/Fall19/555/revised_gedcom/us31_us32.ged')
        multiple_births = classify.us32_multiple_births()
        expect = {'22 FEB 1944': ['Robert /Kardashian/', 'George /Kardashian/'], 
                  '6 NOV 1979': ['Lamar /Odom/', 'Birch /Cynthia'], 
                  '6 NOV 1950': ['Smith /Joseph', 'Sasquatch /Kyle'],
                  '31 MAR 1685': ['Johann /Bach', 'Johann /Bach'], 
                  '5 NOV 1950': ['Jeny /Jenner/', 'Yan /Jenner/'],
                  '19 NOV 1990': ['Chris /Potter/', 'Jill /Potter/', 'James /Potter/', 'Harry /Potter/', 'Katya /Potter/', 'Shawn /Potter/']
                  }
        self.assertEqual (multiple_births, expect)

    def test_us33_list_orphans(self):
        """Function tests user story 33, which lists all orphaned children: both parents are dead and the child is under 18 years old"""
        us33 = list(nadia_sprint4_test.us33_list_orphans())
        expect = [['@I58@', 'Lily /Lanister/'], ['@I59@', 'Jeoffrey /Lanister/']]
        self.assertEqual(us33, expect)

    def test_us35(self):
        """Function that tests us35_recent_births()"""
        #classify = Classification('us35_us42.ged')
        recent_births = classify.us35_recent_births()
        expect =  {'19 OCT 2019': ['Jeff /Crowley/']}
        self.assertEqual (recent_births, expect)
    
    def test_valid_date(self):
        """Function that tests valid_date()"""
        self.assertEqual (valid_date('10 SEP 2019'), True)
        self.assertEqual (valid_date('31 FRB 2019'), False)

    def test_us36(self):
        """Function that tests us36_recent_deaths()"""
        #classify = Classification('us35_us42.ged')
        recent_deaths = classify.us36_recent_deaths()
        expect =  {'25 OCT 2019': ['Gomez /Addams/']}
        self.assertEqual (recent_deaths, expect)
    
    def test_us37_list_recent_survivors_table(self):
        us37 = katya_sprint4_test.us37_list_recent_survivors()
        expect = {'Molly /Weasley/': ['Molly Weasley', 'Arthur Weasley', ['Ron Weasley', 'Fred Johnson']]}
        self.assertEqual(us37, expect)

    def test_us38(self):
        """Function that tests us38_upcomming_birthdays"""
        today = '25 JAN 2019'
        upcomming_births = classify.us38_upcomming_birthdays(today)
        expect = {'12 FEB 1980':['Damon /Thomas/'],'6 FEB 1985':['Kris /Humphries/'] ,'22 FEB 1944':['George /Kardashian/'],'22 FEB 1940':['Chris /Kardashian/']}
        self.assertEqual (upcomming_births, expect)
        
    def test_us39(self):
        """Function that tests us39_upcomming_anniversaries"""
        today ="11 NOV 2019"
        us39 = list(rucha_sprint4_test.us39_upcomming_anniversaries(today).items())
        expect = [('24 NOV 2014', ['Kaney /West/', 'Kim /Kardashian/'])]
        self.assertEqual (us39, expect)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
