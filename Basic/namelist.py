

def namelist(names):
    resultString=''
    for key,x in enumerate(names):
        #seccond last
        if key==len(names)-2:
            resultString += x['name'] + ' & '
        #last item
        elif key==len(names)-1:
            resultString += x['name']
        else:
            resultString += x['name'] + ','

    print(resultString)


# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])

# unit tests
import unittest

class MyTestCase(unittest.TestCase):
    def test_validate_pinc(self):
        self.assertEqual(True,True)
        pass

if __name__ == '__main__':
      unittest.main()
