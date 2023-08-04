# -*- coding: utf-8 -*-
# SECRET_KEY（flask项目密钥,不用管,也用不到）
P = "sk-sk-xx"
SECRET_KEY = "asghnjadfbtywyn"

# openAi api key
OPENAI_API_KEY = "%s" % P

# openAi 官方 api
URL = "https://api.openai.com/v1/chat/completions"

# openAi 代理 api
#URL = "https://open.aiproxy.xyz/v1/chat/completions"


#List models
LISTURL = "https://api.openai.com/v1/models"

#image url
IMAGEURL = "https://api.openai.com/v1/images/generations"