var tagform = document.getElementById("tagform");
let isModified = false;  // Flag to track if the form has been modified


function add(){
  isModified = true;
  
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

  isModified = true;

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
  isModified = true;
  button.parentElement.remove();
}


function hide_error_box() {
  document.getElementById("error_box").style.display = "none";
}
setTimeout(hide_error_box, 5000)


function showForm() {
  isModified = true;

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


function selectForm(type) {
    selector = document.getElementById("typeSelect")
    if (type === "article") {
        selector.value = "article";
    } else if (type === "inproceedings") {
        selector.value = "inproceedings";
    } else if (type === "book") {
        selector.value = "book";
    }
    showForm()
}


document.addEventListener('DOMContentLoaded', function () {
  const cancelButton = document.querySelector('button.btn-secondary');
  let userConfirmedNavigation = false;

  if (cancelButton) {
    cancelButton.addEventListener('click', function (event) {
      handleNavigation(event);
    });

    const confirmButtons = document.querySelectorAll('button[type="submit"]'); // Multiple buttons
    if (confirmButtons) {
        confirmButtons.forEach(confirmButton => {
            confirmButton.addEventListener('click', function () {
                isModified = false;
                window.removeEventListener('beforeunload', beforeUnloadHandler);
            });
        });
    }
    
  }

  window.addEventListener('beforeunload', function (event) {
    if (isModified && !userConfirmedNavigation) {
      event.preventDefault();
      event.returnValue = ''; // Required for some browsers
      return ''; // Required for some browsers
    }
    userConfirmedNavigation = false; // Reset if the user stays on the page
  });

  // Add listener for popstate event (back/forward buttons)
  window.addEventListener('popstate', function(event) {
    if (isModified) {
      handleNavigation();
    }
  });

  function handleNavigation(event) {
      if (isModified) {
          const userConfirmed = confirm('You have unsaved changes. Do you really want to leave this page?');
          if (!userConfirmed) {
              if (event) { // Prevent navigation only if the event exists (e.g., button click)
                  event.preventDefault();
              }
          } else {
              userConfirmedNavigation = true;
              window.location.href = '/';
          }
      } else {
          window.location.href = '/';
      }
  }
  
});
