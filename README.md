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
│  ├─ __init__.py
├─ elapp.wsgi
├─ html/
├─ index.html
front_end/
├─ src/
│  ├─ vis-network.min.js
│  ├─ app.js
│  ├─ background.html
│  ├─ d3.v7.min.js
│  ├─ handler.js
│  ├─ home.css
│  ├─ package.json
│  ├─ home.html
│  ├─ home_handler.js
│  ├─ jquery-3.6.0.min.js
├─ images/
│  ├─ icon.png
├─ manifest.json
```

## Instructions to run the extension
### Step 1
Clone [end2end entity linking](https://github.com/dalab/end2end_neural_el) and follow the instructions to run a HTTP server using `code/server.py`

### Step 2
Run 
```
python ChromeEntity/back_end/__init__.py
```
To start a decond HTTP server


### Step 3
Go to chrome://extensions/ and load `ChromEntity/front_end` as a new extension.

