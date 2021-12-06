import logging
import time
from solana.rpc.api import Client
from constant import TokenAccount
from utils import send_telegram_notice


client = Client('https://api.mainnet-beta.solana.com')

check_list = (
    (TokenAccount.CWAR, "CWAR"),
)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d (%(levelname)s): %(message)s",
        datefmt="%y-%m-%d %H:%M:%S"
    )
    logging.getLogger().setLevel(logging.INFO)
    logging.info(f"solana: {client.is_connected()}")

    while True:
        send_flag = False
        for addr, token in check_list:
            rst = client.get_token_account_balance(addr)
            balance = int(rst['result']['value']['amount'])
            if balance > 0:
                msg = f"{token} balance: {rst['result']['value']['uiAmountString']}"
                send_telegram_notice(msg)
                send_flag = True

        if send_flag:
            time.sleep(60 * 60)
        else:
            time.sleep(30)

