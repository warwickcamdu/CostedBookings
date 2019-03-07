from retrieve_calendars import retrieve_calendars
from create_service import create_service


def test_list_calendars_not_empty():
    service = create_service()
    val = retrieve_calendars(service)
    assert val != []