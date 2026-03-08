# -*- coding: utf-8 -*-
"""
@desc: 请求封装模块，带频率限制功能
@author: 1nchaos
@time: 2023/3/29
@log: change log
"""
import time
import threading
from urllib.parse import urlparse
from collections import defaultdict, deque
import requests


class RateLimiter:
    """
    频率限制器，基于域名控制请求频率
    默认每分钟30次请求，可通过方法设置
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._default_limit = 30  # 默认每分钟30次
        self._domain_limits = {}  # 域名特定的限制
        self._request_history = defaultdict(deque)  # 每个域名的请求历史
        self._history_lock = threading.Lock()
    
    def set_default_limit(self, limit: int):
        """
        设置默认的频率限制（每分钟请求次数）
        :param limit: 每分钟请求次数
        """
        self._default_limit = limit
    
    def set_domain_limit(self, domain: str, limit: int):
        """
        为特定域名设置频率限制
        :param domain: 域名，如 "quote.eastmoney.com"
        :param limit: 每分钟请求次数
        """
        self._domain_limits[domain] = limit
    
    def get_limit(self, domain: str) -> int:
        """
        获取指定域名的频率限制
        :param domain: 域名
        :return: 每分钟请求次数
        """
        return self._domain_limits.get(domain, self._default_limit)
    
    def _get_domain(self, url: str) -> str:
        """从URL中提取域名"""
        parsed = urlparse(url)
        return parsed.netloc
    
    def wait_if_needed(self, url: str):
        """
        检查是否需要等待，如果需要则等待
        :param url: 请求的URL
        """
        domain = self._get_domain(url)
        limit = self.get_limit(domain)
        
        with self._history_lock:
            now = time.time()
            history = self._request_history[domain]
            
            # 清理60秒前的请求记录
            while history and history[0] < now - 60:
                history.popleft()
            
            # 如果已达到限制，等待直到可以发送请求
            if len(history) >= limit:
                sleep_time = history[0] + 60 - now
                if sleep_time > 0:
                    time.sleep(sleep_time)
                    # 重新清理并检查
                    now = time.time()
                    while history and history[0] < now - 60:
                        history.popleft()
            
            # 记录当前请求时间
            history.append(time.time())


class SunProxy:
    """代理配置类"""
    
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
    def get_proxies(cls):
        if cls._config.get('is_proxy') and cls._config.get('ip'):
            return {
                'http': f"http://{cls._config['ip']}",
                'https': f"http://{cls._config['ip']}"
            }
        return None


# 全局频率限制器实例
rate_limiter = RateLimiter()


def set_rate_limit(limit: int):
    """
    设置默认的请求频率限制（每分钟请求次数）
    :param limit: 每分钟请求次数，默认30次
    
    示例:
        import adata
        adata.set_rate_limit(60)  # 设置为每分钟60次
    """
    rate_limiter.set_default_limit(limit)


def set_domain_rate_limit(domain: str, limit: int):
    """
    为特定域名设置请求频率限制
    :param domain: 域名，如 "quote.eastmoney.com"
    :param limit: 每分钟请求次数
    
    示例:
        import adata
        adata.set_domain_rate_limit("quote.eastmoney.com", 60)
    """
    rate_limiter.set_domain_limit(domain, limit)


def get(url, **kwargs):
    """
    发送GET请求，带频率限制
    :param url: 请求URL
    :param kwargs: 其他requests参数
    :return: Response对象
    """
    rate_limiter.wait_if_needed(url)
    
    # 设置默认timeout
    if 'timeout' not in kwargs:
        kwargs['timeout'] = 15
    
    # 设置代理
    proxies = SunProxy.get_proxies()
    if proxies and 'proxies' not in kwargs:
        kwargs['proxies'] = proxies
    
    return requests.get(url, **kwargs)


def post(url, **kwargs):
    """
    发送POST请求，带频率限制
    :param url: 请求URL
    :param kwargs: 其他requests参数
    :return: Response对象
    """
    rate_limiter.wait_if_needed(url)
    
    # 设置默认timeout
    if 'timeout' not in kwargs:
        kwargs['timeout'] = 15
    
    # 设置代理
    proxies = SunProxy.get_proxies()
    if proxies and 'proxies' not in kwargs:
        kwargs['proxies'] = proxies
    
    return requests.post(url, **kwargs)


def request(method, url, **kwargs):
    """
    发送HTTP请求，带频率限制
    :param method: 请求方法
    :param url: 请求URL
    :param kwargs: 其他requests参数
    :return: Response对象
    """
    rate_limiter.wait_if_needed(url)
    
    # 设置默认timeout
    if 'timeout' not in kwargs:
        kwargs['timeout'] = 15
    
    # 设置代理
    proxies = SunProxy.get_proxies()
    if proxies and 'proxies' not in kwargs:
        kwargs['proxies'] = proxies
    
    return requests.request(method, url, **kwargs)
