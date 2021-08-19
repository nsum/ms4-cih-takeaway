from django.test import TestCase
from .models import Order, Item, OrderLineItem
import datetime
# Create your tests here.


class TestOrder(TestCase):

    def test_order(self):
        order = Order()
        order.pickup_time = datetime.time(10, 0)
        order.pickup_date = datetime.date.today()
        order.save()
        item = Item()
        item.price = 5
        item.save()
        order_line_item = OrderLineItem(
            order=order,
            item=item,
            quantity=1,
        )
        order_line_item.save()
        order_line_item_2 = OrderLineItem(
            order=order,
            item=item,
            quantity=1,
        )
        order_line_item_2.save()
        order.update_total()
        self.assertEqual(order.order_discount, 0)
        self.assertEqual(order.grand_total, 10)
