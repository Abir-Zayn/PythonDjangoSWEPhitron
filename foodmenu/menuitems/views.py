from django.shortcuts import render

def foodMenu(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "des":"BeaverTails are a delicious Canadian pastry that has gained popularity worldwide. Shaped like a beaver's tail, hence the name, these sweet treats are made from a yeast-based dough that is stretched and flattened to resemble the tail of a beaver. "
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "des":"Breakfast potatoes are a popular morning dish made from diced or sliced potatoes that are seasoned and cooked until crispy. Often served alongside eggs, bacon, or sausages, these potatoes offer a comforting and hearty start to the day"
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "des":"Canadian Butter Tarts are a beloved Canadian dessert that is known for its rich, gooey, and buttery filling."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "des":"Montreal Smoked Meat is a flavorful deli-style sandwich made with cured and smoked beef brisket, typically served on rye bread with mustard. It's a beloved specialty of Montreal cuisine."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
             "des":"Nanaimo Bars are a Canadian dessert with a buttery chocolate-coconut base, a creamy custard filling, and a chocolate ganache topping. They are a rich and indulgent treat."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
             "des":"Pate Chinois is a French-Canadian dish consisting of layers of ground beef, corn, and mashed potatoes. It's a comforting and satisfying meal with a simple yet delicious flavor profile."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "des":"Pouding Chomeur is a classic Quebecois dessert made of a moist cake-like batter baked in a pool of sweet maple syrup. It's a decadent and comforting treat that showcases the rich flavors of maple"
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "des":"Poutine is a Canadian dish consisting of crispy french fries topped with cheese curds and smothered in rich gravy. It's a delicious and indulgent combination of flavors and textures"
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "des":"Rappie Pie is a traditional Acadian dish made with grated potatoes and meat, usually chicken or pork. The grated potatoes are mixed with the meat, seasoned, and baked to create a savory and hearty pie."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "des":"Split Pea Soup is a comforting and hearty soup made from dried split peas, vegetables, and sometimes ham or bacon. It has a thick and creamy texture with a satisfying and savory flavor."
        }
    ]
    # img_list =[]
    # for mealImg in meals:
    #     img_url= mealImg['strMealThumb']
    #     img_list.append(img_url)
    
    context ={ 'menu':meals}
    return render(request,"index.html",context)
    

# Create your views here.
