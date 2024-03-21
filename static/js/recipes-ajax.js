$(document).ready(function() {
    $('#like_btn').click(function() {
        var recipeIdVar;
        recipeIdVar = $(this).attr('data-recipeid');
        $.get('/recipes/like_recipe/',
            {'recipe_id': recipeIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });
});