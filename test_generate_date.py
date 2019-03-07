from generate_date import generate_date

def test_no_input():
    assert generate_date() == "2019-02-01T00:00:00.00000Z"


def test_with_input():
    input = "2015-12-22T22:11:23.98762Z"
    assert generate_date(input) == "2015-11-01T00:00:00.00000Z"

def test_broken_input():
    input = "2011-13-42T25:71:93.98762Z"
    assert generate_date(input) == None

def test_garbage_input():
    input = "some rubbish"
    assert generate_date(input) == None