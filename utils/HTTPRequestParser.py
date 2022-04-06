from datetime import datetime
import time
# import nest_asyncio
# nest_asyncio.apply()

from requests_html import AsyncHTMLSession, user_agent
session = AsyncHTMLSession()
session.headers = {"user-agent":user_agent()}

async def parse_code(url):
    print(f"http request starts: \t{url}")
    data = [url, datetime.utcnow().isoformat(timespec="seconds")]
    try:
        response = await session.get(url, timeout=20)
        if response.ok:
            data.append("success")
        print(url, response.history)
        if response.history:
            history = response.history
            data.append("|".join([str(x.status_code) for x in history]))
            data.append("|".join([x.url for x in history]))
        print(url, response.status_code, response.url)
        data.append(str(response.status_code))
        data.append(response.url)
    except Exception as e:
        print(e)
        data.append("error")
    finally:
        return data

def async_parse(urls):
    runs = (lambda url=url: parse_code(url) for url in urls)
    start = time.time()
    results = session.run( *(runs) )
    print(f"job finished in {time.time()-start:.2f}s")
    return results

if __name__ == "__main__":
    urls = [
        "http://github.com",
        "http://google.com",
        "http://python.org",
    ]
    print( async_parse(urls) )