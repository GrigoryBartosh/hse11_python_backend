from src.common import Item


def get_hello_message():
    return {"message": "Hello!"}


def read_item_info(id: int):
    base = [
        Item(
            username="user_0",
            price=1.4,
            item_name="item_0"
        ),
        Item(
            price=8.8,
            item_name="item_1"
        )
    ]

    if id < 0 or id >= len(base):
        raise ValueError("incorrect id")

    return base[id]


def create_item(item: Item):
    if item.price < 0:
        raise ValueError("The price cannot be negative")

    response = Item(
        username=item.username,
        price=0.8 * item.price,
        item_name=f"{item.item_name} скидка"
    )
    return response
