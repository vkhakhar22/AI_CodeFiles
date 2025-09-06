#import colorama
#from colorama import Fore, Style
#from textblob import TextBlob
#colorama.init()

#print(f"{Fore.CYAN}Welcome to Sentiment Spy! {Style.RESET_ALL}")

#user_name=input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}").strip()
# if not user_name:
#     user_name="Mystery Agent"

# c_h=[]

# print("\n",Fore.CYAN,"Hello,Agent",user_name,"!")
# print("Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment")
# print("Type",Fore.YELLOW,"reset",Fore.CYAN,Fore.YELLOW,"history",Fore.CYAN ,"or",Fore.YELLOW,"exit",Fore.CYAN,"to quit",Style.RESET_ALL,"\n")

# while True:
#     user_input=input(Fore.GREEN,">>",Style.RESET_ALL).strip()

#     if not user_input:
#         print(Fore.RED,"Please enter some text or a valid command",Style.RESET_ALL)
#         continue


#     if user_input.lower() == "exit":
#         print(f"\n{Fore.BLUE}Exiting Sentiment Spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")
#         break

#     elif user_input.lower() == "reset":
#         c_h.clear()
#         print(f"{Fore.CYAN}ALL conversation history cleared!{Style.RESET_ALL}")
#         continue

#     elif user_input.lower() == "history":
#         if not c_h:
#             print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
#         else:
#             print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
#             for idx, (text, polarity, sentiment_type) in enumerate(c_h, start=1):
#                 if sentiment_type == "Positive":
#                     color = Fore.GREEN
#                 elif sentiment_type == "Negative":
#                     color = Fore.RED
#                 else:
#                     color = Fore.YELLOW

#                 print(f"{idx}. {color}{text} "
#                       f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
#         continue
    
#     polarity = TextBlob(user_input).sentiment.polarity
#     if polarity > 0.25:
#         sentiment_type = "Positive"
#         color = Fore.GREEN
#     elif polarity < -0.25:
#         sentiment_type = "Negative"
#         color = Fore.RED
#     else:
#         sentiment_type = "Neutral"
#         color = Fore.YELLOW

#     c_h.append((user_input, polarity, sentiment_type))

#     print(f"{color}{sentiment_type} sentiment detected! "
#           f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")


from textblob import TextBlob

print("Welcome to Sentiment Spy!")

user_name = input("Please enter your name:").strip()
if not user_name:
    user_name = "Mystery Agent"

c_h = []

print("\nHello, Agent", user_name, "!")
print("Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment")
print("Type reset, history, or exit to quit\n")

while True:
    user_input = input(">>").strip()

    if not user_input:
        print("Please enter some text or a valid command")
        continue

    if user_input.lower() == "exit":
        print(f"\nExiting Sentiment Spy. Farewell, Agent {user_name}!")
        break

    elif user_input.lower() == "reset":
        c_h.clear()
        print("ALL conversation history cleared!")
        continue

    elif user_input.lower() == "history":
        if not c_h:
            print("No conversation history yet.")
        else:
            print("Conversation History:")
            for idx, (text, polarity, sentiment_type) in enumerate(c_h, start=1):
                print(f"{idx}. {text} (Polarity: {polarity:.2f}, {sentiment_type})")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
    elif polarity < -0.25:
        sentiment_type = "Negative"
    else:
        sentiment_type = "Neutral"

    c_h.append((user_input, polarity, sentiment_type))

    print(f"{sentiment_type} sentiment detected! (Polarity: {polarity:.2f})")
