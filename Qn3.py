def combinationofcoins(coins):


        if(coins>=25):

            return str(coins//25)+" quarters "+combinationofcoins(coins-((coins//25)*25))

        elif(coins>=10):

            return str(coins//10)+" dimes "+combinationofcoins(coins-((coins//10)*10))

        elif(coins>=5):

            return str(coins//5)+" nickels "+combinationofcoins(coins-((coins//5)*5))

        elif (coins>0):

            return str(coins)+" Pennies"

        else:

            return ""

coins=int(input("Enter an integer: "))


print ("Coins = ", combinationofcoins(coins))
