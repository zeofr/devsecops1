from calc import add

def test_add():
    # This will now fail the build because 5 != 6
    assert add(2, 3) == 6

# You MUST add this line to actually run the function!
test_add()
