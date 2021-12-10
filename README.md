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
back_end/ <br />
├─ ELApp/ <br />
│  ├─ __init__.py <br />
├─ elapp.wsgi <br />
├─ html/ <br />
├─ index.html <br />
front_end/ <br />
├─ src/ <br />
│  ├─ vis-network.min.js <br />
│  ├─ app.js <br />
│  ├─ background.html  <br />
│  ├─ d3.v7.min.js  <br />
│  ├─ handler.js <br />
│  ├─ new_folder/ <br />
│  ├─ home.css <br />
│  ├─ package.json <br />
│  ├─ home.html <br />
│  ├─ home_handler.js <br />
│  ├─ jquery-3.6.0.min.js <br />
├─ images/ <br />
│  ├─ icon.png <br />
├─ manifest.json <br />

##Instructions to run the extension
###Step 1
Clone [end2end entity linking](https://github.com/dalab/end2end_neural_el) and 


