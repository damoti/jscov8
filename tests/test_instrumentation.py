import pytest
from jscov8 import instrument

def test_declarations():
    js = """
    var bags, trucks = 11, cars = 9;
    function main_func() {
        var elephants = 10;
    }
    """
    expected = """
    track(5);var bags, trucks = 11, cars = 9;
    function main_func() {
        track(73);var elephants = 10;
    }
    """
    assert instrument(js) == expected

@pytest.mark.xfail()
def test_objectliteral():
    # this was a bug in pyv8
    js = """
    var bags = {
        thefunc: function () {
            var elephants = 10;
        }
    }
    """
    expected = """
    track(5);var bags = {
        thefunc: function () {
            track(10);var elephants = 10;
        }
    }
    """
    assert instrument(js) == expected
