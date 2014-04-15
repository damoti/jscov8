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
