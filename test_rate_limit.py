# -*- coding: utf-8 -*-
"""
@desc: 频率限制测试脚本
@author: 1nchaos
@time: 2026/03/08
"""
import time
from adata.common.utils.sunrequests import get, set_rate_limit, set_global_rate_limit, RateLimiter


def test_rate_limiter():
    print("=== 测试频率限制功能 ===")
    
    limiter = RateLimiter()
    
    print("\n1. 测试默认限制（每分钟30次）")
    domain = "example.com"
    for i in range(5):
        wait_time = limiter.acquire(domain)
        if wait_time > 0:
            print(f"  请求 {i+1}: 需要等待 {wait_time:.2f} 秒")
        else:
            print(f"  请求 {i+1}: 立即执行")
    
    print("\n2. 测试自定义域名限制")
    test_domain = "test.custom.com"
    limiter.set_limit(test_domain, 3)  # 每分钟3次
    
    print(f"  设置 {test_domain} 限制为 3 次/分钟")
    for i in range(5):
        wait_time = limiter.acquire(test_domain)
        if wait_time > 0:
            print(f"  请求 {i+1}: 需要等待 {wait_time:.2f} 秒")
        else:
            print(f"  请求 {i+1}: 立即执行")
    
    print("\n3. 测试全局限制")
    limiter.set_global_limit(5)  # 全局默认每分钟5次
    
    new_domain = "new.domain.com"
    print(f"  全局限制设置为 5 次/分钟，测试新域名 {new_domain}")
    for i in range(7):
        wait_time = limiter.acquire(new_domain)
        if wait_time > 0:
            print(f"  请求 {i+1}: 需要等待 {wait_time:.2f} 秒")
        else:
            print(f"  请求 {i+1}: 立即执行")
    
    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    test_rate_limiter()
