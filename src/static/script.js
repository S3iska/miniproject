var tagform = document.getElementById("tagform");

function add(){
  var tagEntry = document.createElement("div");
  tagEntry.classList.add("tag-entry", "d-flex", "align-items-center", "mb-2");

  var newField = document.createElement("input");
  newField.classList.add("tag_id");
  newField.type = "text";
  newField.name = "tag_name";
  newField.size = 60;
  newField.minLength = 3;
  newField.placeholder = "Tag";
  newField.required = true;
  
  var removeButton = document.createElement("button");
  removeButton.type = "button";
  removeButton.classList.add("btn", "btn-danger", "ms-2");
  removeButton.innerText = "Delete";
  removeButton.onclick = function() {
      remove(removeButton);
  };

  tagEntry.appendChild(newField);
  tagEntry.appendChild(removeButton);

  document.getElementById("tagform").appendChild(tagEntry);

}


function addTag(button){
  var tagEntry = document.createElement("div");
  tagEntry.classList.add("tag-entry", "d-flex", "align-items-center", "mb-2");

  var existingField = document.querySelector("#tag_id");
  var buttonText = button.textContent || button.innerText;

  if (existingField && existingField.value === "") {
    existingField.value = buttonText;
  } else {
    
    var newField = document.createElement("input");
    newField.classList.add("tag_id");
    newField.type = "text";
    newField.name = "tag_name";
    newField.size = 60;
    newField.minLength = 3;
    newField.placeholder = "Tag";
    newField.required = true;
    newField.value = buttonText;

    var removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.classList.add("btn", "btn-danger", "ms-2");
    removeButton.innerText = "Delete";
    removeButton.onclick = function() {
        remove(removeButton);
    };

    tagEntry.appendChild(newField);
    tagEntry.appendChild(removeButton);

    document.getElementById("tagform").appendChild(tagEntry);

  }
}


function remove(button) {
  button.parentElement.remove();
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