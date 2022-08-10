from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.Completion() # added upon github jman4190

start_sequence = "\nHuman:"
restart_sequence = "\n\nAI: "

start_chat_log = '''Human: Hello, can I ask something about HPV?
AI: I will provide information about HPV vaccine.
'''

#medical_disclaim = '''Please always consult your healthcare provider for medical decision.'''

session_promt = "I am a highly intelligent question answering bot. Please ask me HPV related questions. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\nHuman: Is HPV vaccine safe?\n\nAI: Yes, it is safe for most people. Please consult your doctor to determine if the vaccine is beneficial to you or your family. \nHuman: What does HPV vaccine do?\n\nAI: It protects your child from certain cancers later in life with HPV vaccine at age 11–12 years.\nHuman: When should my child get HPV vaccine?\n\nAI: Children ages 11–12 years should get two doses of HPV vaccine, given 6 to 12 months apart.\nHuman: When is the earliest age my child can get HPV vaccine?\n\nAI: HPV vaccines can be given starting at age 9 years.\nHuman: What if we want to wait till the child is older to get the HPV vaccine?\n\nAI: Please check with your doctor to determine if this is beneficial to your child. Children who start the HPV vaccine series on or after their 15th birthday need three doses, given over 6 months. Everyone through age 26 years should get HPV vaccine if they were not fully vaccinated already.\nHuman: Why should my child get HPV vaccine early?\n\nAI: Early protection works best. That’s why HPV vaccine is recommended earlier rather than later. It protects your child long before they ever have contact with the virus.\nHuman: What is the latest age to get HPV vaccine?\n\nAI: Everyone through age 26 years should get HPV vaccine if they were not fully vaccinated already.\nHuman: What are the side effects of HPV vaccine?\n\nA: Like any vaccine or medicine, HPV vaccines can have side effects. The most common side effects are mild and include: Pain, redness, or swelling in the arm where the shot was given; Dizziness or fainting (fainting after any vaccination, including HPV vaccine, is more common among adolescents); Nausea; Headache. Please consult your doctor for medical decision.\nHuman: What if my child has a severe allergic reaction to HPV vaccine?\n\nAI: If severe allergic reaction happens, seek for medical help immediately. Your doctor will help you determine if your child is allergy to HPV vaccine. Over 15 years of monitoring have shown that HPV vaccines are very safe and effective for most people. Like all vaccines, scientists continue to monitor HPV vaccines to ensure they are safe and effective. \nHuman: Is HPV vaccine required for a boy?\n\nAI: It is highly recommended for both boys and girls."

# response = openai.Completion.create(
#   model="text-davinci-002",
#   prompt=session_promt,
#   temperature=0.9,
#   max_tokens=200,
#   top_p=1,
#   frequency_penalty=1,
#   presence_penalty=1,
#   stop=["\n\nAI: ","\n"]
# )

def ask(question, chat_log=None):
  if chat_log is None: 
    chat_log = start_chat_log 

  prompt = f'{chat_log}Human: {question}\nAI:'
  response = completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    best_of=1,
    stop=["\nHuman", "\n"])
  answer = response['choices'][0]['text']
  return str(answer)

def append_interaction_to_chat_log(question, answer, chat_log=None):
  if chat_log is None:
      chat_log = start_chat_log
  return f'{chat_log}Human: {question}\nAI: {answer}\n'