## PDF JavaScript Embedder — NZRXHX
---
#### Features

    Embeds arbitrary JavaScript into any PDF file

    Executes the script on PDF open (supports app.alert, app.launchURL, etc.)

    Simple usage via command line

    Built with Python and PyPDF2

#### Usage
##### 1. Install Dependencies

Ensure Python 3.8+ is installed, then run:
```bash
pip install -r requirements.txt
```
##### 2. Prepare Files
Create or choose an input PDF file (e.g. input.pdf)
Create a JavaScript file (e.g. script.js) containing code like:
```python
app.alert("your alert");
app.launchURL("https://example.com", true);
```
##### 3. Run Script

python embed_js.py input.pdf script.js output.pdf

After running, output.pdf will contain JavaScript that runs when opened in a compatible viewer (e.g., Adobe Acrobat).
Compatibility Notes

    Most JavaScript code only runs in Adobe Acrobat Reader. Browsers don't support link redirect and lightweight viewers (like Evince or Preview) often ignore JS.

    Only the first executable line may trigger in some environments. For best results, combine statements into one line or test on Acrobat.

##### Example
```bash
python embed_js.py resume.pdf payload.js infected_resume.pdf
```
