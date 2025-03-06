### What this mini project is about?

I take a lot of notes in class. <br/>
Unfortunately, the space available for note-taking on lecture slides is very limiting. <br/>
Therefore, I decided to create a small python program which allows me to do the following: <br/>


1. takes in one or more PDF files. For each PDF file: <br/>
2. add extra space (see `blankpage.pdf`) to the right hand side of every PDF page. <br/>
3. save the modified PDF as a new PDF file. <br/>


You may replace `blankpage.pdf` with any other draft paper  <br/>
• but it need to have portrait orientation must be A4 sized. <br/>
• and you need to name your draft paper as blankpage.pdf. <br/>


You can use this pdf merger in two ways: <br/>
method 1: In `editor.py`, specify a working directory and a PDF file name, then hit run to begin the merge process. <br/>
method 2: In `main.py`, click run, then select multiple PDF files from the same directory to begin the merge process. <br/>


### Make sure you have the right tools before you run the code.

1. Create a virtual environment (venv) if it doesn’t exist: `python3 -m venv venv`
2. Activate virtual environment
    * Windows: `venv\Scripts\activate` in CMD or `venv\Scripts\Activate.ps1` in PowerShell
    * Mac/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Check installed packages: `pip list`