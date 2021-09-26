import pytest

from src.common import Item
from src import model


def test_get_hello_message():
    response = model.get_hello_message()

    assert response == {"message": "Hello!"}


class TestReadItemInfo:
    def test_m1(self):
        with pytest.raises(ValueError):
            model.read_item_info(-1)

    def test_0(self):
        exp_item = Item(
            username="user_0",
            price=1.4,
            item_name="item_0"
        )

        resp_item = model.read_item_info(0)

        assert resp_item == exp_item


    def test_1(self):
        exp_item = Item(
            price=8.8,
            item_name="item_1"
        )

        resp_item = model.read_item_info(1)

        assert resp_item == exp_item

    def test_2(self):
        with pytest.raises(ValueError):
            model.read_item_info(-1)


class TestCreateItem:
    def test_neg_price(self):
        item = Item(
            price=-1,
            item_name="item"
        )

        with pytest.raises(ValueError):
            model.create_item(item)

    def test_no_username(self):
        item = Item(
            price=1,
            item_name="item"
        )

        resp_item = model.create_item(item)

        assert resp_item.username is None

    def test_prise(self):
        item = Item(
            price=1,
            item_name="item"
        )

        resp_item = model.create_item(item)

        assert resp_item.price == 0.8 * item.price