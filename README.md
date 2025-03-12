## GitGhost 👻
Find out who doesn’t follow you back on GitHub!
GitGhost is a powerful GitHub unfollowers tracking tool that helps you identify users you follow but who don’t follow you back.

## ✨ Features
- ✅ Find non-followers – See who isn’t following you back
- ✅ Uses GitHub API – Fast & reliable data fetching
- ✅ ANSI Colors – Clean and readable output
- ✅ Save Results – Option to save unfollowers list to a file
- ✅ Easy to Use – Just run, enter your username, and get results!

## 🛠️ Installation
Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/s-r-e-e-r-a-j/GitGhost.git
```
```bash
cd GitGhost
```

## 📦 Dependencies
Make sure you have Python installed along with the following dependencies:

- **requests**
  
  install it by 
```bash
pip install requests
```
## 🚀 Usage
**Run the script:**

```bash
python gitghost.py
```

 ## 🔑 Getting a GitHub Personal Access Token  

GitGhost requires a **GitHub personal access token (PAT)** to authenticate API requests. Follow these steps to generate one:  

### 📌 Step 1: Open GitHub Token Settings  
Go to the **GitHub Personal Access Tokens** page:  

🔗 [GitHub Token Settings](https://github.com/settings/tokens)  

### 🛠️ Step 2: Generate a New Token  
1. Click **"Generate new token (classic)"**.  
2. In the **"Note"** field, enter a description (e.g., *GitGhost Token*).  

### 🔒 Step 3: Set Token Permissions  
- Under **"Select scopes"**, check the box for:  
  ✅ **`read:user`** – Required to fetch your followers and following lists.  

### ✅ Step 4: Generate & Copy the Token  
1. Scroll down and click **"Generate token"**.  
2. Copy the token and store it securely (you won’t see it again).  

### 🚀 Step 5: Use the Token in GitGhost  
- When prompted by GitGhost, paste your token to authenticate.  

### ⚠️ Important Notes  
- Never share your **GitHub token** with anyone.  
- If your token is compromised, **revoke it** immediately and generate a new one.  
- GitHub tokens **expire** based on the duration you set, so renew it if needed.  

---

This guide ensures you have a **valid GitHub token** to use with GitGhost.  

## What It Does:
- 1️⃣ Prompts for your GitHub username
- 2️⃣ Asks for your GitHub token 
- 3️⃣ Fetches your followers and following lists
- 4️⃣ Shows users you follow who don’t follow you back
- 5️⃣ Lets you save the results to a file

## 📸 Screenshot

![VirtualBox_klinux13_27_02_2025_22_58_48](https://github.com/user-attachments/assets/00751552-0d1f-48a7-9c98-12ef6973f6e0)


## 📜 License
This project is licensed under the MIT License.

