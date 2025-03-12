"网页查询URL模板列表（直接替换`{keyword}`）"

SEARCH_TEMPLATES = [
    # 通用搜索
    "https://www.baidu.com/s?wd={keyword}",
    "https://www.google.com/search?q={keyword}",
    "https://search.yahoo.com/search?p={keyword}",  # 雅虎搜索
    
    # 百科类
    "https://baike.baidu.com/search/none?word={keyword}",          # 百度百科
    "https://zh.wikipedia.org/w/index.php?search={keyword}",       # 维基百科（中文）
    "https://en.wikipedia.org/w/index.php?search={keyword}",       # 维基百科（英文）
    "https://www.britannica.com/search?query={keyword}",  # 大英百科全书
    
    # 新闻门户
    "http://search.sina.com.cn/?q={keyword}&c=news",               # 新浪新闻
    "https://news.sogou.com/news?query={keyword}",                 # 搜狗新闻（覆盖腾讯等）
    "https://www.so.com/s?q={keyword}&tn=news",                    # 360新闻
    "https://news.163.com/search.html?query={keyword}",            # 网易新闻
    "https://voice.baidu.com/act/newsearch/search?keyword={keyword}",  # 百度热点新闻
    "https://www.leiphone.com/search?s={keyword}&site=article",  # 雷锋网
    "https://www.36kr.com/search/articles/{keyword}",  # 36氪
    "https://www.sohu.com/search/?keyword={keyword}",  # 搜狐
    "https://www.ifeng.com/search.html?searchword={keyword}",  # 凤凰网
    
    # 财经媒体
    "http://so.eastmoney.com/web/s?keyword={keyword}",             # 东方财富网
    "https://www.wsj.com/search?query={keyword}",                  # 华尔街日报
    "http://search.hexun.com/?q={keyword}",                        # 和讯网
    "https://www.cls.cn/search?keyword={keyword}",                 # 财联社
    "https://news.ycombinator.com/from?site={keyword}",  # Hacker News
    "https://www.economist.com/search?q={keyword}",  # 经济学人
    "https://www.ft.com/search?q={keyword}",  # 金融时报
    "https://www.10jqka.com.cn/search?q={keyword}",  # 同花顺
    "https://www.askci.com/search?q={keyword}"  # 中商情报网
    
    # 外国新闻

    "https://www.forbes.com/search/?q={keyword}",  # Forbes
    "https://www.huffpost.com/search?keywords={keyword}",  # Huffington Post
    "https://www.reuters.com/site-search/?query={keyword}",  # 路透社
    "https://www.bloomberg.com/search?query={keyword}",  # 彭博社
    "https://www.cnbc.com/search/?query={keyword}",  # CNBC
    
    "https://www.infoq.cn/search/?q={keyword}",  # InfoQ
    "https://www.producthunt.com/search?term={keyword}",  # Product Hunt
    "https://stackshare.io/search?q={keyword}",  # StackShare
    "https://www.crunchbase.com/search/{keyword}/field/organization",  # Crunchbase
    "https://www.gartner.com/en/search?q={keyword}",  # Gartner
    "https://www.idc.com/search?query={keyword}",  # IDC
    "https://www.techinasia.com/search?query={keyword}",  # Tech in Asia
    "https://www.startupnation.com/search-results/?s={keyword}",  # StartupNation
    "https://www.businessinsider.com/search?q={keyword}",  # Business Insider
    "https://www.entrepreneur.com/search?q={keyword}",  # Entrepreneur
    "https://www.fastcompany.com/search?q={keyword}",  # Fast Company
    "https://www.inc.com/search.html?q={keyword}",  # Inc.
    "https://www.vox.com/search?q={keyword}",  # Vox
    
    # 技术媒体
    "https://techcrunch.com/search/{keyword}",  # TechCrunch
    "https://www.jiqizhixin.com/search?query={keyword}",  # 机器之心
    
    # 社交媒体
    "https://www.zhihu.com/search?q={keyword}",                    # 知乎
    "https://tieba.baidu.com/f/search/res?ie=utf-8&kw={keyword}",  # 百度贴吧
    "https://s.weibo.com/weibo/{keyword}",                         # 微博热搜
    
    # 其他
    "http://www.people.com.cn/GB/59476/59449/index.html?q={keyword}",  # 人民网
    "https://www.thepaper.cn/searchResult.jsp?inp={keyword}",      # 澎湃新闻
    
    
    # 技术
    "https://www.eet-china.com/e/sch/index.php?field=1&keyboard={keyword}",  # 电子工程专辑
    "https://www.esmchina.com/search?q={keyword}",  # 国际电子商情
    "https://en.wikichip.org/w/index.php?search={keyword}&title=Special:Search",  # 芯片维基
    "https://www.company-histories.com/search?q={keyword}",  # 公司历史
    "https://www.ednchina.com/e/sch/index.php?field=1&keyboard={keyword}",  # 电子技术设计
    "https://www.digitimes.com/search?q={keyword}",  # Digitimes
    "https://search.21ic.com/so.php?keyword={keyword}&sort=",  # 21电子网
]

