from flask import Flask, request
from flask_cors import CORS, cross_origin
from wikipedia2vec import Wikipedia2Vec
import json
import spacy
import requests
from wikidata.client import Client
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import spacy_dbpedia_spotlight
import pytextrank
import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup
nlp = spacy.load('en_core_web_lg')

nlp.add_pipe('textrank')

client = Client()

nlp2 = spacy.load('en_core_web_lg')
nlp2.add_pipe('dbpedia_spotlight')

wikipedia2vec_path = '../enwiki_20180420_win10_300d.pkl'


# wiki2vec = Wikipedia2Vec.load(wikipedia2vec_path)
# e = wiki2vec.get_entity('House (TV series)')
#
# similar = wiki2vec.most_similar(e, 5)
# print(str(type(similar[0][0])))
# similar = [x[0].title for x in similar[1:] if 'Entity' in str(type(x[0]))]
#
app = Flask(__name__)

CORS(app)

@app.route("/")
def hello():
    return "Hi there"

# sia = SIA()
#
@app.route('/receiver1', methods = ['POST'])
def worker1():

    data = request.get_data()

    data = data.decode('UTF8')

# def worker1(data):
    data = json.loads(data)

    response_dict = {"image_url": "",
                     "entity_name": "",
                     "entity_url": "",
                     "entity_description": "",
                     "entity_neighbours": {}}

    selection_text = data["selection_text"].strip()
    selection_context = data["selection_context"].strip()
    page_url = data["page_url"].strip()

    wikipedia_id = ""
    wikipedia_url_main = ""
    wikipedia_summary = ""
    wikipedia_title = ""
    wikipedia_image = ""
    wikibase_id = ""
    wikibase_graph = ""
    entity_context = ""

    url = page_url
    html = urlopen(url).read()
    full_web_page_text = BeautifulSoup(html, 'html.parser').get_text()
    
    new_context = ''

    doc = nlp(full_web_page_text)
    for p in doc._.phrases:
        if len(new_context) <= 50:
            new_context += p.text + ' '

    entity_context = new_context
    selection_context = entity_context + selection_context

    index = selection_context.find(selection_text)

    print('zx')

    if index > -1:
        print('xz')
        # def work()
        spans = []
        request_json = {"text": selection_context, "spans": spans}
        response_text = requests.post("http://localhost:5555", json=request_json).text
        response_list = json.loads(response_text)

        print('ooooooooooooooooooo')
        for item in response_list:
            if item[0] == index:

                wikipedia_id = item[2]
                wikipedia_url_main = "https://en.wikipedia.org/wiki/{}".format(wikipedia_id)
                wikipedia_url = "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(wikipedia_id)

                try:
                    wikipedia_result = json.loads(requests.get(wikipedia_url).text)
                except:
                    pass

                try:
                    wikipedia_title = wikipedia_result["displaytitle"]
                except:
                    pass

                try:
                    wikipedia_summary = wikipedia_result["extract"]
                except:
                    pass

                try:
                    wikipedia_image = wikipedia_result["thumbnail"]["source"]
                except:
                    pass

                try:
                    wikibase_id = wikipedia_result["wikibase_item"]
                except:
                    pass

                print(wikibase_id)
                if len(wikibase_id) > 0:
                    try:
                        entity = client.get(wikibase_id, load=True)

                        # er_pairs = entity.items()[:7]
                        try:
                            er_pairs = entity.lists()[:10]
                        except:
                            er_pairs = entity.lists()
                            er_pairs = [x for x in er_pairs][:10]
                        print("\n\n\n\nhhhhh\n\n", er_pairs)
                        pairs = []
                        for p in er_pairs:
                            pair_reln = p[0]
                            pair_en = p[1]
                            try:
                                pair_reln = {"url": "https://www.wikidata.org/wiki/Property:{}".format(pair_reln.id),
                                             "name": pair_reln.label.texts['en']}
                                pair_en = {"url": "https://www.wikidata.org/wiki/{}".format(pair_en[0].id),
                                             "name": pair_en[0].label.texts['en']}
                                pairs.append({"relation": pair_reln, "tail": pair_en})
                            except:
                                pass
                        wikibase_graph = pairs
                    except:
                        pass

                break

        # work()
        print('-----------------d--')
        if len(wikipedia_title) == 0:
            print('-------------------')
            a = nlp2(selection_text)

            b = [(ent.text, ent.label_, ent.kb_id_) for ent in a.ents]

            print(b)

            for x, y, z in b:
                if x == selection_text:
                    print("dbpedia ", x)
                    response_list = [(index, 0, z.split('/')[-1])]
                    print('ooooooooooooooooooo')
                    for item in response_list:
                        if item[0] == index:

                            wikipedia_id = item[2]
                            wikipedia_url_main = "https://en.wikipedia.org/wiki/{}".format(wikipedia_id)
                            wikipedia_url = "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(wikipedia_id)

                            try:
                                wikipedia_result = json.loads(requests.get(wikipedia_url).text)
                            except:
                                pass

                            try:
                                wikipedia_title = wikipedia_result["displaytitle"]
                            except:
                                pass

                            try:
                                wikipedia_summary = wikipedia_result["extract"]
                            except:
                                pass

                            try:
                                wikipedia_image = wikipedia_result["thumbnail"]["source"]
                            except:
                                pass

                            try:
                                wikibase_id = wikipedia_result["wikibase_item"]
                            except:
                                pass

                            print(wikibase_id)
                            if len(wikibase_id) > 0:
                                try:
                                    entity = client.get(wikibase_id, load=True)

                                    # er_pairs = entity.items()[:7]
                                    try:
                                        er_pairs = entity.lists()[:10]
                                    except:
                                        er_pairs = entity.lists()
                                        er_pairs = [x for x in er_pairs][:10]
                                    print("\n\n\n\nhhhhh\n\n", er_pairs)
                                    pairs = []
                                    for p in er_pairs:
                                        pair_reln = p[0]
                                        pair_en = p[1]
                                        try:
                                            pair_reln = {
                                                "url": "https://www.wikidata.org/wiki/Property:{}".format(pair_reln.id),
                                                "name": pair_reln.label.texts['en']}
                                            pair_en = {"url": "https://www.wikidata.org/wiki/{}".format(pair_en[0].id),
                                                       "name": pair_en[0].label.texts['en']}
                                            pairs.append({"relation": pair_reln, "tail": pair_en})
                                        except:
                                            pass
                                    wikibase_graph = pairs
                                except:
                                    pass

                            break
                break

    response_dict = {"image_url": wikipedia_image,
                     "entity_id": wikipedia_id.replace('_', ' '),
                     "entity_name": wikipedia_title,
                     "entity_context": entity_context,
                     "entity_url": wikipedia_url_main,
                     "entity_description": wikipedia_summary,
                     "entity_neighbours": wikibase_graph}
    print(response_dict)
    return json.dumps(response_dict)

@app.route('/receiver2', methods = ['POST'])
def worker2():

    data = request.get_data()

    entity_name = data.decode('UTF8')

    # try:

    wiki2vec = Wikipedia2Vec.load(wikipedia2vec_path)
    e = wiki2vec.get_entity(entity_name)

    similar = wiki2vec.most_similar(e, 10)
    print(str(type(similar[0][0])))
    similar = [x[0].title for x in similar if 'Entity' in str(type(x[0]))]

    similar_with_ = [x.replace(' ', '_') for x in similar]
    similar_urls = ['https://en.wikipedia.org/wiki/' + x for x in similar_with_]

    print(similar, similar_urls)

    return json.dumps({"names": similar, "urls": similar_urls})
    # except:
    #     return ""

# worker1(json.dumps({"selection_text": "France",
#                     "selection_context": "I like France",
#                    "page_url": "https://en.wikipedia.org/wiki/Germany"}))

#
#
# @app.route('/receiver2', methods = ['POST'])
# def worker2():
#
#         data = request.get_data().lower()
#
#         connection = MongoClient()
#
#         db = connection["test_db"]
#
#         collection = db["tweets"]
#
#         db_record = db["tweets"].find_one({"ne_list" : data})
#
# 	if db_record == None:
#                 return "No records found"
#
#
#         return str(db_record["sentiment"]["compound"])
#
# @app.route('/receiver3', methods = ['POST'])
# def worker3():
#
#         data = request.get_data().lower()
#
#         connection = MongoClient()
#
#         db = connection["news_db"]
#
#         collection = db["news_overall"]
#
#         db_record = db["news_overall"].find_one({"ne_list" : data})
#
# 	if db_record == None:
#                 return "No records found"
#
#         return db_record["text_body"]
#
#
# @app.route('/receiver4', methods = ['POST'])
# def worker4():
#
#         data = request.get_data().lower()
#
#         connection = MongoClient()
#
#         db = connection["news_db"]
#
#         collection = db["news_overall"]
#
#         db_record = db["news_overall"].find_one({"ne_list" : data})
#
# 	if db_record == None:
#                 return "No records found"
#
#
#         return str(sia.polarity_scores(db_record["text_body"])["compound"])
#

if __name__ == "__main__":
#     app.run(host="167.99.83.32", port=443, debug=True)
    app.run(host="127.0.0.1", port=5667, debug=True)
