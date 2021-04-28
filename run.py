import price
import auto_email
import pandas as pd

with open('./credentials/gmail.txt', 'r') as fp:
    secret = fp.readlines()
    EMAIL_ADDRESS = secret[0].rstrip('\n')
    EMAIL_PASSWORD = secret[1]
    fp.close()

# subject = "50% DROP PRICE ALERT"
# contents = "has dropped more than 50% from 52W High. Definitely panic market!"
# auto_email.sendEmail(EMAIL_ADDRESS, EMAIL_PASSWORD, subject, contents)

df = pd.read_csv('./export_df_rpi.csv')
df.set_index('Symbol', inplace=True)
print(df)

##############################################################################
## Drawdowns From 52 Weeks High + Email Alert Setup
##############################################################################

for symbol in list(df.index):
    high = price.calculate_prev_max_high(symbol,252)
    curr_price = price.get_current_price(symbol)
    df.loc[symbol,'12M_High'] = high
    df.loc[symbol,'Current_Price'] = curr_price
    df.loc[symbol,'15%_Drop'] = high * 0.85
    df.loc[symbol,'30%_Drop'] = high * 0.70
    df.loc[symbol,'50%_Drop'] = high * 0.5
    drop_15 = df.loc[symbol,'15%_Drop']
    drop_30 = df.loc[symbol,'30%_Drop']
    drop_50 = df.loc[symbol,'50%_Drop']
    if curr_price < drop_15 and curr_price > drop_30:
        subject = f"15% DROP PRICE ALERT - {symbol}"
        contents = f"{symbol} has dropped more than 15% from 52W High. It's time to consider buying some shares of it."
        auto_email.sendEmail(EMAIL_ADDRESS, EMAIL_PASSWORD, subject, contents)
    elif curr_price < drop_30 and curr_price > drop_50:
        subject = f"30% DROP PRICE ALERT - {symbol}"
        contents = f"{symbol} has dropped more than 30% from 52W High. Should I buy more?"
        auto_email.sendEmail(EMAIL_ADDRESS, EMAIL_PASSWORD, subject, contents)
    elif curr_price < drop_50:
        subject = f"50% DROP PRICE ALERT - {symbol}"
        contents = f"{symbol} has dropped more than 50% from 52W High. Definitely panic market!"
        auto_email.sendEmail(EMAIL_ADDRESS, EMAIL_PASSWORD, subject, contents)


subject = "50% DROP PRICE ALERT"
contents = "has dropped more than 50% from 52W High. Definitely panic market!"
auto_email.sendEmail(EMAIL_ADDRESS, EMAIL_PASSWORD, subject, contents)