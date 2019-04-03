def remove_duplicate_words(s):
    from pandas import Series as sr
    array=s.split(' ')
    s=sr(array).drop_duplicates(keep='first')


    print(' '.join(s))
    #remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')
# remove_duplicate_words("my cat is my cat fat")
