/* How many times checkbox is ticked off */
let count = 0;

/* Runs when user checks/unchecks a task */
function check_me(input_id) {
  var checked_input = document.querySelector("input[id='" + input_id + "']");
  var checked_label = document.querySelector("label[for='" + input_id + "']");
  
  /* Bunny weather image*/
  var status_image = document.getElementById("status-image");

  //* Changes bunny gif based on tasks ticked */
  function update_image(count) {
    if (count >= 3) {
      // 3+ tasks = sunny 
      status_image.src = "/static/images/sunny.gif";
    } else if (count == 2) {
      // 2 tasks = windy
      status_image.src = "/static/images/windy.gif";
    } else {
      // 0-1 tasks = rainy (starting gif)
      status_image.src = "/static/images/rainy.gif";
    }
  }
  
  // if task is checked off
  if (checked_input.checked) {
    
    // Strikes through the ticked item
    checked_label.style.textDecoration = "line-through";
    /* Add one on to a count if checked, the count should change the hero image */
    count += 1;
    console.log(count);
    
  } else {
    /* If task is unchecked, remove strikethrough, 
    also subtract 1 from count to change hero image */
    checked_label.style.textDecoration = "";
    count -= 1;
    console.log(count);
  }

  // Update hero image gif based on count
  update_image(count);

  /* Done button also changes colour once checkbox is checked. */
  var btn = document.getElementById("remove_btn");

  btn.value = "Done";
  btn.style.color = "#202020";
  btn.style.backgroundColor = "#A5BA5C";
  btn.style.cursor = "pointer";
}
