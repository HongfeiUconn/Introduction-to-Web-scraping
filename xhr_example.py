### author: Hongfei Li, https://www.hongfei-business.com/

import requests
import json

## Suppose we want to scrape the information of all presentations from Hongfei's personal website

## Go to: https://www.hongfei-business.com/talk/, then right click-->Inspect-->Network-->Choose XHR, refresh webpage,
## Then we can see the request URL is "Request URL: https://www.hongfei-business.com/index.json"

url = "https://www.hongfei-business.com/index.json"

### Use requests to get html source codes
content_html = requests.get(url, timeout=50).text
## The output is json, which is a type of text written with Javascript object notation
print(type(content_html))

### Convert from json to lists
content_list = json.loads(content_html)
print(type(content_list))

## Print all the element in the list
for ele in content_list:
    print(ele)
    ## The output type is dictionary, which is very easy to deal with, for example, if we want the inforamtion of authors, we can write: print(ele['authors'])
    print(type(ele))