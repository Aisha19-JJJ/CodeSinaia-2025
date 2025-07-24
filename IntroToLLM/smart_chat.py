import ollama
from smart_agent import SmartAgent as blud

sarmaluta=blud("gemma3:1b")


question=input ("Question???? ").strip()
while question!="/pa":
    if question!="":
        print (sarmaluta.chat(question))
    question=input ("Question???? ").strip()    


  