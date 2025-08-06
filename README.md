# Package Tracking Chatbot CLI

A simple Python-based command-line interface chatbot that assists users with their lost packages by verifying a tracking number and name, then guiding them through delivery status checks, refund/replacement requests, and looping to track additional packages.

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yiduoke/lost-package-chatbot.git
   cd lost-package-chatbot
   ```

2. **Ensure you have Python 3 installed**  
   ```bash
   python3 --version
   ```

3. **Run the chatbot**  
   ```bash
   python3 chatbot.py
   ```

---

## Usage

1. **Welcome prompt**  
   The bot greets you and asks for a tracking number. You may type `END` at any point to end the conversation.

2. **Tracking-number validation**  
   - Only two demo records are supported:  
     - `12345678` → `yiduo`  
     - `88888888` → `cameron`  
   - Invalid or unrecognized numbers will prompt a retry message.

3. **Name verification**  
   - After inputting valid tracking number, you must enter the matching name.  
   - Mismatches prompt a retry.

4. **Delivered status**  
   - If you’ve already received the package, you will be prompted to track another.  
   - If not, the bot asks if you’ve checked your delivery area and neighbors.

5. **User has/has not checked everywhere**  
   - **Checked already?** Prompt to request a **refund** or **replacement**.
   - **Not yet checked?** Bot instructs you to check, then immediately offers to track another package.

6. **Track another package or exit**  
   - After refund/replacement, the bot asks if you’d like to track another package.  
   - Type `yes` to restart, or `no`/`END` to exit.

---

## Demo Test Cases

There are two predefined tracking numbers for test usage:

| Tracking #  | Name      |  
|-------------|-----------|
| `12345678`  | `yiduo`   |  
| `88888888`  | `cameron` |

Example session:
```text
Bot: Welcome! You may end this conversation at any time by typing 'END'. Please enter your package tracking number.
You: 129837asyd
Bot: Hmmm I cannot find this number. Please check and try again.
You: 126876132
Bot: Hmmm I cannot find this number. Please check and try again.
You: kashdjasgd
Bot: Hmmm I cannot find this number. Please check and try again.
You: asdb
Bot: Hmmm I cannot find this number. Please check and try again.
You: 12345678
Bot: Got it. Please enter your name as on the order.
You: xzmnbcmndh
Bot: Hmmm that doesn't match our records. Please check your spelling and try again.
You: ashdjkshd
Bot: Hmmm that doesn't match our records. Please check your spelling and try again.
You: 218936876asd
Bot: Hmmm that doesn't match our records. Please check your spelling and try again.
You: yiduo
Bot: Your package (#12345678) was delivered on August 4th, 2025. Have you received it? (yes/no)
You: no
Bot: I am sorry to hear that! Have you checked around your delivery area and asked your neighbors? (yes/no)
You: no
Bot: Please check around your porch, mailbox, or with your neighbors.
Bot: Would you like to track another package? (yes/no)
You: yes
Bot: Sure! Please enter the new tracking number.
You: 12345678
Bot: Got it. Please enter your name as on the order.
You: yiduo
Bot: Your package (#12345678) was delivered on August 4th, 2025. Have you received it? (yes/no)
You: no
Bot: I am sorry to hear that! Have you checked around your delivery area and asked your neighbors? (yes/no)
You: yes
Bot: Would you like a refund or a replacement? (refund/replace)
You: refund
Bot: Your refund request has been submitted. You will receive a confirmation email shortly.
Bot: Would you like to track another package? (yes/no)
You: yes
Bot: Sure! Please enter the new tracking number.
You: 88888888
Bot: Got it. Please enter your name as on the order.
You: cameron
Bot: Your package (#88888888) was delivered on August 4th, 2025. Have you received it? (yes/no)
You: no
Bot: I am sorry to hear that! Have you checked around your delivery area and asked your neighbors? (yes/no)
You: yes
Bot: Would you like a refund or a replacement? (refund/replace)
You: replace
Bot: A replacement request has been submitted. You will receive new tracking info soon.
Bot: Would you like to track another package? (yes/no)
You: yes
Bot: Sure! Please enter the new tracking number.
You: 88888888
Bot: Got it. Please enter your name as on the order.
You: cameron
Bot: Your package (#88888888) was delivered on August 4th, 2025. Have you received it? (yes/no)
You: yes
Bot: Great! Would you like to track another package? (yes/no)
You: no
Bot: Thank you! Goodbye.
```