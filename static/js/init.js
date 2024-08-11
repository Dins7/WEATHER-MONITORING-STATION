(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space


// Array of background image URLs
const imageUrls = [
  'path_to_image1.jpg',
  'path_to_image2.jpg',
  'path_to_image3.jpg',
  // Add more image URLs as needed
];

// Function to set a random background image
function setRandomBackgroundImage() {
  // Get the element you want to set the background image for
  const bgElement = document.getElementById('bg-element');

  // Check if the element exists
  if (bgElement) {
      // Generate a random index based on the array length
      const randomIndex = Math.floor(Math.random() * imageUrls.length);

      // Get a random image URL from the array
      const randomImageUrl = imageUrls[randomIndex];

      // Set the background image of the element
      bgElement.style.backgroundImage = `url(${randomImageUrl})`;
  }
}

// Call the function to set a random background image when the page loads
window.addEventListener('load', setRandomBackgroundImage);
