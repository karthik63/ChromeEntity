# Timeline Summarization using tilse with enhancements

The Project Presentation Video and Documentation are among the files in my repository.

## Installation and Dependencies
Install tilse using
```
pip install tilse
```
For some of my additional functionality you'll also need the following
```
python -m spacy download en_core_web_lg
pip install transformers[torch]

```
## Running the code
The data along with many pre-processed objects are in `tilse/bin/timeline_17`
all of my configuration files are in `tilse/bin/`

To run and evaluate my settings 

```
python3 -u predict-timelines types.json
python3 -u predict-timelines events.json
python3 -u predict-timelines args.json
python3 -u predict-timelines outgoing.json

```



