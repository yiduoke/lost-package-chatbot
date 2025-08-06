#!/usr/bin/env python3
"""
Simple CLI chatbot for tracking a lost package with demo records.
Supports two valid records: 12345678 -> yiduo, 88888888 -> cameron
"""

def chatbot():
    # Predefined valid {tracking-number: user-name} dictionary
    # The two valid tracking numbers are '12345678' and '88888888',
    # and their respective owners are 'yiduo' and 'cameron'
    valid_records = {
        '12345678': 'yiduo',
        '88888888': 'cameron'
    }
    state = 'start'
    tracking_number = ''

    while True:
        # Start of the conversation
        if state == 'start':
            print("Bot: Welcome! You may end this conversation at any time by typing 'END'. Please enter your package tracking number.")
            state = 'await_tracking'
        
        # Waiting for user to enter a tracking number
        elif state == 'await_tracking':
            user = input('You: ').strip()
            if user.upper() == 'END': # user may end the convo at any time
                print('Bot: Thank you! Goodbye.')
                break
            if user in valid_records: # user gave a valid tracking number
                tracking_number = user
                print('Bot: Got it. Please enter your name as on the order.')
                state = 'await_name'
            else: # user gave an invalid tracking number
                print('Bot: Hmmm I cannot find this number. Please check and try again.')

        # Waiting for user to enter their name
        elif state == 'await_name':
            user = input('You: ').strip().lower()
            if user.upper() == 'END': # user may end the convo at any time
                print('Bot: Thank you! Goodbye.')
                break
            expected = valid_records.get(tracking_number, '').lower()
            if user == expected: # user gave a matching name for their tracking number
                print(f"Bot: Your package (#{tracking_number}) was delivered on August 4th, 2025. Have you received it? (yes/no)")
                state = 'await_received'
            else: # user gave a name that does not match up with their tracking number
                print("Bot: Hmmm that doesn't match our records. Please check your spelling and try again.")

        # Waiting for user to answer whether they've received their package
        elif state == 'await_received':
            user = input('You: ').strip().lower()
            if user.upper() == 'END': # user may end the convo at any time
                print('Bot: Thank you! Goodbye.')
                break
            if user in ('yes', 'y'): # user says yes, they've received their package already
                print('Bot: Great! Would you like to track another package? (yes/no)')
                state = 'await_another'
            elif user in ('no', 'n'): # user says no, they've not received their package yet
                print('Bot: I am sorry to hear that! Have you checked around your delivery area and asked your neighbors? (yes/no)')
                state = 'await_checked'
            else:
                print('Bot: Please reply with yes or no.') # invalid input

        # User said they did not receive the package. Waiting for user to answer whether they've checked everywhere already
        elif state == 'await_checked':
            user = input('You: ').strip().lower()
            if user.upper() == 'END': # user may end the convo at any time
                print('Bot: Thank you! Goodbye.')
                break
            if user in ('yes', 'y'): # user has checked everywhere for the missing package
                print('Bot: Would you like a refund or a replacement? (refund/replace)')
                state = 'await_choice'
            elif user in ('no', 'n'): # user has not checked everywhere yet
                print('Bot: Please check around your porch, mailbox, or with your neighbors.')
                # Immediately ask to track another package
                print('Bot: Would you like to track another package? (yes/no)')
                state = 'await_another'
            else:
                print('Bot: Please reply with yes or no.') # invalid input

        # User affirmed that they checked everywhere already. Waiting for user to answer whether they want a refund or replacement
        elif state == 'await_choice':
            user = input('You: ').strip().lower()
            if user.upper() == 'END': # user may end the convo at any time
                print('Bot: Thank you! Goodbye.')
                break
            if 'refund' in user: # user wants a refund
                print('Bot: Your refund request has been submitted. You will receive a confirmation email shortly.')
                print('Bot: Would you like to track another package? (yes/no)') # immediately ask to track another package
                state = 'await_another'
            elif 'replace' in user or 'replacement' in user: # user wants a replacement
                print('Bot: A replacement request has been submitted. You will receive new tracking info soon.')
                print('Bot: Would you like to track another package? (yes/no)') # immediately ask to track another package
                state = 'await_another'
            else:
                print('Bot: Please type refund or replace.') # invalid input

        # Waiting for user to answer whether they want to track another package
        elif state == 'await_another':
            user = input('You: ').strip().lower()
            if user.upper() == 'END': # user may end the convo at any time
                print('Bot: Thank you! Goodbye.')
                break
            if user in ('yes', 'y'): # user wants to track another package
                print('Bot: Sure! Please enter the new tracking number.')
                state = 'await_tracking'
            elif user in ('no', 'n'): # user does not want to track another package. End the convo
                print('Bot: Thank you! Goodbye.')
                break
            else:
                print('Bot: Please reply with yes or no.') # invalid input

if __name__ == '__main__':
    chatbot()

