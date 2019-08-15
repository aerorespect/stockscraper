import json
import requests
import bs4 as bs
import smtplib


def lambda_handler(event, context):
    # TODO implement

    #Create a dictionary of stock to scrape as keys and minimum buy limit as values
    stockdict = {'UNVR': 45000,
                 'TLKM': 4000}

    def checkprice(stock, buylimit):
        url = 'http://www.duniainvestasi.com/bei/summaries/' + str(stock)

        sauce = requests.get(url)
        soup = bs.BeautifulSoup(sauce.text, 'html.parser')

        stock_price = soup.find('div', attrs={'class': 'span-3 summary_value last'}).text
        price = int(stock_price.replace(',', ''))
        if price < buylimit:
            gmail_user = 'INSERT BOT MAIL' #BOT USER EMAIL
            gmail_password = 'INSERT BOT PASSWORD' #BOT EMAIL PASSWORD

            sender = 'INSERT BOT MAIL'
            receivers = ['INSERT LIST OF RECIPIENT EMAIL']

            SUBJECT = 'BELI SAHAM {}'.format(stock)
            TEXT = 'HARGA {} {}, lagi dibawah {} BELI SEKARANG!'.format(stock, price, buylimit)

            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(gmail_user, gmail_password)
            server.sendmail(sender, receivers, message)
            print('notif sent')

        else:
            print('nothing done')

    for key, value in stockdict.items():
        checkprice(key, value)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }






