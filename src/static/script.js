var tagform = document.getElementById("tagform");

function add(){
  var newField = document.createElement("input");
  newField.setAttribute("id","tag_id");
  newField.setAttribute("type","text");
  newField.setAttribute("name","tag_name");
  newField.setAttribute("size",60);
  newField.setAttribute("minsize",3);
  newField.setAttribute("placeholder","Tag");
  newField.setAttribute("required","");
  tagform.appendChild(newField);
}

function remove(){
  var input_tags = tagform.getElementsByTagName("input");
  if(input_tags.length > 1) {
    tagform.removeChild(input_tags[(input_tags.length) - 1]);
  }
}