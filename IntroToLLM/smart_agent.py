import ollama

class SmartAgent:
    model_name=''
    chat_log=[]
    def __init__(self, model):
        self.model_name = model
        self.chat_log = [{
            'role': 'user',
            'content':
                "You are a chatbot named Cat. You like to drink milk, listen to the Spice Girls, and solve math problems. Say MIAU at the start of every new sentence."
        }]
        print("Agent is created!")
    def chat(self, prompt):
        self.chat_log.append ({'role': 'user', 'content': prompt})
        answer=ollama.chat(model=self.model_name, messages=self.chat_log)
        ret=answer['message']['content']
        return ret
