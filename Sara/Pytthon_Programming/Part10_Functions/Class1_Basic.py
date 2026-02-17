#Function without paramaters

def Hello():
    print("Hello World")
    
Hello()  # calling the function

"""
********OUTPUT********

PS C:\PythonAutomationProject\GTM_PS_BATCH14\Sara\Pytthon_Programming\Part10_Functions> python Class1_Basic.py

Hello World
"""

print("_" * 50)
#########################################################################################

#function with parameters : Pass by value

def Learning(a):
    print("I am learning", a)

Learning("Python with Selenium")

"""
********OUTPUT********
i/p:  PS C:\PythonAutomationProject\GTM_PS_BATCH14\Sara\Pytthon_Programming\Part10_Functions> python Class1_Basic.py

I am learning Python with Selenium

"""
print("_"*50)
##############################################################

# function with paramaters :: Pass by reference

def AI_tools(b):
    print(b,"is an AI tool")

a1="ChatGPT"
a2="DALL-E"

AI_tools(a1)
print("_"*50)

AI_tools(b=a2) #parameter defined in def is == to reference parameter

"""
********OUTPUT********
ChatGPT is an AI tool
__________________________________________________
DALL-E is an AI tool

"""
print("_"*50)
#############################################################
