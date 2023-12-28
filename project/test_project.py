from project import foods,drinks,checkout

def test_foods():
    assert foods("No.1 * 1, No.2 * 3") == "🍔🥪🥪🥪"
    assert foods("No.1 * 2, No.2 * 1") == "🍔🍔🥪"
    assert foods("No.5 * 2, No.4 * 1") == "🌮🌮🥗"
    assert foods("No.1 * 1, No.3 * 2") == "🍔🍟🍟"

def test_drinks():
    assert drinks("No.1 * 1, No.2 * 3") == "🥤☕☕☕"
    assert drinks("No.1 * 2, No.2 * 1") == "🥤🥤☕"
    assert drinks("No.5 * 2, No.4 * 1") == "🥛🥛🍹"
    assert drinks("No.1 * 1, No.3 * 2") == "🥤🧃🧃"

def test_checkout():
    assert checkout("🍔🥪🥪🥪") == 22.5
    assert checkout("🍔🍔🥪") == 20.0
    assert checkout("🌮🌮🥗") == 10.5
    assert checkout("🍔🍟🍟") == 14.5
    assert checkout("🥤☕☕☕") == 7.5
    assert checkout("🍔🍟☕") == 13.0
    assert checkout("") == 0
