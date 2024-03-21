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

document.addEventListener("DOMContentLoaded", function() {

    const logoImage = document.getElementById('logoImage');
    const profilePictures = document.querySelectorAll('.recipe-picture');

    setTimeout(function() {
        logoImage.style.display = 'none'; 
        startSlideshow();
    }, 5000);

    function startSlideshow() {
        let currentIndex = 0;
        profilePictures[currentIndex].style.display = 'block';

        function showNextPicture() {
            profilePictures[currentIndex].style.display = 'none';
            currentIndex = (currentIndex + 1) % profilePictures.length;
            profilePictures[currentIndex].style.display = 'block';
        }
        setInterval(showNextPicture, 5000);
    }
});