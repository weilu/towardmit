## Toward MIT

Scripts to scrape quiz content off Edx, remove answers & consolidate to a single html for print-out/practice/review purposes.

### Requirements
This project requires:

- Python 3, and
- a Unix based operation system (e.g. MacOS or Linux). Sorry Windows users, you deserve a better operating system.

### Preparation

Get the source code onto your computer:

if you have git:

```bash
git clone git@github.com:weilu/towardmit.git
```

Otherwise click the green button "Clone or download" on this page, click "Download ZIP". Then unzip the file you downloaded.

Then open the Terminal app (MacOS) or the equivalent of a console thing on other unix systems and executing the following commands:

```bash
cd towardmit
pip install -r requirements.txt
cp scrape_sample.sh scrape.sh
```

### Editing the scrape.sh file

In the scrape.sh file, the [your request headers] needs to be replaced by request headers obtained from your browser.
The request headers will be a series of '-H' options, which includes your edX login details.
The header you need to scrape the courses are the cookies, which can be detected because they start with the work Cookie (e.g. -H 'Cookie: __cf...').

These headers can be found by doing the following.

(instructions are with the Chrome or Chromium web-browser, and tested using Linux & MacOS)

1. Open your edX dashboard, logging in as necessary
2. Open 'Developer Tools', which is a sub-menu item from 'More tools' in the menu
3. Choose the 'Console' tab in the Developer pane
4. Enter the following command 'alert( document.cookie );' (only the text inside the single quotes)
5. Copy the text in the alert window
6. Paste the required header into your scrape.sh file inside the single quotes

### Editing the scrape.py file

You may need to edit the scrape.py file to adjust for the version of the course you are enrolled to. This can be achieved by doing the following.

1. Open the scrape.py file in a text editor.
2. Find the courses variable inside the "\__main__" function.
3. Adjust to the the courses you want to scrape. You have to be registered for that run of the course, which is denoted by the letters following the (+) 1T2020 -> term (1T for spring, 2T for summer and 3T for fall) and the year you enrolled. You can also check this information in the URL of any of your courses.


### Executing the script

```bash
python scrape.py
```

The generated quiz html files can be found in your `out` directory
