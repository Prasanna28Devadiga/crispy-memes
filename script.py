import openai
import random
openai.api_key = OPENAI_API_KEY='Insert your key here'

# list engines
engines = openai.Engine.list()



string1= ""
list_prompts=[]
# Data Ckeaning
f= open("Drake.txt","r")
list_toptext=[]    
list_bottomtext=[]
while True:
    line1 = f.readline().rstrip('\n').lower()
    line2 = f.readline().rstrip('\n').lower()
    list_toptext.append(line1)
    list_bottomtext.append(line2)
    if not line1: break 
print(list_toptext)
print(len(list_toptext))
for i in range(len(list_toptext)):
    string1=list_toptext[i]
    string1+=" "
    string1+=list_bottomtext[i]
    list_prompts.append(string1)
list =[]        
print(len(list_prompts))
#print(list_prompts)
prompt=string1
for i in range(0,len(list_toptext)):
    prompt+=str(i+1) + "."
    prompt+=list_toptext[i] +" "
    prompt+=list_bottomtext[i]
print(prompt)    
#Text Generation
for i in range(100):
    completion = openai.Completion.create(engine="curie", prompt=prompt,max_tokens=20,temperature=0.85) #curie worked pretty well for our cause
    list.append(completion.choices[0].text)

with open("drake_generation_100.txt", "w",encoding="utf-8") as textfile:
    for element in list:
        textfile.write(element + "\n")
    textfile.close()
    
