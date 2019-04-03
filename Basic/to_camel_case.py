import re
def to_camel_case(text):
    #your code here
    if text!='':
        res=re.split('_|-', text)
        [i.capitalize() for i in res]
        # print(res)

        #        map(lambda x:x.lower(),res)
        if  text[0].islower():
             # res[0]=res[0].lower()
             print(res[0])

        res2=''.join(res)
        return res2
    else :
          return text

# print(to_camel_case("a-b-c"))
# print(to_camel_case("the-stealth-warrior"))

# print(to_camel_case("A-B-C"))


# unit tests
import unittest

class MyTestCase(unittest.TestCase):
    def test_validate_pinc(self):
        self.assertEqual(True,True)
        pass

if __name__ == '__main__':
      unittest.main()
