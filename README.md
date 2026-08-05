# Bank-Simulator-Python

A Python project simulating a simple **banking system** with multiple banks (HDFC, AXIS, SBI).  
This project demonstrates **file handling, data consistency, and CRUD operations** (Create, Read, Update, Delete) along with transaction logic.

---

## 📂 Repository Structure
- **HDFC/** → Folder containing individual account files for HDFC Bank.  
- **AXIS/** → Folder containing individual account files for Axis Bank.  
- **SBI/** → Folder containing individual account files for SBI Bank.  
- **Bank(RAW).txt** → Development/raw version of the bank file.  
- **Bank.py** → Main program file containing all functions and menu logic.  
- **README.md** → Documentation for the project.  

⚠️ Note: The text file used for storage is not uploaded. It will be created automatically when the program runs.

---

## 🚀 Features
- **Account Creation** → New accounts can be created by bank employees only.  
- **Bank Employee PIN (123)**  
- **Balance Check** → View account details and current balance.  
- **Deposit / Withdraw** → Add or remove money from accounts with validation.  
- **Transfer** → Move money between accounts (even across different banks).  
- **Update Pin** → Change account pin securely.  
- **Update Details** → Modify account holder information (e.g., name).  
- **Multi-Bank Support** → Works with HDFC, AXIS, and SBI folders.  

---

## 🧩 Challenges Faced
- **Multi-Bank Transfers**: The most difficult part was enabling transfers between accounts in different banks without a shared system. I solved this by designing separate storage files for each bank and building logic to handle cross-bank transactions.  
- **Efficient Data Search**: To reduce runtime, I implemented a search mechanism that validates account numbers and passwords directly from the main file before accessing individual bank folders.  
- **File-Based Storage**: Managing multiple files for accounts and ensuring consistency across operations required careful design of read/write functions.  

---

## 🔮 Future Improvements
- **Banking Investments**: Add features like fixed deposits, recurring deposits, and investment tracking.  
- **Enhanced User Profiles**: Store more customer details (phone number, address, etc.) for better account management.  
- **Database Integration**: Transition from file-based storage to **SQLite/MySQL** for scalability and faster queries.  
- **Security Enhancements**: Stronger encryption for PINs and account data.  

---

## ⚙️ How to Run
1. Clone or download the repository.  
2. Ensure the folder structure is intact.  
3. Run `Bank.py` in Python.  

