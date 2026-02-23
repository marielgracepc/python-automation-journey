
---

# **Final Project – ECO Automation**

```markdown
# Final Project – ECO Outlook → Excel Automation

## Objective
Recreate the full VBA ECO Release Notify automation in Python.

## What I Learned
- Read Outlook TCADMIN folder
- Filter emails starting with "ECO Release Notify:"
- Extract ECO number, model, description
- Store results in Python list/dictionary
- Export results to Excel using `pandas`
- Use regex for parsing subject lines

## Practice Example
```python
import win32com.client
import pandas as pd
import re

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
tcadmin = namespace.GetDefaultFolder(6).Folders["TCADMIN"]

eco_list = []

for mail in tcadmin.Items:
    subject = mail.Subject
    if subject.startswith("ECO Release Notify:"):
        match = re.search(r'ECO\d+', subject)
        if match:
            eco_number = match.group()
            eco_list.append({
                "ECO Number": eco_number,
                "Subject": subject,
                "Received": mail.ReceivedTime
            })

df = pd.DataFrame(eco_list)
df.to_excel("eco_report.xlsx", index=False)
