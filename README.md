# Chrome Entity Linker for Contextual Search and Linked Thinking

## Motivation
Often while browsing the web, we encounter an entity that we'd like to look up. This involves copy-pasting the word to a search engine and navigating to the article we want, which is often quite low on the search results because it is missing the specific context from the website we were browsing. We need to use the local context of the word/phrase as well as the context of the web page to perform entity linking. 

Also, vital to learning about a new entity quickly is the ability to put it in context using relations extracted from public knowledge bases and semantically nearby entities.

My chrome extension performs the following functions
1. Entity Linking using local + webpage context using a combination of neural [end2end entity linking](https://github.com/dalab/end2end_neural_el) and the [DBPedia spotlight API](https://www.dbpedia-spotlight.org/).
2. Displaying the local knowledge graph of the entity using WikiData
3. Extracting similar entities using Wikipedia2Vec embeddings

### Screenshots
<img src="https://user-images.githubusercontent.com/18640459/145547057-c8efa310-4922-40c0-a646-96853f5cddf3.png" width="400">

<img src="https://user-images.githubusercontent.com/18640459/145547077-0f4ec194-4232-405a-9aa5-f26245a1eb10.png" width="400">\

## Directory Structure
```
back_end/
├─ ELApp/
│  ├─ __init__.py (contains the back-end logic)
├─ elapp.wsgi
├─ html/
├─ index.html
front_end/
├─ src/
│  ├─ vis-network.min.js
│  ├─ app.js (content script with a listener)
│  ├─ background.html
│  ├─ d3.v7.min.js
│  ├─ handler.js (logic for adding context menu entry and handling click events)
│  ├─ home.css
│  ├─ package.json
│  ├─ home.html
│  ├─ home_handler.js (contains the bulk of the front-end logic)
│  ├─ jquery-3.6.0.min.js
├─ images/
│  ├─ icon.png
├─ manifest.json
```

## Instructions to run the extension
### Step 0
Clone the directory
```
git clone https://github.com/karthik63/ChromeEntity
cd ChromeEntity
```

### Step 1
Clone [end2end entity linking](https://github.com/dalab/end2end_neural_el) and follow the instructions to run a HTTP server using `code/server.py`. Use a manual threshhold of -0.4.

```
python -m gerbil.server --training_name=base_att_global  --experiment_name=paper_models  --persons_coreference_merge=True --all_spans_training=True --entity_extension=extension_entities --hardcoded_thr -0.4
```

### Step 2
Run a second HTTP server using the code in the `back_end` directory.
```
cd back_end/ELApp
python __init__.py
```

### Step 3
Go to chrome://extensions/ and load `ChromEntity/front_end` as a new extension.

Once the extension has been loaded and the two servers are running, you are good to go! You can right click and link any entity on any webpage.
