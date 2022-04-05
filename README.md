# Propaganda Detection

## Installation and Dependencies
Install the dependencies using
```
cd kv16
pip install -r requirements.txt
```

You'll also need the following
```
python -m spacy download en_core_web_lg
```
## Running the code

The data must be in `../data`
A list of the options my code takes is in `utils/options.py`

To run and evaluate my settings 

All of my configurations can be run using
```
python3 -u bart.py --model-name nghuyong/ernie-2.0-large-en --train-epoch 10 --enhance F
python3 -u bart.py --model-name roberta-large --train-epoch 24 --enhance F
python3 -u bart.py --model-name roberta-base --train-epoch 11 --enhance F
python3 -u bart.py --model-name facebook/bart-large --train-epoch 10 --enhance F
python3 -u bart.py --model-name facebook/bart-base --train-epoch 10 --enhance F

python3 -u bart.py --model-name nghuyong/ernie-2.0-large-en --train-epoch 10 --enhance T
```

