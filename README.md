## Toward MIT

Scripts to scrape quiz content off Edx, remove answers & consolidate to a single html for print-out/practice/review purposes.

This project requires python 3.

```
pip install -r requirements.txt
# grab request headers off chrome dev console & fill out scrape.sh
cp scrape_sample.sh scrape.sh
python scrape.py
```

The generated quiz html files can be found in your `out` directory

### Editing the scrape.sh file

In the scrape.sh file, the [your request headers] needs to be replaced by your headers!
This will be a series of '-H' options, which includes your edX login details.

These headers can be found by doing the following.

(instructions are with the Chromium web-browser, and tested using Linux)

1. Open your edX dashboard, logging in as necessary
2. Open 'Developer Tools', which is a sub-menu item from 'More tools' in the menu
3. Choose the 'Network' tab in the Developer pane
4. Reload the dashboard web-page
5. Using the first entry in the 'Network' tab, named 'dashboard', open up the context (right-click) menu and choose 'Copy as cURL'
6. Using a text editor, copy all the '-H' options (which will follow the "curl 'https://courses.edx.org/dashboard'"), but DO NOT copy any option which will compress the output (e.g. "-H 'Accept-Encoding: gzip, deflate, br'" and "--compressed". There will be many lines of '-H' options!
7. Copy the required '-H' options into your scrape.sh file, replacing '[your request headers]'
