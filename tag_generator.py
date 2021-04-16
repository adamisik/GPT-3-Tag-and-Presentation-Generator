import os
import openai
import json


text = "Hello, today I want to show you how you can configure a template button the notion. So first I created an empty page, give it a title of test page. Then we want to search for the templates button. If we have it and selected now we can configure our own template button. First we will give it a name, we'll name it add a new to do block. And then every block we want to have a header and the to do list. So we're This is the block that actually appears when we are pressing a button. So first we want header. We'll select all section header, name it's pool, block number, and then we could select the number and then we will add a to do list. Then we click on Close. So now every time we click on this add new to do block the new heading the new to do list will appear. This is how template buttons work. If we want to we configured which is press the settings and then we could add this we could probably list it for clothes. Every time we press on the button. This new block with the toggle editor that will appeal to very much."
API_key  = 

def description_gen(text,API_key,task):

  openai.api_key = API_key

  if task=="description":
    prompt = text+"\n\ntl;dr:"
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      temperature=0.5,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

  else:
    prompt = text+"\n\nKeywords: "
    response = openai.Completion.create(
    engine="davinci",
    prompt = prompt,
    temperature=0.3,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.8,
    presence_penalty=0.0,
    stop=["\n"])

  return response



tags = description_gen(text,API_key, task="tag")['choices'][0]['text']
print("Generated tags:", tags)

description = description_gen(text,API_key, task="description")['choices'][0]['text']
print("Generated description:", description)

generated_answers = {"Tags of text": tags,"Description of text": description}

with open('answer.txt', 'w') as file:
     file.write(json.dumps(generated_answers)) # use `json.loads` to do the reverse