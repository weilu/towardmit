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

These headers can be found by doing the following.

(instructions are with the Chrome or Chromium web-browser, and tested using Linux & MacOS)

1. Open your edX dashboard, logging in as necessary
2. Open 'Developer Tools', which is a sub-menu item from 'More tools' in the menu
3. Choose the 'Network' tab in the Developer pane
4. Reload the dashboard web-page
5. Using the first entry in the 'Network' tab, named 'dashboard', open up the context (right-click) menu and choose 'Copy as cURL'
6. Using a text editor, copy all the '-H' options (which will follow the "curl 'https://courses.edx.org/dashboard'"), but DO NOT copy any option which will compress the output (e.g. "-H 'Accept-Encoding: gzip, deflate, br'" and "--compressed". There will be many lines of '-H' options!
7. Copy the required '-H' options into your scrape.sh file, replacing '[your request headers]'

### Executing the script

```bash
python scrape.py
```

The generated quiz html files can be found in your `out` directory
