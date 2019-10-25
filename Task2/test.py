# Write your tests here
from task import *

def test_get_products_from_page():
    # make by hands expected dictionary and
    # get first value from our list of books
    assert {'name': 'A Light in the ...',
            'price': 'Â£51.77',
            'image': 'http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg',
            'rating': 3,
            'Is_tock': True} == get_products_from_page('http://books.toscrape.com/index.html')[0]

    print("+ test_get_products_from_page complite with SUCCESS")

def test_get_proper_len():
    # there are 20 elements in the page
    # let's check it
    assert 20 == len(get_products_from_page('http://books.toscrape.com/index.html'))
    print("+ test_get_proper_len complite with SUCCESS")

test_get_products_from_page()
test_get_proper_len()