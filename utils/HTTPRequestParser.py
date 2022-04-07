from datetime import datetime
from time import perf_counter
# import nest_asyncio
# nest_asyncio.apply()

from requests_html import AsyncHTMLSession, user_agent
session = AsyncHTMLSession()
# session.headers = {"user-agent":user_agent()}

async def parse_code(url):
    if url.startswith("https://"):
        url = url.replace("https://", "http://")
    if not url.startswith("http://"):
        url = "http://" + url
    # print(f"http request starts: \t{url}")
    data = [url, datetime.utcnow().isoformat(timespec="seconds")]
    try:
        response = await session.get(
            url, 
            timeout=10, 
            headers={"user-agent":user_agent()}
        )
        if response.ok:
            data.append("request success")
        else:
            data.append("request error")
        print("="*10, url, response.history)
        print("="*10, url, response.status_code, response.url)
        redirected_codes = [str(x.status_code) for x in response.history]
        redirected_urls = [x.url for x in response.history]
        data.append("|".join(redirected_codes))
        data.append("|".join(redirected_urls))
        data.append(str(response.status_code))
        data.append(response.url)
    except Exception as e:
        print("=="*10, url, "failed to connect")
        print(e)
        data.append("request failed")
    finally:
        return data

def async_parse(urls):
    runs = (lambda url=url: parse_code(url) for url in urls)
    start = perf_counter()
    results = session.run( *(runs) )
    print(f"batch job finished in {perf_counter()-start:.2f}s.\n")
    return results

if __name__ == "__main__":
    urls = [
        "http://github.com",
        "http://google.com",
        "http://python.org",
    ]
    print( async_parse(urls) )