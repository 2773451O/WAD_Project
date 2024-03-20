function previewImage(event) {
    var input = event.target;
    var reader = new FileReader();
    var placeholderPhoto = document.getElementById('placeholderPhoto');

    reader.onload = function() {
        var img = document.createElement('img');
        img.src = reader.result;
        img.style.width = '200px';
        img.style.height = '200px';

        document.getElementById('imagePreview').innerHTML = '';
        document.getElementById('imagePreview').appendChild(img);
    };

    reader.readAsDataURL(input.files[0]);
    
    placeholderPhoto.style.display = 'none';
    
}
var images = ['carrots.png', 'chickencurry.png', 'pasta.png', 'carbonara.png','lasanga.png'];

var index = 0; 
var timer; 

function changeImageHomepage() {
    var image = document.getElementById('home_pictures');
    image.src = '/media/'+images[index]; 
    index = (index + 1) % images.length; 
}

timer = setInterval(changeImageHomepage, 5000);

// Not used but useful to have set up
function stop() {
    clearInterval(timer);
}

