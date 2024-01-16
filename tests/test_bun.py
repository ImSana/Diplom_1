from bun import Bun


class TestBun:
    def test_get_return_name(self):
        add_bun = Bun('Краторная булка N-200i', 11.1)
        assert add_bun.get_name() == 'Краторная булка N-200i'

    def test_get_return_price(self):
        add_bun = Bun('Краторная булка N-200i', 11.1)
        assert add_bun.get_price() == 11.1