from .client import get_client
from .utils import log

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        log(f"Placing MARKET order: {side} {quantity} {symbol}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        log(order)
        return order

    except Exception as e:
        log(f"ERROR: {e}")
        return None
