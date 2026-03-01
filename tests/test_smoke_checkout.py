import pytest

@pytest.mark.smoke
class TestCheckoutSmoke:
    def test_guest_cod_checkout(self, logged_in_pages):
        pages = logged_in_pages
        pages["inventory"].add_backpack_to_cart()
        pages["cart"].go_to_checkout()
        result = pages["checkout"].complete_checkout_cod()
        assert result is True, "COD checkout failed"
