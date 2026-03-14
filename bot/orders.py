import logging
from .client import get_client

client = get_client()

def place_order(symbol,side,order_type,quantity,price=None):
  try:
    logging.info(f"Order Request: {symbol} {side} {order_type} {quantity} {price}")
    if order_type =="MARKET":
      response = client.futures_create_order(symbol=symbol,side=side,type="MARKET",quantity=quantity)
    elif order_type =="LIMIT":
      response = client.futures_create_order(symbol=symbol,side=side,type="LIMIT",quantity=quantity,price=price,timeInForce="GTC")
    else:
      raise ValueError("Invalid order type")
    logging.info(f"Order Response: {response}")
    return response
  except Exception as e:
    logging.error(f"Order Error: {str(e)}")
    raise
