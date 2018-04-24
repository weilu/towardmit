# bash scrape.sh [url] [outfile]
curl "$1" --max-time 30 -L [your request headers] -w %{http_code} -o "$2"
