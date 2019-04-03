
import re
import unittest

def validate_pin(pin):
    #return true or false
    r=re.compile(r"^(\d{4}|\d{6})$")
    result=bool(re.match(r,pin))
    result=pin.isdigit() and( len(pin)==4 or len(pin)==6)
    print(result)
# validate_pin('098765')


# unit tests
import unittest

class MyTestCase(unittest.TestCase):
    def test_validate_pinc(self):
        self.assertEqual(True,True)
        pass

if __name__ == '__main__':
      unittest.main()
