# IngestParserTest
Simple utility that uses ADSIngestParser to parse publisher metadata into Ingest_Data_Model json


# Create an environment
Using anaconda, create a python3.8 virtual environment:

```
anaconda_activate ; python -m venv venv ; anaconda_deactivate ; source venv/bin/activate.csh
python -m pip install -r requirements.txt
```

# Parse an input metadata file into Ingest_Data_Model JSON

```
python run.py -f input.xml -t [TYPE] # [TYPE] one of 'jats', 'nlm', 'dc', 'cr', 'elsevier'
```

If successful, the file will be written to `./output/input.xml.json`
