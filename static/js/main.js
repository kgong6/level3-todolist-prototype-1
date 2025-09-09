/* When task is checked off, strike-through*/
function check_me(input_id){
  var checked_input = document.querySelector("input[id=" + input_id + "]");
  var checked_label = document.querySelector("label[name=" + input_id + "]");

  if (checked_input.checked){
    checked_label.style.textDecoration = "line-through";
  }

  else {
    checked_label.style.textDecoration = "";
  }
    
  
/* Done button also changes colour once checkbox is checked. */
  var btn = document.getElementById("remove_btn");

  btn.value = "Done";
  btn.style.color = "#FFFFFF";
  btn.style.backgroundColor = "#A5BA5C";
  btn.style.cursor = "pointer";

  
}



