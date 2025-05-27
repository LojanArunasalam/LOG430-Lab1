from src.models import User, Sale, LineSale, Product
import unittest 
# Will do test afterwards, for now, I put some template test 
class TestProduct(unittest.TestCase):
    def test_product(self):
        product = Product(name="Timbits",category="Snacks",description="Tiny donut balls",prix_unitaire=0.25,stock=100)
        self.assertEqual(product.name, "Timbits")
        self.assertEqual(product.stock, 100)
        self.assertAlmostEqual(product.prix_unitaire, 0.25)

class TestSale(unittest.TestCase):
    def test_sale(self):
        assert True is True
        
class TestLineSale(unittest.TestCase):
    def test_line_sale(self):
        assert True is True


class TestUser(unittest.TestCase):
    def test_user(self):
        assert True is True