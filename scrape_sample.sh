# bash scrape.sh [url] [outfile]
# The header you need is the cookie (e.g. -H 'Cookie: __cf...')
curl "$1" --max-time 30 -L -H 'paste the cookie header here (do NOT erase the single quotes)' -w %{http_code} -o "$2"

