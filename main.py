from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.twap import twap
from utils import log


def main():
    log("BOT STARTED")

    # EXAMPLE ORDERS:
    place_market_order("BTCUSDT", "BUY", 0.001)
    place_limit_order("BTCUSDT", "SELL", 0.001, 95000)
    # twap("BTCUSDT", "BUY", total_qty=0.01, parts=5, delay=2)

    log("BOT FINISHED")

if __name__ == "__main__":
    main()
