from item_management import add_item, view_items

def test_add_item():
    add_item("Test Item", 10.5, 5)
    items = view_items()
    assert any(item[1] == "Test Item" for item in items)
