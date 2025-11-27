from .client import get_client
from .utils import log

client = get_client()

def place_limit_order(symbol, side, quantity, price):
    try:
        log(f"Placing LIMIT order: {side} {quantity} {symbol} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )

        log(order)
        return order

    except Exception as e:
        log(f"ERROR: {e}")
        return None
