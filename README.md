# Timeline Summarization using tilse with enhancements

## Installation and Dependencies
Install tilse using
```
pip install tilse
```
Tilse only works with spacy v2. `spacy==2.2.4` works well.
You might see an error where 'Perl-DB_File' is missing. You can download it manually using [this](https://centos.pkgs.org/7/centos-x86_64/perl-DB_File-1.830-6.el7.x86_64.rpm.html) link.

For some of my additional functionality you'll also need the following
```
python -m spacy download en_core_web_lg
pip install transformers[torch]
wget http://wikipedia2vec.s3.amazonaws.com/models/en/2018-04-20/enwiki_20180420_win10_100d.pkl.bz2
bzip2 -d enwiki_20180420_win10_100d.pkl.bz2
```
Most of my large files (data objects mainly) can be found [here](https://drive.google.com/drive/folders/1KCmFOLTVwSL2CYqkUEQlkw7MKQx_MU_L?usp=sharing).

## Running the code

The data along with the pre-processed objects must be in `tilse/bin/timeline_17`
All of my configuration files are in `tilse/bin/`

To run and evaluate my settings 

To run the baselines/IE enhancements, please edit line 61 of `bin/predict-timelines` to 
```
news_corpora[topic] = pickle.load(open(dumped_corpora_directrory + topic + ".corpus.obj", "rb"))
```
To run the the wikipedia entity vector enhancement, please edit thr line to say 
```
news_corpora[topic] = pickle.load(open(dumped_corpora_directrory + topic + ".wiki_corpus.obj", "rb"))
```
To run the the ERNIE enhancement, please edit thr line to say 
```
news_corpora[topic] = pickle.load(open(dumped_corpora_directrory + topic + ".new_corpus.obj", "rb"))
```

All of these object files can be found in my [drive](https://drive.google.com/drive/folders/1KCmFOLTVwSL2CYqkUEQlkw7MKQx_MU_L?usp=sharing). You can also generate them using `bin/get-and-preprocess-data`

The object files must be in `bin/timeline17/dumped_corpora`

All of my configurations can be run using
```
python3 -u predict-timelines types.json
python3 -u predict-timelines events.json
python3 -u predict-timelines args.json
python3 -u predict-timelines all.json
python3 -u predict-timelines outgoing.json

python3 -u predict-timelines ernie.json
python3 -u predict-timelines wiki.json
```
Please make sure to edit line 5 of the json file to include all the topics


