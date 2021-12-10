
{/* <script src="home_handler.js"></script> */}
{/* <link rel="stylesheet" href="http://cdn.graphalchemist.com/alchemy.min.css"></link> */}

{/* <script type="text/javascript" src="http://cdn.graphalchemist.com/alchemy.min.js"></script> */}
{/* <script src="jquery-3.6.0.min.js"></script> */}
console.log('AAAAAAAAAAAAAAAAAAAA')

chrome.storage.sync.get(
        ["selection_text", "selection_context", "url"], function (obj) {
    console.log(obj);
    items = obj
    console.log(items)
    let selection_text = items.selection_text
    let selection_context = items.selection_context
    let page_url = items.url

    console.log([selection_text, selection_context, page_url])



    selection_text_element = document.getElementById("highlighted_word")
    preamble_element = document.getElementById("preamble_element")

    context_element = document.getElementById("context_element")
    keyword_element = document.getElementById("keyword_element")
    context_heading = document.getElementById("context_heading")

    entitiy_name_element = document.getElementById("entity_element")
    entitiy_description_element = document.getElementById("definition_element")
    entity_image_element = document.getElementById("entity_image_element")
    nearest_neighbours_div = document.getElementById("nearest_neighbours_div")

    selection_text_element.innerText = selection_text

    console.log('0000000000000000')

    let request_json = {"selection_text": selection_text, "selection_context": selection_context, "page_url": page_url}
    let request_string = JSON.stringify(request_json)

    $.post("http://127.0.0.1:5667/receiver1", request_string, function(data){ console.log(data);
        // selected_text_element.innerHTML = data;
        response_json = JSON.parse(data)
        console.log(response_json)
        console.log('VVVVVVVVVV')

        if(response_json.entity_name.length > 0){
            entitiy_name_element.innerText = response_json.entity_name;
            entitiy_name_element.href = response_json.entity_url;
            preamble_element.innerText = "The nearest entity is - ";
        }
        else{
            entitiy_name_element.innerText = "We couldn't link this entity ╮(╯ _╰ )╭";
        }

        if(response_json.entity_context.length > 0){
            context_heading.innerText = "Context"
            keyword_element.innerText = response_json.entity_context
            context_element.innerText = selection_context;
        }

        if(response_json.entity_description.length > 0){
            entitiy_description_element.innerText = response_json.entity_description;
        }
        else{
            entitiy_description_element.innerText = "(⌣́_⌣̀)";
        }

        if(response_json.image_url.length > 0){
        let img = document.createElement("img");
        img.onload = function (event)
        {
            // console.log("natural:", img.naturalWidth, img.naturalHeight);
            console.log("width,height:", img.width, img.height);
            entity_image_element.style.height = img.height.toString + 'px'
            // console.log("offsetW,offsetH:", img.offsetWidth, img.offsetHeight);
        }
        img.src = response_json.image_url
        img.id = "entity_image"
        entity_image_element.appendChild(img)

        // entity_image_element.innerHTML = '<img src=' + '"' + response_json.image_url + '"' + ' alt="image" loading="lazy" id="entity_image">' ;
        // console.log(document.getElementById('entity_image').height)
        // entity_image_element.style.height = document.getElementById('entity_image').height
        // entity_image_element.height = 1000000000000
        }
        else{
            
        }
        // console.log('ffffffffffffff', typeof(response_json.entity_neighbours))
        if(typeof(response_json.entity_neighbours) != "string"){
            
            console.log(response_json.entity_neighbours)

            var nodes = [{ id: 0, label: response_json.entity_name }]
            var edges = []

            id = 1

            for(var i=0; i<response_json.entity_neighbours.length; i++){
                current_item = response_json.entity_neighbours[i]
                nodes.push({"id": id, "label": current_item.relation.name})
                edges.push({from: 0, to: id})
                id +=1
                

                nodes.push({"id": id, "label": current_item.tail.name})
                edges.push({from: id-1, to: id})
                id += 1
                
            }

            nodes = new vis.DataSet(nodes)
            edges = new vis.DataSet(edges)

            var container = document.getElementById("mynetwork");
            var data = {
            nodes: nodes,
            edges: edges,
            };
            var options = {};
            var network = new vis.Network(container, data, options);

            }
            else{
                
            }

            if(response_json.entity_id.length > 0){

                $.post("http://127.0.0.1:5667/receiver2", response_json.entity_name, function(data){ 
                
                    if(data.length > 0){
                        let nn_json = JSON.parse(data)
                        console.log(data);

                        let nn_para = document.createElement("p");

                        let nn_heading = document.createElement("h3")
                        nn_heading.style = "text-align:center padding:8px padding-bottom:8px;"
                        nn_heading.innerText = "Similar entities you might be interested in"
                        nn_para.appendChild(nn_heading)
                
                        for(i=0;i<nn_json.names.length;i++){
                            let nn_item = document.createElement("a")
                            nn_item.style.color = "blue"
                            nn_item.style.textDecoration = "underline"
                            nn_item.innerText = nn_json.names[i];
                            nn_item.href = nn_json.urls[i]
                            nn_item.style.padding = "5px"
                            nn_para.append(nn_item)
                        }
                        console.log(nn_para)
                        nearest_neighbours_div.align = "center"
                        nearest_neighbours_div.appendChild(nn_para)
                    }
  
                }
                );
            }
                    
    });
})

// document.getElementById("highlighted_word_div")
//
// document.getElementById("highlighted_word_div")
//
// document.getElementById("highlighted_word_div")


// alert(items)