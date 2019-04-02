
#******************************************************
'''
A function that when given two strings return true if all the letters in the first array are also in the second string.

'''
#******************************************************

import unittest

# first approach
#====================================
def compareStrings(string1,string2):
    '''
    :param string1:
    :param string2:
    :return:
    '''
    if len(string1)==len(string2) and len(string2)!=0 and len(string1 )!=0:
         for i in string1:
             if i in string2:
                 continue
             else:
                 return False
         return True
    else :
        return False

#===================================================
# Second approach
# using recursion
#====================================================
def recurse(string1,string2,i):
    """
    recursing over the array
    :param string1:
    :param string2:
    :param i:
    :return:
    """
    #Terminate the loop when the array ends
    if i < len(string1):
        if string2[i] in string1:
             return recurse(string1, string2, i + 1)
    else:
        return True

def compareStrings1(string1,string2):
    '''
    Compare two strings to see if they are equal or not
    :param string1:
    :param string2:
    :return:
    '''
    if len(string1)==len(string2) and len(string2)!=0 and len(string1 )!=0:
         return  recurse(string1,string2,0)
    else :
        return False

class MyTestCase(unittest.TestCase):
    def test_lenth_comparison(self):
        self.assertEqual(compareStrings('hshsw','hshs'),False)
        self.assertEqual(compareStrings('hshsw', 'errr'), False)
    def test_equal_strings(self):
        self.assertEqual(compareStrings('hshs','hshs'),True)
        self.assertEqual(compareStrings('advd','dvba'),True)
        self.assertEqual(compareStrings('posokamalukazi','dvba'),True)


    def test_null_strings(self):
        self.assertEqual(compareStrings('',''),False)
        self.assertEqual(compareStrings('','wewee'),False)
        self.assertEqual(compareStrings('eeeee',''),False)

if __name__ == '__main__':
    unittest.main()


