import os
import openai
import json


text = "Hello, everyone. Welcome to this introduction of Jeff Bezos. Jeff beezus is an American intrapreneur and industrialist. He is the founder and CEO of the multinational technology company. Amazon is the richest world man in the world. He was born in Albuquerque and raised in Houston major Miami, and graduated from Princeton University. He holds a degree in electrical engineering and computer science. His first job included a wall street job in a variety of fields from 1996 to 1994. He founded Amazon in 1994. On a cross country road trip from New York to Seattle company began as a bookstore and has since expanded to a wide variety of other ecommerce products and services. Amazon's currently the world's largest online sales company, the largest internet company revenue and reports largest provider of virtual assistants and cloud infrastructure services."
API_key  = "sk-KngzsmcU00JLEPrtIA7pkQlmkqeGaDWQfaumCHUG"

def description_gen(text,API_key,task,max_tokens):
  """
  Creates a dict with tags based on a video script using the GPT-3 model of OpenAI.
  
  Args:
    text:
      String containing the video script.
    API_key:
      Secret API Key. 
    taks:
      Task to be solved. Arguments: tag (generates script tags), description (generates short description of script)
    max_tokens:
      The maximum number of tokens to be generated. 
  
  Returns:
    response: 
      String containing the list of instructions generated by GPT-3.
  """
  openai.api_key = API_key

  if task=="summary":
    prompt = "\n"\
    "Text to make summary from:\n"\
    "\n"\
    "Hello, today I want to show you how you can configure a template button the notion. So first I created an empty page, give it a title of test page. Then we want to search for the templates button. If we have it and selected now we can configure our own template button. First we will give it a name, we'll name it add a new to do block. And then every block we want to have a header and the to do list. So we're This is the block that actually appears when we are pressing a button. So first we want header. We'll select all section header, name it's pool, block number, and then we could select the number and then we will add a to do list. Then we click on Close. So now every time we click on this add new to do block the new heading the new to do list will appear. This is how template buttons work. If we want to we configured which is press the settings and then we could add this we could probably list it for clothes. Every time we press on the button. This new block with the toggle editor that will appeal to very much.\n"\
    "\n"\
    "\n"\
    "Summary:\n"\
    "This tutorial video shows you how to configure a template button on notion. It includes a step-by-step walkthrough for the button configuration.\n"\
    "\n"\
    "Text to make summary from:\n"\
    "\n"\
    "Hello everyone, today I want to talk to you about the charter of open AI. So one important aspect are broadly distributed benefits. So we want artificial intelligence for the benefit of all. While not enabling users of AI that may harm humanity. We also want to minimize conflicts of interests among stakeholders that could compromise our goal. Apart from that, we want long term safety. So we want you to research required to make artificial intelligence safe. And if a value aligned project reaches the goal First, we are planning on teaming up with them in order to avoid the rights. In order to achieve that, we also need technical leadership. So openly I must be on the cutting edge of AI capabilities, and also lead with the pre products. Those should, in turn be used according to our chart. Lastly, we have a cooperative orientation. So we want to actively cooperate with other research and policy institutions to create a global community working together to address API's global challenges, and provide public goods like source code.\n"\
    "\n"\
    "\n"\
    "Summary:\n"\
    "This tutorial video talks about the charter of Open AI. The core concepts behind this framework will be elaborated.\n"\
    "\n"\
    "Text to make summary of:\n"\
    "\n" + text + "\n"\
    "\n"\
    "\nSummary:\n"
    "\n"
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      temperature=0.6,
      max_tokens=max_tokens,
      top_p=0.0,
      frequency_penalty=0.0,
      presence_penalty=0.0)

  elif task=="tag":
    prompt = "###\n"\
    "Text to extract tags from:\n"\
    "\n"\
    "Hello, today I want to show you how you can configure a template button the notion. So first I created an empty page, give it a title of test page. Then we want to search for the templates button. If we have it and selected now we can configure our own template button. First we will give it a name, we'll name it add a new to do block. And then every block we want to have a header and the to do list. So we're This is the block that actually appears when we are pressing a button. So first we want header. We'll select all section header, name it's pool, block number, and then we could select the number and then we will add a to do list. Then we click on Close. So now every time we click on this add new to do block the new heading the new to do list will appear. This is how template buttons work. If we want to we configured which is press the settings and then we could add this we could probably list it for clothes. Every time we press on the button. This new block with the toggle editor that will appeal to very much.\n"\
    "\n"\
    "\n"\
    "Tags:\n"\
    "template button,configuration,notion\n"\
    "\n"\
    "Text to extract tags from:\n"\
     "\n" + text + "\n"\
    "\n"\
    "Tags:\n"\

    response = openai.Completion.create(
    engine="davinci",
    prompt = prompt,
    temperature=0.7,
    max_tokens=max_tokens,
    top_p=0.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)

  elif task =="title":
    prompt="###\n"\
    "Text to make title for:\n"\
    "\n"\
    "Hello, today I want to show you how you can configure a template button the notion. So first I created an empty page, give it a title of test page. Then we want to search for the templates button. If we have it and selected now we can configure our own template button. First we will give it a name, we'll name it add a new to do block. And then every block we want to have a header and the to do list. So we're This is the block that actually appears when we are pressing a button. So first we want header. We'll select all section header, name it's pool, block number, and then we could select the number and then we will add a to do list. Then we click on Close. So now every time we click on this add new to do block the new heading the new to do list will appear. This is how template buttons work. If we want to we configured which is press the settings and then we could add this we could probably list it for clothes. Every time we press on the button. This new block with the toggle editor that will appeal to very much.\n"\
    "\n"\
    "\n"\
    "Title:\n"\
    "Template button configuration on notion\n"\
    "\n"\
    "Text to make title for:\n"\
     "\n" + text + "\n"\
    "\n"\
    "Title:\n"\
    "\n"
    response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt=prompt,
    temperature=0.6,
    max_tokens=max_tokens,
    top_p=0.5,
    frequency_penalty=1.0,
    presence_penalty=0.0,
    )

  return response

tags = description_gen(text,API_key, task="tag", max_tokens=7)['choices'][0]['text']
tags  = tags.split("Text to make summary")[0]
print("Generated tags:", tags)

summary = description_gen(text,API_key, task="summary", max_tokens=50)['choices'][0]['text']
summary = summary.split("Text to make summary")[0]
print("Generated short script summary:", summary)

title = description_gen(text,API_key, task="title", max_tokens=5)['choices'][0]['text']
title = title.split("Text to make summary")[0]
print("Generated title:", title)

generated_answers = {"Tags for text": tags,"Summary for text": summary,"Title for text": title}

with open('answer.txt', 'w') as file:
    file.write(json.dumps(generated_answers)) # use `json.loads` to do the reverse