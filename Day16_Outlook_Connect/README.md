
---

# **Day 16 – Connect to Outlook**

```markdown
# Day 16 – Connect to Outlook

## Objective
Learn to connect to Outlook using Python and access folders.

## What I Learned
- Using `pywin32` to automate Outlook
- Accessing the default Inbox and subfolders
- Iterating over mail items
- Filtering based on subject

## Practice Example
```python
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
inbox = namespace.GetDefaultFolder(6)  # 6 = Inbox
tcadmin = inbox.Folders["TCADMIN"]

for mail in tcadmin.Items:
    subject = mail.Subject
    if subject.startswith("ECO Release Notify:"):
        print(subject)
