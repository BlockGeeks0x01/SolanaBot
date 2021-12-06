import json
import logging
import requests
import base58

from solana.keypair import Keypair

from constant import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def load_abi(file_name):
    with open(f"./abi/{file_name}", "r") as f:
        return json.load(f)


def send_telegram_notice(msg):
    if not TELEGRAM_TOKEN:
        raise Exception("telegram token is null!")
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={msg}")
    logging.info("发送电报机器人提醒")


def private_key2key_pair(private_key: str) -> Keypair:
    private_key_of_bytes = base58.b58decode(private_key)
    return Keypair.from_secret_key(private_key_of_bytes)
