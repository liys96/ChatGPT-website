# -*- coding: utf-8 -*-

import openai


def createImg():
    openai.api_key = "sk-xx"
    response = openai.Image.create(
    prompt="画一幅酷炫的中国古风人物画，要求五官细腻帅气",
    n=2,
    size="512x512"
    )
    image_url = response['data'][0]['url']
    print(str(image_url))

if __name__ =="__main__":
    createImg()
