import logging
import time
from solana.rpc.api import Client
from constant import TokenAccount
from utils import send_telegram_notice


client = Client('https://api.mainnet-beta.solana.com')

check_list = (
    (TokenAccount.CWAR, "CWAR", ""),
    (TokenAccount.BLOCK, "BLOCK", "cost: 0.078"),
    (TokenAccount.UNQ, "UNQ", ""),
    (TokenAccount.MEAN, "MEAN", ""),
    (TokenAccount.GWT, "GWT", ""),
    (TokenAccount.SLC, "SLC", "cost: 0.07"),
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
        for addr, token, remark in check_list:
            rst = client.get_token_account_balance(addr)
            balance = int(rst['result']['value']['amount'])
            balance_of_readable = rst['result']['value']['uiAmountString']
            logging.info(f"{token} balance: {balance_of_readable}")
            if balance > 0:
                msg = f"{token} balance: {balance_of_readable} [{remark}]"
                send_telegram_notice(msg)
                send_flag = True

        if send_flag:
            time.sleep(60 * 60)
        else:
            time.sleep(30)

