#!/usr/bin/env python3
"""
Simple CLI chatbot for tracking a lost package with demo records.
Supports two valid records: 12345678 -> yiduo, 88888888 -> cameron
"""

def chatbot():
    # Predefined valid tracking-number -> user-name map
    valid_records = {
        '12345678': 'yiduo',
        '88888888': 'cameron'
    }
    state = 'start'
    tracking_number = ''

    while True:
        if state == 'start':
            print("Bot: Welcome! You may end the conversation at any time by typing 'END'. Please enter your package tracking number.")
            state = 'await_tracking'

        elif state == 'await_tracking':
            user = input('You: ').strip()
            if user.upper() == 'END':
                print('Bot: Thank you! Goodbye.')
                break
            if user in valid_records:
                tracking_number = user
                print('Bot: Got it. Please enter your name as on the order.')
                state = 'await_name'
            else:
                print('Bot: I cannot find this number. Please check and try again.')

        elif state == 'await_name':
            user = input('You: ').strip().lower()
            if user.upper() == 'END':
                print('Bot: Thank you! Goodbye.')
                break
            expected = valid_records.get(tracking_number, '').lower()
            if user == expected:
                print(f"Bot: Your package (#{tracking_number}) was delivered on August 4th, 2025. Have you received it? (yes/no)")
                state = 'await_received'
            else:
                print("Bot: That doesn't match our records. Please check your spelling and try again.")

        elif state == 'await_received':
            user = input('You: ').strip().lower()
            if user.upper() == 'END':
                print('Bot: Thank you! Goodbye.')
                break
            if user in ('yes', 'y'):
                print('Bot: Great! Would you like to track another package? (yes/no)')
                state = 'await_another'
            elif user in ('no', 'n'):
                print('Bot: I am sorry to hear that! Have you checked around your delivery area and asked your neighbors? (yes/no)')
                state = 'await_checked'
            else:
                print('Bot: Please reply with yes or no.')

        elif state == 'await_checked':
            user = input('You: ').strip().lower()
            if user.upper() == 'END':
                print('Bot: Thank you! Goodbye.')
                break
            if user in ('yes', 'y'):
                print('Bot: Would you like a refund or a replacement? (refund/replace)')
                state = 'await_choice'
            elif user in ('no', 'n'):
                print('Bot: Please check around porch, mailbox, or with your neighbors and let me know.')
                # Immediately ask to track another package
                print('Bot: Would you like to track another package? (yes/no)')
                state = 'await_another'
            else:
                print('Bot: Please reply with yes or no.')

        elif state == 'await_choice':
            user = input('You: ').strip().lower()
            if user.upper() == 'END':
                print('Bot: Thank you! Goodbye.')
                break
            if 'refund' in user:
                print('Bot: Your refund request has been submitted. You will receive a confirmation email shortly.')
                print('Bot: Would you like to track another package? (yes/no)')
                state = 'await_another'
            elif 'replace' in user or 'replacement' in user:
                print('Bot: A replacement request has been submitted. You will receive new tracking info soon.')
                # Immediately ask to track another package
                print('Bot: Would you like to track another package? (yes/no)')
                state = 'await_another'
            else:
                print('Bot: Please type refund or replace.')

        elif state == 'await_another':
            user = input('You: ').strip().lower()
            if user.upper() == 'END':
                print('Bot: Thank you! Goodbye.')
                break
            if user in ('yes', 'y'):
                print('Bot: Sure! Please enter the new tracking number.')
                state = 'await_tracking'
            elif user in ('no', 'n'):
                print('Bot: Thank you! Goodbye.')
                break
            else:
                print('Bot: Please reply with yes or no.')

if __name__ == '__main__':
    chatbot()

