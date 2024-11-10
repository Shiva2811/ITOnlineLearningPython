#importing exchange_rates.py module in the file
import exchange_rates


# Function to convert USD to EUR
def usd_to_eur(amount):
    # Access the exchange rate from the module
    return amount * exchange_rates.USD_TO_EUR

# Function to convert USD to GBP
def usd_to_gbp(amount):
    # Access the exchange rate from the module
    return amount * exchange_rates.USD_TO_GBP

# Function to convert EUR to USD
def eur_to_usd(amount):
    # Access the exchange rate from the module
    return amount * exchange_rates.EUR_TO_USD

# Function to convert GBP to USD
def gbp_to_usd(amount):
    # Access the exchange rate from the module
    return amount * exchange_rates.GBP_TO_USD

#Demonstrating scope using variables from module and with in function
def demonstrate_scope():
    #Accessing exchange rate directly from exchange rate module
    print(f"USD to EUR rate : {exchange_rates.USD_TO_EUR}")
    print(f"USD to GBP :{exchange_rates.USD_TO_GBP}")

    #local variable wihtin function 
    local_rate= 100
    print(f"local variable within function scope : {local_rate}")

    #attemt to access module-level variable outside the finctions local scope
    print(f"Global USD to INR rate from exchange_rate : {exchange_rates.USD_TO_INR}")

#Test the functionality 

if __name__=="__main__":
    amount_in_usd = 100
    print(f"{amount_in_usd} USD to EUR: {usd_to_eur(amount_in_usd)}")
    print(f"{amount_in_usd} USD to GBP: {usd_to_gbp(amount_in_usd)}")
    print(f"{amount_in_usd} GBP to USD: {gbp_to_usd(amount_in_usd)}")
    print(f"{amount_in_usd} EUR to USD: {eur_to_usd(amount_in_usd)}")

    #Demonstrate scope
    demonstrate_scope()