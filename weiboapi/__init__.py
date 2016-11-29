"""
@Author: Rossi
2016-02-01
"""

__all__ = [
    "login", "get_account", "post", "comment",
    "get_weibos", "get_comments", "repost",
    "get_weibo", "get_domain", "get_relation",
    "get_user_info", "Account", "Comment", "Weibo",
    "search_user", "search_weibo", "send_message",
    "follow", "get_homepage_topic", "get_homepage",
    "reply_comment", "like", "get_inbox_comment",
    "get_own_account", "get_inbox_count", "get_hot_weibos",
    "has_login"
]

from weiboapi.api.api import login, get_account, post
from weiboapi.api.api import comment, get_weibos
from weiboapi.api.api import get_comments, repost
from weiboapi.api.api import get_weibo, get_domain
from weiboapi.api.api import get_relation, get_user_info
from weiboapi.api.api import search_user, search_weibo
from weiboapi.api.api import send_message, follow
from weiboapi.api.api import get_homepage, reply_comment
from weiboapi.api.api import get_inbox_comment, like
from weiboapi.api.api import get_homepage_topic, get_own_account
from weiboapi.api.api import get_inbox_count, get_hot_weibos
from weiboapi.api.api import has_login
from weiboapi.api.account import Account
from weiboapi.api.comment import Comment
from weiboapi.api.weibo import Weibo
