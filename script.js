
  // Array of image URLs to preload
var imageUrls = [
    "imgs/DSC07452.jpeg",
    "imgs/DSC07512.jpeg",
    "imgs/DSC07531.jpeg"
    // Add more image URLs as needed
  ];
  
  // Function to optimize image size
  function optimizeImages(urls) {
    urls.forEach(function(url) {
      var img = new Image();
      img.src = url;
      
      img.onload = function() {
        var canvas = document.createElement("canvas");
        var ctx = canvas.getContext("2d");
  
        // Calculate the new width and height
        var maxWidth = 800; // Adjust as needed
        var maxHeight = 600; // Adjust as needed
        var width = img.width;
        var height = img.height;
        if (width > maxWidth || height > maxHeight) {
          if (width / maxWidth > height / maxHeight) {
            height *= maxWidth / width;
            width = maxWidth;
          } else {
            width *= maxHeight / height;
            height = maxHeight;
          }
        }
  
        // Set the canvas dimensions
        canvas.width = width;
        canvas.height = height;
  
        // Draw the image on the canvas
        ctx.drawImage(img, 0, 0, width, height);
  
        // Get the optimized data URL
        var optimizedDataUrl = canvas.toDataURL("image/jpeg", 0.7); // Adjust the compression quality (0.7 is 70% quality)
  
        // Replace the image source with the optimized data URL
        img.src = optimizedDataUrl;
      };
    });
  }
  
  // Call the optimizeImages function with your array of image URLs
  optimizeImages(imageUrls);
  
  $(document).ready(function() {
    $('.carousel').carousel();
  });