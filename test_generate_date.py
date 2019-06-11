from generate_date import generate_date, increase_month

def test_no_input():
    assert generate_date() == "2019-05-01T00:00:00.00000Z"


def test_with_input():
    input = "2015-12-22T22:11:23.98762Z"
    assert generate_date(input) == "2015-11-01T00:00:00.00000Z"

def test_broken_input():
    input = "2011-13-42T25:71:93.98762Z"
    assert generate_date(input) == None

def test_garbage_input():
    input = "some rubbish"
    assert generate_date(input) == None

def test_increase_month():
    input = "2015-11-22T22:11:23.98762Z"
    assert increase_month(input) == "2015-12-01T00:00:00.00000Z"

def test_increase_month_over_year():
    input = "2015-12-22T22:11:23.98762Z"
    assert increase_month(input) == "2016-01-01T00:00:00.00000Z"

def test_increase_month_broken_input():
    input = "2011-13-42T25:71:93.98762Z"
    assert increase_month(input) == None

def test_increase_month_garbage_input():
    input = "some rubbish"
    assert increase_month(input) == None