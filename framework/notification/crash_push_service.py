import requests
import framework.logger

log = framework.logger.getLogger(__name__)


def push(title, message, push_service_token):
    # server推送
    server_push_url = "https://sc.ftqq.com/" + push_service_token + ".send"
    str = push_service_token[0:3]
    if "SCT" == str:
        server_push_url = "https://sctapi.ftqq.com/" + push_service_token + ".send"
    params = {
        "text": title,
        "desp": message,
    }
    res = requests.post(url=server_push_url, params=params)
    if res.status_code == 200:
        log.info("推送成功!")
    else:
        log.info("推送失败!")
    log.info("标题->", title)
    log.info("内容->\n", message)
