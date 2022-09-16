bitcoin_price = input("What is Bitcoin price today?\n")
money_amount = input("How much $ do you have?\n")
bitcoin_amount = int(money_amount) / int(bitcoin_price)
print("You can buy {0:.7f} BTC".format(bitcoin_amount))