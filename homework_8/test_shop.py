"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # напишите проверки на метод check_quantity
        assert product.check_quantity(0) is True, 'вернет True, т.к. quantity продукта больше запрашиваемого'
        assert product.check_quantity(1) is True, 'вернет True, т.к. quantity продукта больше запрашиваемого'
        assert product.check_quantity(499) is True, 'вернет True, т.к. quantity продукта больше запрашиваемого'
        assert product.check_quantity(999) is True, 'вернет True, т.к. quantity продукта больше запрашиваемого'
        assert product.check_quantity(1000) is True, 'вернет True, т.к. quantity продукта равно запрашиваемому'
        assert product.check_quantity(1001) is False, 'вернет False, т.к. quantity продукта меньше запрашиваемого'


    def test_product_buy(self, product):
        # напишите проверки на метод buy
        Product.buy(product, 100)
        assert product.quantity == 900, 'Проверка через количество'

        current_quantity = product.quantity
        purchase_quantity = 500
        product.buy(purchase_quantity)
        assert product.quantity == current_quantity - purchase_quantity, 'Проверка через созданную переменную'

    def test_product_buy_more_than_available(self, product):
        #  напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert Product.buy(product, 1001)


class TestCart:
    """
        Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_in_the_cart(self, cart, product):
        cart.add_product(product, 1)

        assert product in cart.products
        assert cart.products[product] == 1

        cart.add_product(product, 10)
        assert cart.products[product] == 11

    def test_remove_product_from_the_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 5)
        assert cart.products[product] == 5

        cart.remove_product(product, 10), 'При удалении большего количества товара чем в корзине - удаляется вся позиция'
        assert product not in cart.products

        cart.add_product(product, 6)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 3)
        assert product in cart.products

        cart.clear()
        assert product not in cart.products

    def test_total_price_in_the_cart(self, cart, product):
        product_count = 5
        cart.add_product(product, product_count)

        assert cart.get_total_price() == 500
        assert cart.get_total_price() == product.price * product_count

    def test_buy_products(self, cart, product):
        current_quantity = product.quantity
        cart.add_product(product, 1)
        cart.buy()

        assert product.quantity == current_quantity - 1
        assert len(cart.products) == 0

    def test_product_buy_more_than_quantity(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            assert cart.buy()




