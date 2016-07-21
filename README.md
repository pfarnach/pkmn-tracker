Uses Python 3.5

Start up a virtual environment (recommended)

Run `pip install -r requirements.txt`

Run `curl 'https://pokevision.com/map/data/45.51933087670564/-122.67473459243774' | python catchem.py`

To post to the Slack webhook:
Run  curl 'https://pokevision.com/map/data/45.518729484823304/-122.67571091651915' | python3 catchem.py | curl -X POST -d @- https://hooks.slack.com/services/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
