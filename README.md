# 🤖 My Personal Python Agents Squad

Welcome to my quirky world of **Python agents**—because remembering everything is overrated.  

This project contains **four autonomous agents** that know everything about me, my student life, my library books, and even my bank account!  

---

## Agents Overview

1. **Personal Agent**  
   - Knows my full name and user ID.  
   - Responds instantly to personal info queries.  
   - Example:
     ```python
     "What is my name and my user id?"
     # Output: The user info is: Name = Faqeha Noor (FN), ID = 10690
     ```

2. **Student Profile Agent**  
   - Tracks semesters, total courses, and profile info.  
   - Example:
     ```python
     "Provide student profile"
     # Output: The Student Profile: StudentProfile(student_id='10690', student_name='Faqeha Noor (FN)', current_quater='Q4', total_courses=7)
     ```

3. **Library Book Agent**  
   - Gives details about a library book and its availability.  
   - Example:
     ```python
     "Give Library Book Details"
     # Output: Library Book Details: LibraryBook(book_id='1088', book_title='JavaScript Mastery', author_name='John Dalton', is_available=True)
     ```

4. **Bank Account Agent**  
   - Knows account number, balance, and account type.  
   - Example:
     ```python
     "Give Customer Bank Account Details"
     # Output: Customer Bank Account Details is : BankAccount(account_number='ACC-789456', customer_name='Fatima Khan', account_balance=75500.50, account_type='savings')
     ```

---

## Features

- ⚡ **Fast & Async**: Uses `asyncio` for lightning-fast responses.  
- 🔧 **Tool-based Architecture**: Each agent has a function tool for specific queries.  
- 😂 **Funny & Engaging**: These agents are basically my digital sidekicks.  

---

## How to Run

1. Clone the repository:  
   ```bash
   git clone <repo-url>
   cd <repo-folder>
