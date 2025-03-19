import streamlit as st
import random
import os

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            color: #2c3e50;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #FF9800;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
        }
        .stApp {
            background: linear-gradient(to right, #f9f5e3, #f0e6d2);
            color: #2c3e50;
        }
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 10px;
        }
        .image-container img {
            width: 300px !important;
            height: auto;
            display: block;
            margin: 0 auto;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>The Dietitian AI 🍽️</h1>", unsafe_allow_html=True)

# Display Banner Image
image_path = "C:/Users/abhib/Desktop/Project/Dietitian_AI-master/a1b89bb1-7eb8-478c-996f-1edddf5e69ec.webp"
st.markdown("<div class='image-container'>", unsafe_allow_html=True)
if os.path.exists(image_path):
    st.image(image_path, use_container_width=False, width=300)
else:
    st.image("https://source.unsplash.com/1600x400/?healthy-food,fruits,vegetables", use_container_width=False, width=300)
st.markdown("</div>", unsafe_allow_html=True)

# User Inputs
gender = st.selectbox("Select Gender", ["Male", "Female"])
weight = st.number_input("Enter Weight (kg)", min_value=30.0, max_value=200.0, step=0.5)
height = st.number_input("Enter Height (cm)", min_value=100.0, max_value=250.0, step=1.0)
age = st.number_input("Enter Age", min_value=10, max_value=100, step=1)
activity = st.selectbox("Select Activity Level", [
    "Sedentary (little or no exercise)",
    "Lightly active (1-3 days/week)",
    "Moderately active (3-5 days/week)",
    "Very active (6-7 days/week)",
    "Super active (twice/day)"
])

# BMR Calculation
def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

bmr = calculate_bmr(gender, weight, height, age)

# Activity Factor
activity_multiplier = {
    "Sedentary (little or no exercise)": 1.2,
    "Lightly active (1-3 days/week)": 1.375,
    "Moderately active (3-5 days/week)": 1.55,
    "Very active (6-7 days/week)": 1.725,
    "Super active (twice in a day)": 1.9
}

total_calories = bmr * activity_multiplier[activity]
st.markdown(f"<h3 style='color: #e74c3c; text-align: center;'>Your daily calorie requirement: {total_calories:.2f} kcal</h3>", unsafe_allow_html=True)

# Meal Plan Suggestions
meals = {
    "protein": ['Yogurt', 'Cooked meat', 'Cooked fish', 'Eggs', 'Tofu'],
    "fruit": ['Berries', 'Apple', 'Orange', 'Banana', 'Dried Fruits'],
    "vegetables": ['Broccoli', 'Carrots', 'Spinach', 'Cucumber', 'Tomatoes'],
    "grains": ['Brown Rice', 'Whole Wheat Bread', 'Oats', 'Quinoa', 'Corn Tortillas'],
    "snacks": ['Almonds', 'Cottage Cheese', 'Hummus', 'Soy Nuts', 'Low-fat Yogurt'],
}

# Recipes
recipes = {
    "Yogurt": "Yogurt Mix with fresh fruits and a drizzle of honey.",
    "Cooked meat": "Cooked meat : Grill with spices and serve with steamed veggies.",
    "Cooked fish": "Fish : Bake with lemon, garlic, and herbs.",
    "Eggs": " Eggs : Scramble with spinach and whole-grain toast.",
    "Tofu": " Tofu : Stir-fry with bell peppers and soy sauce.",
    "Berries": " Berries : Blend into a smoothie with yogurt.",
    "Apple": " Apple : Slice and dip into peanut butter.",
    "Orange": " Orange : Make a fresh juice or eat as is.",
    "Banana": " Banana : Mash with oats and nuts for a quick snack.",
    "Dried Fruits": " Dried Fruits : Mix with nuts for a healthy energy boost.",
    "Broccoli": " Broccoli : Steam and drizzle with olive oil.",
    "Carrots": " Carrots : Roast with a pinch of salt and pepper.",
    "Spinach": " Spinach : Sauté with garlic and serve with rice.",
    "Cucumber": " Cucumber : Slice and mix with yogurt and mint.",
    "Tomatoes": " Tomatoes : Chop into a fresh salad with olive oil.",
    "Brown Rice": " Brown Rice : Cook with a bit of garlic and serve with protein.",
    "Whole Wheat Bread": " Wheat Bread : Make a sandwich with hummus and veggies.",
    "Oats": " Oats : Boil with milk and top with fruits and nuts.",
    "Quinoa": " Quinoa : Cook with lemon and serve as a salad base.",
    "Corn Tortillas": " Corn Tortillas : Make a wrap with grilled vegetables.",
    "Almonds": " Almonds : Eat raw or mix with yogurt.",
    "Cottage Cheese": " Cottage Cheese : Spread on toast with honey.",
    "Hummus": " Hummus : Dip with whole-wheat crackers.",
    "Soy Nuts": " Soy Nuts : Eat as a crunchy snack.",
    "Low-fat Yogurt": " Low-fat Yogurt : Mix with granola and berries."
}
# Initialize session state to store meal plan
if "meal_plan" not in st.session_state:
    st.session_state.meal_plan = None
    st.session_state.show_recipe = False  # Track recipe visibility

# Generate Meal Plan Button
if st.button("Generate Meal Plan"):
    st.session_state.meal_plan = {
        "breakfast": [random.choice(meals['protein']), random.choice(meals['fruit'])],
        "lunch": [random.choice(meals['protein']), random.choice(meals['vegetables']), random.choice(meals['grains'])],
        "snack": [random.choice(meals['snacks']), random.choice(meals['vegetables'])],
        "dinner": [random.choice(meals['protein']), random.choice(meals['vegetables']), random.choice(meals['grains'])]
    }
    st.session_state.show_recipe = False  # Reset recipe visibility

# Display Meal Plan
if st.session_state.meal_plan:
    for meal, items in st.session_state.meal_plan.items():
        st.success(f"🍽️ **{meal.capitalize()}:** {', '.join(items)}")

    # Show Recipe Button
    if st.button("Want Recipe?"):
        st.session_state.show_recipe = True  # Set flag to show recipes

# Display Recipes (Only when 'Want Recipe?' is clicked)
if st.session_state.show_recipe and st.session_state.meal_plan:
    st.subheader("Recipes for Your Meal Plan")
    for meal, items in st.session_state.meal_plan.items():
        st.write(f"**{meal.capitalize()} Recipes:**")
        for item in items:
            st.write(f"- {item}: {recipes.get(item, 'Recipe not found.')}")
