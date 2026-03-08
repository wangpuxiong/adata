# -*- coding: utf-8 -*-
"""
@desc: 请求工具类，支持代理和频率限制
@author: 1nchaos
@time: 2023/4/4
@log: change log
"""
import time
import threading
from collections import defaultdict
from urllib.parse import urlparse
import requests


class SunProxy:
    _config = {
        'is_proxy': False,
        'ip': None,
        'proxy_url': None
    }

    @classmethod
    def set(cls, key, value):
        cls._config[key] = value

    @classmethod
    def get(cls, key):
        return cls._config.get(key)

    @classmethod
    def get_proxy(cls):
        if not cls._config['is_proxy']:
            return None
        if cls._config['ip']:
            return {
                'http': f'http://{cls._config["ip"]}',
                'https': f'http://{cls._config["ip"]}'
            }
        if cls._config['proxy_url']:
            try:
                r = requests.get(cls._config['proxy_url'], timeout=5)
                ip = r.text.strip()
                return {
                    'http': f'http://{ip}',
                    'https': f'http://{ip}'
                }
            except Exception:
                pass
        return None


class RateLimiter:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._domain_limits = defaultdict(lambda: 30)
            self._request_history = defaultdict(list)
            self._lock = threading.Lock()
            self._initialized = True

    def set_limit(self, domain, limit):
        with self._lock:
            self._domain_limits[domain] = limit

    def set_global_limit(self, limit):
        with self._lock:
            self._domain_limits.default_factory = lambda: limit

    def _clean_old_requests(self, domain, now):
        minute_ago = now - 60
        self._request_history[domain] = [
            t for t in self._request_history[domain]
            if t > minute_ago
        ]

    def acquire(self, domain):
        now = time.time()
        with self._lock:
            self._clean_old_requests(domain, now)
            limit = self._domain_limits[domain]
            if len(self._request_history[domain]) >= limit:
                wait_time = self._request_history[domain][0] + 60 - now
                if wait_time > 0:
                    return wait_time
            self._request_history[domain].append(now)
            return 0

    def wait_and_acquire(self, domain):
        while True:
            wait_time = self.acquire(domain)
            if wait_time <= 0:
                return
            time.sleep(wait_time)


_rate_limiter = RateLimiter()


def set_rate_limit(domain, limit):
    _rate_limiter.set_limit(domain, limit)


def set_global_rate_limit(limit):
    _rate_limiter.set_global_limit(limit)


def get_domain(url):
    parsed = urlparse(url)
    return parsed.netloc


def get(url, **kwargs):
    domain = get_domain(url)
    _rate_limiter.wait_and_acquire(domain)
    proxy = SunProxy.get_proxy()
    if proxy:
        kwargs['proxies'] = proxy
    return requests.get(url, **kwargs)


def post(url, **kwargs):
    domain = get_domain(url)
    _rate_limiter.wait_and_acquire(domain)
    proxy = SunProxy.get_proxy()
    if proxy:
        kwargs['proxies'] = proxy
    return requests.post(url, **kwargs)
