import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wad_Project.settings')

django.setup()
from recipes.models import Recipe, Category, User

def populate():
    recipes_data = [
        {
            'title': 'Spaghetti Bolognese',
            'categories': ['Easy'],
            'ingredients': '500g spaghetti\n400g minced beef\n1 onion, chopped\n2 cloves garlic, minced\n400g canned chopped tomatoes\n2 tbsp tomato paste\n1 tsp dried oregano\n1 tsp dried basil\nSalt and pepper to taste\nGrated Parmesan cheese, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. Cook spaghetti according to package instructions.\n2. In a large skillet, brown the minced beef over medium heat.\n3. Add chopped onion and garlic, and cook until softened.\n4. Stir in canned tomatoes, tomato paste, oregano, basil, salt, and pepper.\n5. Simmer for 15-20 minutes, stirring occasionally.\n6. Serve the sauce over cooked spaghetti, topped with grated Parmesan cheese.',
            'views': 100,
            'likes': 37,
            'image':"recipes/spag_bol.png"
        },
        {
            'title': 'Chicken Tikka Masala',
            'categories': ['Medium'],
            'ingredients': '500g chicken breast, diced\n200g plain yogurt\n2 tbsp tomato paste\n1 onion, finely chopped\n2 cloves garlic, minced\n1 tsp ground cumin\n1 tsp ground coriander\n1 tsp paprika\n1/2 tsp turmeric\n1/2 tsp cayenne pepper (adjust to taste)\nSalt and pepper to taste\n2 tbsp vegetable oil\nFresh cilantro, for garnish\nCooked rice, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. In a bowl, combine diced chicken, yogurt, tomato paste, chopped onion, garlic, and spices.\n2. Cover and marinate in the refrigerator for at least 1 hour, or overnight.\n3. Heat vegetable oil in a large skillet over medium-high heat.\n4. Add marinated chicken mixture and cook until chicken is browned and cooked through.\n5. Serve chicken tikka masala over cooked rice, garnished with fresh cilantro.',
            'views': 150,
            'likes': 45,
            'image':"recipes/chicken_tikka.png"
        },
        {
            'title': 'Beef Wellington',
            'categories': ['Hard'],
            'ingredients': '600g beef fillet\n200g mushrooms, finely chopped\n2 cloves garlic, minced\n2 tbsp butter\nSalt and pepper to taste\n500g puff pastry\n8 slices prosciutto\n1 egg, beaten\n2 tbsp olive oil\nMashed potatoes and steamed vegetables, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. Season beef fillet with salt and pepper.\n2. In a skillet, melt butter over medium heat. Add chopped mushrooms and garlic, and cook until mushrooms release their moisture.\n3. Transfer mushrooms to a plate and let cool.\n4. Lay out prosciutto slices on plastic wrap, overlapping slightly.\n5. Spread mushroom mixture evenly over prosciutto.\n6. Place beef fillet on top of mushroom-covered prosciutto and wrap tightly.\n7. Roll out puff pastry and place beef and prosciutto on top.\n8. Wrap puff pastry around beef, sealing edges tightly.\n9. Brush pastry with beaten egg.\n10. Bake in preheated oven at 200°C for 25-30 minutes, until pastry is golden brown.\n11. Let rest for 10 minutes before slicing.\n12. Serve beef Wellington with mashed potatoes and steamed vegetables.',
            'views': 200,
            'likes': 60,
            'image':"recipes/beef_wellington.png"
        },
        {
            'title': 'Chicken Parmesan',
            'categories': ['Medium'],
            'ingredients': '4 boneless, skinless chicken breasts\nSalt and pepper to taste\n1 cup all-purpose flour\n2 large eggs, beaten\n1 cup breadcrumbs\n1/2 cup grated Parmesan cheese\n2 cups marinara sauce\n1 cup shredded mozzarella cheese\nChopped fresh basil, for garnish',
            'author': 'Culinary_Carnival',
            'directions': '1. Preheat the oven to 200°C. Line a baking sheet with parchment paper.\n2. Season chicken breasts with salt and pepper.\n3. Dredge each chicken breast in flour, dip in beaten eggs, and coat with breadcrumbs mixed with Parmesan cheese.\n4. Place chicken breasts on the prepared baking sheet and bake for 20-25 minutes, until golden brown and cooked through.\n5. Spoon marinara sauce over each chicken breast and sprinkle with shredded mozzarella cheese.\n6. Return to the oven and bake for an additional 5-10 minutes, until the cheese is melted and bubbly.\n7. Garnish with chopped fresh basil before serving.',
            'views': 90,
            'likes': 30,
            'image':"recipes/chicken_parm.png"
        },
        {
            'title': 'Beef Stroganoff',
            'categories': ['Medium'],
            'ingredients': '500g beef sirloin, thinly sliced\nSalt and pepper to taste\n2 tbsp vegetable oil\n1 onion, thinly sliced\n200g mushrooms, sliced\n2 cloves garlic, minced\n2 tbsp all-purpose flour\n1 cup beef broth\n1 cup sour cream\n2 tbsp Dijon mustard\n1 tbsp Worcestershire sauce\nChopped fresh parsley, for garnish\nCooked egg noodles, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. Season beef slices with salt and pepper.\n2. Heat vegetable oil in a large skillet over medium-high heat.\n3. Add beef slices and cook until browned. Remove from skillet and set aside.\n4. In the same skillet, add sliced onion and mushrooms. Cook until softened.\n5. Add minced garlic and cook until fragrant.\n6. Sprinkle flour over the vegetables and cook, stirring constantly, for 1-2 minutes.\n7. Slowly pour in beef broth, stirring to combine.\n8. Return beef slices to the skillet and simmer for 5-10 minutes, until the sauce thickens.\n9. Stir in sour cream, Dijon mustard, and Worcestershire sauce.\n10. Cook for an additional 2-3 minutes, until heated through.\n11. Garnish with chopped fresh parsley and serve over cooked egg noodles.',
            'views': 85,
            'likes': 25,
            'image':"recipes/beef_stroganoff.png"
        },
        {
            'title': 'Sushi Rolls',
            'categories': ['Easy'],
            'ingredients': '4 nori sheets\n2 cups sushi rice, cooked\n1 cucumber, julienned\n1 avocado, sliced\n100g smoked salmon\nWasabi and pickled ginger, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. Place a nori sheet on a bamboo sushi mat.\n2. Spread a thin layer of sushi rice over the nori, leaving a border at the top.\n3. Arrange cucumber, avocado, and smoked salmon along the bottom edge of the nori.\n4. Roll the sushi tightly using the bamboo mat, applying gentle pressure as you roll.\n5. Seal the edge of the nori with a bit of water.\n6. Slice the sushi roll into bite-sized pieces using a sharp knife.\n7. Serve with wasabi and pickled ginger.',        
            'views': 80,
            'likes': 20,
            'image':"recipes/sushi_rolls.png"
        },
        {
            'title': 'Margherita Pizza',
            'categories': ['Easy'],
            'ingredients': 'Pizza dough\n1/2 cup pizza sauce\n1 cup shredded mozzarella cheese\nFresh basil leaves\nExtra virgin olive oil\nSalt and pepper to taste',
            'author': 'Culinary_Carnival',
            'directions': '1. Preheat the oven to the highest temperature (usually around 250°C) with a pizza stone inside.\n2. Stretch out the pizza dough into a circle on a floured surface.\n3. Spread pizza sauce evenly over the dough, leaving a small border.\n4. Sprinkle shredded mozzarella cheese over the sauce.\n5. Tear fresh basil leaves and scatter them over the cheese.\n6. Drizzle a little extra virgin olive oil over the pizza.\n7. Season with salt and pepper to taste.\n8. Carefully transfer the pizza onto the hot pizza stone.\n9. Bake for 8-10 minutes, until the crust is golden brown and the cheese is bubbly.\n10. Remove from the oven, slice, and serve hot.',
            'views': 95,
            'likes': 28,
            'image':"recipes/pizza.png"
        },
        {
            'title': 'Beef Bourguignon',
            'categories': ['Medium'],
            'ingredients': '1 kg beef chuck, cut into chunks\nSalt and pepper to taste\n2 tbsp olive oil\n200g bacon, diced\n2 onions, chopped\n2 carrots, sliced\n2 cloves garlic, minced\n2 tbsp all-purpose flour\n750ml red wine\n500ml beef broth\n2 tbsp tomato paste\n2 sprigs fresh thyme\n2 bay leaves\n200g mushrooms, halved\nChopped fresh parsley, for garnish',
            'author': 'Culinary_Carnival',
            'directions': '1. Season beef chunks with salt and pepper.\n2. Heat olive oil in a large Dutch oven over medium-high heat.\n3. Add bacon and cook until browned and crispy. Remove from the pot and set aside.\n4. In the same pot, add beef chunks and brown on all sides. Remove from the pot and set aside.\n5. Add chopped onions and carrots to the pot. Cook until softened.\n6. Add minced garlic and cook until fragrant.\n7. Sprinkle flour over the vegetables and cook, stirring constantly, for 1-2 minutes.\n8. Pour in red wine and beef broth, scraping the bottom of the pot to deglaze.\n9. Stir in tomato paste, thyme, and bay leaves.\n10. Return the beef and bacon to the pot. Bring to a simmer, then cover and cook over low heat for 2-3 hours, until the beef is tender.\n11. In a separate skillet, heat a little olive oil and sauté mushrooms until golden brown.\n12. Add sautéed mushrooms to the beef stew and simmer for an additional 15 minutes.\n13. Garnish with chopped fresh parsley before serving.',
            'views': 105,
            'likes': 32,
            'image':"recipes/beef_bourguignon.png"
        },
        {
            'title': 'Croissant',
            'categories': ['Hard'],
            'ingredients': '500g all-purpose flour\n1/4 cup granulated sugar\n1 tsp salt\n2 1/4 tsp instant yeast\n1 cup warm milk\n1/2 cup unsalted butter, melted\n1 egg, beaten\nButter, for laminating\nPowdered sugar, for dusting',
            'author': 'Culinary_Carnival',
            'directions': '1. In a large bowl, whisk together flour, sugar, salt, and instant yeast.\n2. Make a well in the center and pour in warm milk and melted butter.\n3. Mix until a dough forms, then turn out onto a floured surface.\n4. Knead the dough for 10-15 minutes, until smooth and elastic.\n5. Shape the dough into a ball and place in a greased bowl. Cover and let rise in a warm place for 1-2 hours, until doubled in size.\n6. Punch down the dough and divide it into four equal portions.\n7. Roll out each portion into a rectangle on a floured surface.\n8. Spread softened butter over the surface of each rectangle.\n9. Roll up each rectangle tightly into a log, then shape into a crescent.\n10. Place the croissants on a baking sheet lined with parchment paper.\n11. Cover and let rise for another 1-2 hours, until puffy.\n12. Preheat the oven to 200°C.\n13. Brush the croissants with beaten egg.\n14. Bake for 15-20 minutes, until golden brown.\n15. Dust with powdered sugar before serving.',
            'views': 115,
            'likes': 38,
            'image':"recipes/croissant.png"
        },
        {
            'title': 'Butter Chicken',
            'categories': ['Medium'],
            'ingredients': '500g boneless chicken, cut into bite-sized pieces\n1 cup plain yogurt\n2 tbsp ginger garlic paste\n2 tsp garam masala\n1 tsp ground turmeric\n1 tsp ground cumin\n1 tsp ground coriander\n1/2 tsp chili powder\n1/2 cup tomato puree\n1/4 cup cream\n2 tbsp butter\n2 tbsp oil\nSalt to taste\nFresh cilantro, for garnish\nCooked rice or naan, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. In a bowl, mix together yogurt, ginger garlic paste, garam masala, turmeric, cumin, coriander, and chili powder.\n2. Add chicken pieces to the marinade, making sure they are well coated. Cover and refrigerate for at least 1 hour.\n3. Heat oil and butter in a skillet over medium heat.\n4. Add marinated chicken pieces and cook until browned on all sides.\n5. Stir in tomato puree and simmer for 10-15 minutes, until chicken is cooked through.\n6. Add cream and simmer for another 5 minutes.\n7. Season with salt to taste.\n8. Garnish with fresh cilantro and serve hot with rice or naan.',
            'views': 90,
            'likes': 25,
            'image':"recipes/butter_chicken.png"
        },
        {
            'title': 'Vegetable Biryani',
            'categories': ['Hard'],
            'ingredients': '2 cups basmati rice, soaked for 30 minutes\n2 tbsp ghee or vegetable oil\n1 onion, thinly sliced\n2 carrots, diced\n1 potato, diced\n1/2 cup green peas\n1/4 cup cashew nuts\n1/4 cup raisins\n1 tsp cumin seeds\n1 cinnamon stick\n2-3 cardamom pods\n2-3 cloves\n1 bay leaf\n1 tsp garam masala\n1/2 tsp turmeric powder\n1/2 tsp chili powder\nSalt to taste\nFresh cilantro, for garnish\nYogurt raita, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. Heat ghee or oil in a large pot over medium heat.\n2. Add cumin seeds, cinnamon stick, cardamom pods, cloves, and bay leaf. Saute until fragrant.\n3. Add sliced onion and saute until golden brown.\n4. Stir in diced carrots, potato, green peas, cashew nuts, and raisins.\n5. Add soaked basmati rice and mix well.\n6. Season with garam masala, turmeric powder, chili powder, and salt.\n7. Pour in enough water to cover the rice by about an inch.\n8. Bring to a boil, then reduce heat to low, cover, and simmer for 20-25 minutes, until rice is cooked and water is absorbed.\n9. Fluff the rice with a fork and garnish with fresh cilantro.\n10. Serve hot with yogurt raita.',
            'views': 85,
            'likes': 22,
            'image':"recipes/veg_biryani.png"
        },
        {
            'title': 'Fish and Chips',
            'categories': ['Medium'],
            'ingredients': '4 fillets of white fish (cod, haddock, or pollock)\n1 cup all-purpose flour\n1 cup beer (lager works well)\n1 tsp baking powder\nSalt and pepper to taste\nVegetable oil, for frying\n4 large potatoes, peeled and cut into thick strips\nMalt vinegar, for serving\nTartar sauce, for serving',
            'author': 'Culinary_Carnival',
            'directions': '1. Heat vegetable oil in a deep fryer or large pot to 180°C (350°F).\n2. In a bowl, whisk together flour, beer, baking powder, salt, and pepper to make the batter.\n3. Dip fish fillets in the batter, allowing excess batter to drip off.\n4. Carefully lower fish into the hot oil and fry for 4-5 minutes, until golden brown and crispy.\n5. Remove fish from oil and drain on paper towels.\n6. In the same hot oil, fry potato strips in batches until golden and crispy, about 3-4 minutes per batch.\n7. Remove chips from oil and drain on paper towels.\n8. Serve fish and chips hot, with malt vinegar and tartar sauce on the side.',
            'views': 110,
            'likes': 40,
            'image':"recipes/fish_chips.png"
        },
        {
            'title': 'Shepherd\'s Pie',
            'categories': ['Easy'],
            'ingredients': '500g ground lamb or beef\n1 onion, diced\n2 carrots, diced\n2 cloves garlic, minced\n2 tbsp tomato paste\n1 cup beef or vegetable broth\n1 tsp Worcestershire sauce\n2 cups mashed potatoes\n1 cup frozen peas\nSalt and pepper to taste\nFresh parsley, for garnish',
            'author': 'Culinary_Carnival',
            'directions': '1. Preheat oven to 200°C (400°F).\n2. Heat oil in a large skillet over medium heat. Add diced onion, carrots, and garlic, and cook until softened.\n3. Add ground lamb or beef to the skillet and cook until browned.\n4. Stir in tomato paste, beef or vegetable broth, and Worcestershire sauce. Simmer for 10 minutes.\n5. Season with salt and pepper to taste.\n6. Transfer meat mixture to a baking dish and spread mashed potatoes evenly on top.\n7. Use a fork to create a decorative pattern on the surface of the mashed potatoes.\n8. Bake in preheated oven for 20-25 minutes, until the top is golden brown.\n9. Garnish with fresh parsley before serving.',
            'views': 120,
            'likes': 35,
            'image':"recipes/shepherd's_pie.png"
        },
        {
            'title': 'Borscht',
            'categories': ['Medium'],
            'ingredients': '500g beef stew meat, cubed\n2 tbsp vegetable oil\n1 onion, diced\n2 carrots, diced\n2 potatoes, diced\n2 beets, peeled and grated\n1/2 small head of cabbage, shredded\n4 cups beef or vegetable broth\n2 cups water\n2 tbsp tomato paste\n2 tbsp red wine vinegar\n1 bay leaf\nSalt and pepper to taste\nSour cream, for serving\nFresh dill, for garnish',
            'author': 'Culinary_Carnival',
            'directions': '1. Heat vegetable oil in a large pot over medium heat. Add beef stew meat and brown on all sides.\n2. Add diced onion and carrots to the pot and cook until softened.\n3. Stir in diced potatoes, grated beets, shredded cabbage, beef or vegetable broth, water, tomato paste, red wine vinegar, and bay leaf.\n4. Season with salt and pepper to taste.\n5. Bring the soup to a boil, then reduce heat and simmer for 1-1.5 hours, until meat and vegetables are tender.\n6. Remove bay leaf before serving.\n7. Serve borscht hot, topped with a dollop of sour cream and garnished with fresh dill.',
            'views': 130,
            'likes': 45,
            'image':"recipes/BORSCHT.png"
        },
        {
            'title': 'Pelmeni',
            'categories': ['Hard'],
            'ingredients': '2 cups all-purpose flour\n1/2 tsp salt\n1 large egg\n1/2 cup water\n300g ground beef\n300g ground pork\n1 onion, finely chopped\n2 cloves garlic, minced\nSalt and pepper to taste\nFor serving:\nSour cream\nButter\nFresh dill\n',
            'author': 'Culinary_Carnival',
            'directions': '1. To make the dough, combine flour and salt in a large bowl. Make a well in the center and add egg and water. Mix until a dough forms.\n2. Knead the dough on a floured surface until smooth and elastic. Cover with plastic wrap and let rest for 30 minutes.\n3. To make the filling, combine ground beef, ground pork, chopped onion, minced garlic, salt, and pepper in a bowl.\n4. Roll out the dough on a floured surface to about 1/8 inch thickness. Cut out circles using a round cookie cutter or glass.\n5. Place a small spoonful of filling in the center of each circle of dough.\n6. Fold the dough over the filling to form a half-moon shape. Press the edges together to seal.\n7. Bring a large pot of salted water to a boil. Add pelmeni in batches and cook for 5-7 minutes, until they float to the surface.\n8. Remove pelmeni with a slotted spoon and serve hot, topped with sour cream, butter, and fresh dill.',
            'views': 140,
            'likes': 50,
            'image':"recipes/pelmeni.png"
        },
        {
            'title': 'Yakitori',
            'categories': ['Medium'],
            'ingredients': '500g chicken thigh fillets, cut into bite-sized pieces\n1/4 cup soy sauce\n1/4 cup mirin\n2 tbsp sake (Japanese rice wine)\n2 tbsp sugar\nBamboo skewers, soaked in water\nReserved marinade\n1/4 cup water\n2 tbsp honey\n2 tbsp soy sauce\n1 tbsp sake\n1 tsp cornstarch dissolved in 1 tbsp water (optional, for thickening)',
            'author': 'Culinary_Carnival',
            'directions': '1. In a bowl, combine soy sauce, mirin, sake, and sugar to make the marinade. Reserve a portion of the marinade for the sauce.\n2. Add chicken pieces to the remaining marinade and marinate for at least 30 minutes, or overnight in the refrigerator.\n3. Preheat grill or broiler to medium-high heat.\n4. Thread marinated chicken onto soaked bamboo skewers, dividing evenly.\n5. Grill or broil chicken skewers, turning occasionally and basting with marinade, until cooked through and nicely charred, about 8-10 minutes.\n6. Meanwhile, prepare the sauce by combining the reserved marinade, water, honey, soy sauce, and sake in a small saucepan. Bring to a simmer over medium heat.\n7. If desired, thicken the sauce with cornstarch slurry, stirring constantly until thickened.\n8. Serve yakitori hot, drizzled with sauce and garnished with sesame seeds and chopped green onions.',
            'views': 160,
            'likes': 55,
            'image':"recipes/yakitori.png"
        },
        {
            'title': 'Okonomiyaki',
            'categories': ['Hard'],
            'ingredients': '1 cup all-purpose flour\n1/2 cup dashi (Japanese soup stock)\n2 eggs\n1/4 cabbage, thinly sliced\n2 green onions, thinly sliced\n1/2 cup tenkasu (tempura scraps)\n1/4 cup pickled ginger, chopped\nSalt and pepper to taste\nOkonomiyaki sauce (or a mixture of Worcestershire sauce, ketchup, and soy sauce)\nMayonnaise\nAonori (dried seaweed flakes)\nKatsuobushi (bonito flakes)\n',
            'author': 'Culinary_Carnival',
            'directions': '1. In a large bowl, whisk together flour, dashi, and eggs until smooth.\n2. Add sliced cabbage, green onions, tenkasu, pickled ginger, salt, and pepper to the batter. Mix until well combined.\n3. Heat a non-stick skillet or griddle over medium heat. Grease lightly with oil.\n4. Pour a ladleful of batter onto the skillet, spreading it out into a circle about 1/2-inch thick.\n5. Cook until the bottom is golden brown and crispy, about 5 minutes.\n6. Flip the okonomiyaki and cook the other side until golden brown and cooked through, about 5 more minutes.\n7. Transfer the okonomiyaki to a plate and drizzle with okonomiyaki sauce and mayonnaise.\n8. Sprinkle with aonori and katsuobushi.\n9. Serve hot, cut into wedges.',
            'views': 170,
            'likes': 60,
            'image':"recipes/okonomiyaki.png"
        },
        {
            'title': 'Croque Monsieur',
            'categories': ['Easy'],
            'ingredients': '4 slices of bread (preferably brioche or white sandwich bread)\n4 slices of ham\n100g Gruyère cheese, grated\n2 tbsp Dijon mustard\n2 tbsp unsalted butter\n2 tbsp all-purpose flour\n1 cup milk\nSalt and pepper to taste\nPinch of nutmeg\n',
            'author': 'Culinary_Carnival',
            'directions': '1. Preheat your oven to 200°C (400°F).\n2. Spread mustard evenly over two slices of bread.\n3. Place a slice of ham on each mustard-covered bread slice.\n4. Sprinkle half of the grated Gruyère cheese on top of the ham.\n5. Top with the remaining slices of bread to make sandwiches.\n6. In a saucepan, melt butter over medium heat. Add flour and whisk until smooth.\n7. Gradually add milk, whisking constantly, until the sauce thickens.\n8. Season the sauce with salt, pepper, and nutmeg.\n9. Remove the sauce from heat and pour it evenly over the sandwiches.\n10. Sprinkle the remaining grated Gruyère cheese on top.\n11. Place the sandwiches on a baking sheet and bake in the preheated oven for about 10-15 minutes, or until the cheese is melted and bubbly.\n12. Serve hot as a delicious and comforting meal!',
            'views': 180,
            'likes': 65,
            'image':"recipes/croque_monsieur.png"
        }

    ]

    for recipe in recipes_data:
        category_names = recipe.get('categories')
        categories = [Category.objects.get_or_create(name=name)[0] for name in category_names]

        author_name = recipe.get('author')
        author, _ = User.objects.get_or_create(username=author_name)

        recipe_data_copy = recipe.copy()
        recipe_author = recipe_data_copy.pop('author')
        recipe_categories = recipe_data_copy.pop('categories')

        recipe = Recipe.objects.create(author=author, **recipe_data_copy)
        recipe.categories.set(categories)  

def clear():
    Recipe.objects.all().delete()
    Category.objects.all().delete()


if __name__ == '__main__':

    print('Running WAD population script...')
    populate()
    print('Done')