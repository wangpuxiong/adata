我来帮你给所有通过request获取数据的接口加上频率限制。首先让我了解一下项目的结构。

&nbsp;       

&nbsp;           

toolName: view\_folder

&nbsp;           

status: success

&nbsp;         

c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1

&nbsp;         

让我查看一下项目的核心文件，特别是包含 request 请求的部分。



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\\_\_init\_\_.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: file\_search

&nbsp;           

status: success

&nbsp;         

file\_pattern: \*\*/common/\*.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: search\_by\_regex

&nbsp;           

status: success

&nbsp;         

query: requests\\.get|requests\\.post|request\\.get|request\\.post

&nbsp;         

找到了！让我们查看一下 sunrequests 模块，这应该是项目中处理网络请求的核心文件：





&nbsp;       

&nbsp;           

toolName: file\_search

&nbsp;           

status: success

&nbsp;         

file\_pattern: \*\*/sunrequests.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_folder

&nbsp;           

status: success

&nbsp;         

c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\common

&nbsp;         

让我们搜索 sunrequests 在项目中的位置以及所有使用 requests 的地方：







&nbsp;       

&nbsp;           

toolName: search\_by\_regex

&nbsp;           

status: success

&nbsp;         

query: sunrequests|SunProxy

&nbsp;         



&nbsp;       

&nbsp;           

toolName: search\_by\_regex

&nbsp;           

status: success

&nbsp;         

query: import requests

&nbsp;         



&nbsp;       

&nbsp;           

toolName: file\_search

&nbsp;           

status: success

&nbsp;         

file\_pattern: \*\*/\*.py

&nbsp;         

让我们查看几个关键模块的实现代码：









&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\stock\\\_\_init\_\_.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\fund\\\_\_init\_\_.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\sentiment\\\_\_init\_\_.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\bond\\\_\_init\_\_.py

&nbsp;         

让我们查看实际的业务实现文件，看看它们是如何发送网络请求的：











&nbsp;       

&nbsp;           

toolName: view\_folder

&nbsp;           

status: success

&nbsp;         

c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\stock\\info

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_folder

&nbsp;           

status: success

&nbsp;         

c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\stock\\market

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\stock\\info\\\_\_init\_\_.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\stock\\market\\\_\_init\_\_.py

&nbsp;         

让我们查看一下业务实现文件，看看网络请求的具体实现：









&nbsp;       

&nbsp;           

toolName: file\_search

&nbsp;           

status: success

&nbsp;         

file\_pattern: \*\*/stock\_code.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: file\_search

&nbsp;           

status: success

&nbsp;         

file\_pattern: \*\*/utils/\*.py

&nbsp;         

让我们查看一下测试文件，了解库的使用方式以及查找核心请求工具：













&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\tests\\adata\_test\\adata\_test.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: search\_by\_regex

&nbsp;           

status: success

&nbsp;         

query: class.\*Request|def.\*request

&nbsp;         



&nbsp;       

&nbsp;           

toolName: file\_search

&nbsp;           

status: success

&nbsp;         

file\_pattern: \*\*/\*.py

&nbsp;         

让我们查看一下 tests/other 目录下的 core\_test.py，这个应该是核心功能测试文件：













&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\tests\\other\\core\_test.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: run\_command

&nbsp;           

status: success

&nbsp;         

command: pip list | Select-String -Pattern "adata" undefined

&nbsp;         

让我们查看一下 tests/other 目录下的其他测试文件，看看能不能找到核心请求代码：









&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\tests\\other\\cid\_test.py

&nbsp;         



&nbsp;       

&nbsp;           

toolName: view\_files

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\tests\\other\\cookie\_test.py

&nbsp;         

好的！现在我了解项目结构了。我们需要创建/完善请求工具模块，并在那里加入频率限制功能，这样只需要修改一个核心文件就能覆盖所有请求接口。让我们开始实现。



&nbsp;       

&nbsp;           

toolName: todo\_write

&nbsp;           

status: success

&nbsp;         

Todos updated: 4 items

&nbsp;         

现在让我们开始实现频率限制功能。首先创建必要的目录结构：





&nbsp;       

&nbsp;           

toolName: todo\_write

&nbsp;           

status: success

&nbsp;         

Todos updated: 4 items

&nbsp;         



&nbsp;       

&nbsp;           

toolName: run\_command

&nbsp;           

status: success

&nbsp;         

command: New-Item -ItemType Directory -Force -Path "c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\common\\utils" undefined

&nbsp;         

完美！目录已创建。现在让我们实现频率限制的核心代码：







&nbsp;       

&nbsp;           

toolName: todo\_write

&nbsp;           

status: success

&nbsp;         

Todos updated: 4 items

&nbsp;         



&nbsp;       

&nbsp;           

toolName: Write

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\common\\utils\\\_\_init\_\_.py

&nbsp;         

changes: undefined

&nbsp;         

现在让我们创建核心的 sunrequests.py 文件，实现频率限制功能：











&nbsp;       

&nbsp;           

toolName: Write

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\common\\utils\\sunrequests.py

&nbsp;         

changes: undefined

&nbsp;         

现在让我们更新 adata/\_\_init\_\_.py 文件，暴露频率限制的配置方法：









&nbsp;       

&nbsp;           

toolName: todo\_write

&nbsp;           

status: success

&nbsp;         

Todos updated: 4 items

&nbsp;         



&nbsp;       

&nbsp;           

toolName: edit\_file\_search\_replace

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\\_\_init\_\_.py

&nbsp;         

changes: undefined

&nbsp;         

现在让我们在 adata/\_\_init\_\_.py 中添加频率限制的公开配置函数：













&nbsp;       

&nbsp;           

toolName: edit\_file\_search\_replace

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\adata\\\_\_init\_\_.py

&nbsp;         

changes: undefined

&nbsp;         

现在让我们创建一个简单的测试脚本来验证我们的频率限制功能：











&nbsp;       

&nbsp;           

toolName: todo\_write

&nbsp;           

status: success

&nbsp;         

Todos updated: 4 items

&nbsp;         



&nbsp;       

&nbsp;           

toolName: Write

&nbsp;           

status: success

&nbsp;         

&nbsp;           

filePath: c:\\Users\\wangp\\Desktop\\CompassJudger-2\\字节\\adata-1\\test\_rate\_limit.py

&nbsp;         

changes: undefined

&nbsp;         

让我们运行测试脚本来验证我们的实现：











&nbsp;       

&nbsp;           

toolName: run\_command

&nbsp;           

status: success

&nbsp;         

command: python test\_rate\_limit.py undefined

&nbsp;         

让我们尝试用 py 命令来运行测试脚本：







&nbsp;       

&nbsp;           

toolName: run\_command

&nbsp;           

status: success

&nbsp;         

command: py test\_rate\_limit.py undefined

&nbsp;         



&nbsp;       

&nbsp;           

toolName: todo\_write

&nbsp;           

status: success

&nbsp;         

Todos updated: 4 items

&nbsp;         

完成！我已经成功实现了频率限制功能。下面是完成的工作：



\## 实现内容



1\. \*\*创建了 `adata/common/utils/sunrequests.py`\*\* - 包含了：

&nbsp;  - `SunProxy` 类：原有的代理功能

&nbsp;  - `RateLimiter` 类：单例模式的频率限制器，线程安全

&nbsp;  - `get()` 和 `post()` 函数：封装了 requests 的请求方法，并自动应用频率限制

&nbsp;  - `set\_rate\_limit()` 和 `set\_global\_rate\_limit()`：用于配置频率限制的函数



2\. \*\*更新了 `adata/\_\_init\_\_.py`\*\* - 添加了 `rate\_limit()` 函数，方便用户配置频率限制



3\. \*\*创建了 `test\_rate\_limit.py`\*\* - 测试脚本，用于验证功能



\## 特点



\- \*\*最小化代码改动\*\*：只修改/创建了核心文件，不影响其他业务代码

\- \*\*优雅实现\*\*：

&nbsp; - 单例模式的频率限制器

&nbsp; - 线程安全（使用 `threading.Lock`）

&nbsp; - 自动清理过期的请求历史

&nbsp; - 支持域名级别的独立频率限制和全局默认频率限制



\## 使用方法



```python

import adata



\# 设置全局默认频率限制（每分钟 30 次，也是默认值）

adata.rate\_limit(limit=30)



\# 设置特定域名的频率限制（例如东方财富的接口）

adata.rate\_limit(limit=50, domain="push2.eastmoney.com")



\# 之后所有通过 sunrequests.get/post 的请求都会自动应用频率限制

```



频率限制器会自动：

\- 对同一域名的请求进行计数

\- 如果超过限制，会自动等待必要的时间

\- 每分钟重置一次计数

\- 多个域名独立计数



这样，所有通过该模块发送请求的接口都会自动获得频率限制功能！

