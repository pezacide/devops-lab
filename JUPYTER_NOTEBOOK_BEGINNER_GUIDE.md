![Status](https://img.shields.io/badge/Status-Beginner%20Guide-green)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Level](https://img.shields.io/badge/Level-Complete%20Beginner-yellow)

# 📓 Jupyter Notebook Beginner Guide

This guide is for complete beginners who want to install Jupyter Notebook, start it for the first time, and create their first working notebook.

Jupyter Notebook lets you combine **code**, **notes**, **tables**, and **output** in one place. It is great for learning Python, data analysis, experimentation, and keeping track of your work.

---

## 🏁 Phase 0: What You Need Before You Start

**Goal:** Make sure your computer has the basics required to run Jupyter Notebook.

You will need:

1. A computer running **Windows 11**, macOS, or Linux.
2. An internet connection to download Python and Jupyter.
3. A terminal app:
   - **Windows:** Command Prompt or PowerShell
   - **macOS/Linux:** Terminal

For complete beginners on **Windows 11**, Command Prompt is perfectly fine.

---

## 🐍 Phase 1: Install Python

**Goal:** Install Python, which Jupyter Notebook needs to run.

### Step 1: Download Python

1. Open your browser and go to **python.org/downloads**.
2. Download the latest **Python 3** version for Windows.
3. Run the installer.

### Step 2: Important Checkbox During Install

When the installer opens:

1. **Tick the box** that says **Add Python to PATH**.
2. Click **Install Now**.

This step is important because it lets you run Python and pip from Command Prompt.

### Step 3: Check Python Installed Correctly

Open **Command Prompt** and run:

```bash
python --version
pip --version
```

If both commands return version numbers, Python is installed correctly.

---

## 📦 Phase 2: Install Jupyter Notebook

**Goal:** Install Jupyter Notebook using pip.

In Command Prompt, run:

```bash
pip install notebook
```

If pip needs updating first, run:

```bash
python -m pip install --upgrade pip
pip install notebook
```

Wait for the installation to finish.

---

## 🚀 Phase 3: Start Jupyter Notebook

**Goal:** Launch Jupyter Notebook in your browser.

### Step 1: Open the Folder You Want to Work In

In Command Prompt, move to the folder where you want your notebook files saved.

Example:

```bash
cd Desktop
mkdir jupyter-practice
cd jupyter-practice
```

### Step 2: Launch Jupyter Notebook

Run:

```bash
jupyter notebook
```

Your default web browser should open automatically.

You will usually see the **Jupyter Notebook Dashboard**, which is the home screen where you can create and open notebooks.

---

## 📄 Phase 4: Create Your First Notebook

**Goal:** Make a notebook and understand what a cell is.

### Step 1: Create a New Notebook

In the Jupyter dashboard:

1. Click **New**.
2. Select **Python 3**.

A new notebook will open in a new browser tab.

### Step 2: Understand Cells

A notebook is made up of **cells**.

You will mainly use two types:

1. **Code cells** — for Python code
2. **Markdown cells** — for headings, notes, and explanations

---

## ▶️ Phase 5: Run Your First Code

**Goal:** Write and run a simple Python command.

In the first cell, type:

```python
print("Hello, world!")
```

Now press:

```text
Shift + Enter
```

You should see:

```text
Hello, world!
```

That means your notebook is working.

---

## 📝 Phase 6: Add Notes with Markdown

**Goal:** Learn how to add headings and written notes.

### Step 1: Add a New Cell

Click the **+** button on the toolbar.

### Step 2: Change the Cell Type

Change the cell from **Code** to **Markdown** using the dropdown menu.

### Step 3: Type This

```markdown
# My First Notebook

This notebook is being used to learn Jupyter Notebook.
```

Run the cell with:

```text
Shift + Enter
```

Now it will display as formatted text instead of code.

---

## 🧪 Phase 7: Try a Small Python Example

**Goal:** See how variables work in a notebook.

In a new code cell, type:

```python
name = "Geoff"
age = 40
print("Name:", name)
print("Age:", age)
```

Run it with:

```text
Shift + Enter
```

You should see the output underneath the cell.

---

## 💾 Phase 8: Save Your Work

**Goal:** Make sure your notebook is saved properly.

You can save by:

1. Clicking the **Save** icon
2. Or pressing **Ctrl + S**

Your notebook will be saved as a file ending in:

```text
.ipynb
```

---

## ⌨️ Phase 9: Learn the Most Useful Shortcuts

**Goal:** Get comfortable moving around the notebook.

Here are the most useful beginner shortcuts:

| Action | Shortcut |
| --- | --- |
| Run current cell | `Shift + Enter` |
| Save notebook | `Ctrl + S` |
| Add cell above | `A` |
| Add cell below | `B` |
| Change cell to Markdown | `M` |
| Change cell to Code | `Y` |
| Enter edit mode | `Enter` |
| Leave edit mode | `Esc` |
|

**Tip:** `A`, `B`, `M`, and `Y` work when you are in **command mode**. Press `Esc` first.

---

## 📚 Phase 10: Install Extra Python Packages Later

**Goal:** Learn how to add more tools when you need them.

For example, if you want to work with data later, you may want packages like **pandas** and **matplotlib**.

Install them in Command Prompt with:

```bash
pip install pandas matplotlib
```

Then in your notebook, you can use:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

---

## 🛑 Phase 11: Close Jupyter Properly

**Goal:** Shut everything down cleanly.

Closing the browser tab does **not always stop** the Jupyter server.

To stop it properly:

1. Go back to the Command Prompt window where Jupyter is running.
2. Press:

```text
Ctrl + C
```

3. Confirm if asked.

---

## 🧯 Phase 12: Common Beginner Problems

**Goal:** Fix the most common setup issues.

### Problem 1: `python` is not recognised

This usually means Python was not added to PATH.

**Fix:** Reinstall Python and make sure **Add Python to PATH** is ticked.

### Problem 2: `pip` is not recognised

Try:

```bash
python -m pip --version
python -m pip install notebook
```

### Problem 3: Browser does not open automatically

Jupyter usually prints a local web address in the terminal. It often looks like this:

```text
http://localhost:8888/tree
```

Copy and paste that into your browser.

### Problem 4: A code cell does not run

Make sure you are pressing:

```text
Shift + Enter
```

Just pressing **Enter** only edits the cell.

---

## ✅ Your First Beginner Workflow

If you want the shortest path from zero to success, follow this exact order:

1. Install Python
2. Open Command Prompt
3. Run `pip install notebook`
4. Create a folder for your notebook files
5. Run `jupyter notebook`
6. Click **New > Python 3**
7. Type `print("Hello, world!")`
8. Press `Shift + Enter`
9. Save the notebook
10. Stop Jupyter later with `Ctrl + C`

---

## ⚡ Quick Start Command Cheat Sheet

| Step | Command |
| --- | --- |
| Check Python | `python --version` |
| Check pip | `pip --version` |
| Upgrade pip | `python -m pip install --upgrade pip` |
| Install Jupyter | `pip install notebook` |
| Create practice folder | `mkdir jupyter-practice` |
| Enter folder | `cd jupyter-practice` |
| Start Jupyter | `jupyter notebook` |
| Stop Jupyter | `Ctrl + C` |

---

## 🎯 What to Learn Next

Once you are comfortable with the basics, the next good topics are:

1. Python variables and data types
2. Using pandas for tables and data
3. Making graphs with matplotlib
4. Organising notebooks for projects
5. Moving from Jupyter Notebook to **JupyterLab** later

---

## 📌 Final Tip

The best way to learn Jupyter Notebook is to use it for small, simple tasks first.

Start with:

- printing text
- basic maths
- simple variables
- short notes in Markdown

Then build up from there.

You do **not** need to learn everything at once.
