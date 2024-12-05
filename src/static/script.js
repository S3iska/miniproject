var tagform = document.getElementById("tagform");

function add(){
  var newField = document.createElement("input");
  newField.setAttribute("id","tag_id");
  newField.setAttribute("type","text");
  newField.setAttribute("name","tag_name");
  newField.setAttribute("size",60);
  newField.setAttribute("minlength",3);
  newField.setAttribute("placeholder","Tag");
  newField.setAttribute("required","");
  tagform.appendChild(newField);
}


function addTag(button){

  var existingField = document.querySelector("#tag_id");
  var buttonText = button.textContent || button.innerText;

  if (existingField && existingField.value === "") {
    existingField.value = buttonText;
  } else {
    var newField = document.createElement("input");

    newField.setAttribute("id", "tag_id");
    newField.setAttribute("type", "text");
    newField.setAttribute("name", "tag_name");
    newField.setAttribute("size", 60);
    newField.setAttribute("minlength", 3);
    newField.setAttribute("placeholder", "Tag");
    newField.setAttribute("required", "");
    newField.value = buttonText;
    tagform.appendChild(newField);
  }
}


function remove(){
  var input_tags = tagform.getElementsByTagName("input");
  if(input_tags.length > 1) {
    tagform.removeChild(input_tags[(input_tags.length) - 1]);
  }
}


function hide_error_box() {
  document.getElementById("error_box").style.display = "none";
}
setTimeout(hide_error_box, 5000)


function showForm() {
  document.getElementById("articleForm").style.display = "none";
  document.getElementById("inproceedingsForm").style.display = "none";
  document.getElementById("bookForm").style.display = "none";

  var selectedValue = document.getElementById("typeSelect").value;

  if (selectedValue === "article") {
      document.getElementById("articleForm").style.display = "block";
  } else if (selectedValue === "inproceedings") {
      document.getElementById("inproceedingsForm").style.display = "block";
  } else if (selectedValue === "book") {
      document.getElementById("bookForm").style.display = "block";
  }
}