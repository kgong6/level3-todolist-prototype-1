/* number of times checkbox is ticked off */
var count = 0;
var status_image_path = "rainy.gif";

/* When task is checked off, strike-through*/
function check_me(input_id){
  /*
this function should put a line through the ticked item
add one on to a count
the count should change the hero image
  */

  //* Hero image changing as tasks get checked off*/
  function update_Image(count) {
    if (count >= 3) {
      status_image_path = 'sunny.gif';
    } else if (count == 2 ) {
      status_image_path = 'windy.gif';
    } else {
      status_image_path = 'rainy.gif'; 
    }
  }
  
  var checked_input = document.querySelector("input[id='" + input_id + "']");
  var checked_label = document.querySelector("label[name='" + input_id + "']");
  


  if (checked_input.checked){
    checked_label.style.textDecoration = "line-through";
    count += 1;
    console.log(count)
    update_Image(count)
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





