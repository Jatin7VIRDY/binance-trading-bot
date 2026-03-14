import argparse 
import logging 
from bot.logging_config import setup_logging
from bot.orders import place_order
from bot.validators import validate_side,validate_order_type,validate_price

def main():
  parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
  parser.add_argument("--symbol",required=True)
  parser.add_argument("--side",required=True)
  parser.add_argument("--type",required=True)
  parser.add_argument("--quantity",required=True,type=float)
  parser.add_argument("--price",type=float)

  args = parser.parse_args()
  try:
    validate_side(args.side)
    validate_order_type(args.type)
    validate_price(args.price,args.type)
    print("Order Summary")
    print("Symbol: ",args.symbol)
    print("Side: ",args.side)
    print("Type: ", args.type)
    print("Quantity: ", args.quantity)
    print("Price: ",args.price)

    response=place_order(args.symbol, args.side, args.type, args.quantity, args.price)
    print("Full Response: ",response)
    print("Order ID: ",response.get("orderId"))
    print("Status: ",response.get("status"))
    print("Executed Quantity: ",response.get("executedQty"))
    print("Avg Price: ",response.get("avgPrice"))
  except Exception as e:
    print("Error placing order: ",str(e))

if __name__ == "__main__":
  setup_logging()
  main()
    