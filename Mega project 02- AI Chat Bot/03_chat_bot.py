from ai import ai
import pyautogui
import pyperclip
import time

pyautogui.click(1283, 1048)
time.sleep(1)

while True:
    pyautogui.moveTo(732, 222)
    pyautogui.dragTo(1806, 912, duration=1.0, button='left')

    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1425, 592)
    time.sleep(1)
    
    text = pyperclip.paste()
    sender = text.split('\n')
    print(sender)
    n = len(sender)

    if 'Vishal' in sender[n-1]:
        continue

    t= ai(text)
    pyperclip.copy(t)
    print(t)
    pyautogui.click(1367, 965)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')



# import pyautogui
# import time
# import pyperclip
# from openai import OpenAI

# client = OpenAI(
#     api_key=("***********************")
# )

# def is_last_message_from_sender(chat_log, sender_name= 'bhonpu'):
#     # Remove any leading/trailing whitespace and split into lines
#     lines = chat_log.strip().split("/2025] ")[-1]
#     if sender_name in lines:
#         return True
#     return False
    
    
# # Small delay to switch to the target window
# time.sleep(2)

#     # Click on the icon at (1318, 1044)
# pyautogui.click(1283, 1048)
# time.sleep(2)  # Wait for any response from the system

# while True:

#     # Move to the starting point of selection
#     pyautogui.moveTo(732, 222)
#     pyautogui.mouseDown()  # Hold the mouse button

#     # Drag to the end point of selection
#     pyautogui.moveTo(1806, 912, duration=1)
#     pyautogui.mouseUp()  # Release the mouse button

#     # Copy selected text
#     pyautogui.hotkey('ctrl', 'c')
#     pyautogui.click(1425, 592)
#     time.sleep(1)  # Wait for clipboard update[2:57 PM, 2/14/2025] Vishal Dwivedi: Haan, chalu ho jata hoon. Kya topic par baat karni hai?

#     # Get copied text from clipboard and store it in a variable
#     chat_hittory = pyperclip.paste()
#     print("Copied Text:", chat_hittory)

#     # # Store copied text in a variable
#     # selected_text = chat_hittory
#     if is_last_message_from_sender(chat_hittory):
#         completion = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "You are a person named vishal who speas hindi as well as english. you  are from india and a coder by proffesion. you analyse chat history and respond like vishal. and give small and accurate respond of the next chat according to previous conversation. and please dont write any time stamp and vishal dwivedi name"},
#                 {
#                     "role": "user",
#                     "content": chat_hittory
#                 }
#             ]
#         )

#         response= completion.choices[0].message.content
#         pyperclip.copy(response)

#         # Click at (1367, 965)
#         pyautogui.click(1367, 965)
#         time.sleep(0.5)

#         # Paste the copied text
#         pyautogui.hotkey('ctrl', 'v')
#         time.sleep(0.5)

#         # Press Enter
#         pyautogui.press('enter')


