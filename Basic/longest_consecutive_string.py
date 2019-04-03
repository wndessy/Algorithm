import unittest






def longest_consec(strarr,k):
    '''

    :param strarr: The string array to be tested
    :param k: the number of consecutive strings
    :return: the longest string combination
    '''

# if string is null,or the length ask for longer than the string itself or k less than or equal to zero return empty string
    if len(strarr)== 0 or k > len(strarr) or k <= 0:
        return ''
    else:
        lenngth=0
        longest=''
        for index,item in enumerate(strarr):
            newstr=''.join(strarr[index:index+k])
            if len(newstr)>lenngth:
                longest=newstr
                lenngth=len(longest)
        return longest


# unit tests
class MyTestCase(unittest.TestCase):
    def test_longest_consec(self):
        self.assertEqual(longest_consec(['the','quick','brown','fox','jumps','over','the','lazy','dog'],2), 'quickbrown')
        self.assertEqual(longest_consec(["one", "two", "three", "fourteen", "five", "six", "seven", "eight"],2),'threefourteen')
        self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2),'abigailtheta')

if __name__ == '__main__':
      unittest.main()
