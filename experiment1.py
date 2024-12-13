import streamlit as st

# App title
st.title("Ladies Tailoring Service")

# Introduction
st.write("""
Welcome to the Ladies Tailoring App!  
Provide your measurements, select your desired tailoring services, and we'll handle the rest.  
Let's create a perfect fit for you!
""")

# Sidebar for navigation
st.sidebar.title("Menu")
options = ["Home", "Measurements", "Services", "Submit"]
choice = st.sidebar.radio("Navigate", options)

# Home page
if choice == "Home":
    st.header("Welcome to Our Tailoring Service")
    st.image("https://via.placeholder.com/500x300.png?text=Tailoring+Service", use_column_width=True)
    st.write("""
    - Personalized tailoring services
    - High-quality stitching and fabrics
    - Fast delivery options available
    """)
    st.write("Select an option from the sidebar to get started.")

# Measurements input page
elif choice == "Measurements":
    st.header("Enter Your Measurements")

    # User inputs
    bust = st.number_input("Bust (in inches)", min_value=20.0, max_value=60.0, step=0.1)
    waist = st.number_input("Waist (in inches)", min_value=20.0, max_value=60.0, step=0.1)
    hips = st.number_input("Hips (in inches)", min_value=20.0, max_value=60.0, step=0.1)
    height = st.number_input("Height (in inches)", min_value=40.0, max_value=90.0, step=0.1)
    
    st.write("Please ensure all measurements are accurate for the perfect fit!")

# Services selection page
elif choice == "Services":
    st.header("Select Tailoring Services")
    
    # Checkbox options
    st.write("Choose your desired services:")
    stitching = st.checkbox("Custom Stitching")
    alteration = st.checkbox("Alteration")
    embroidery = st.checkbox("Embroidery")
    express_delivery = st.checkbox("Express Delivery")

    if stitching:
        st.write("- Custom Stitching selected")
    if alteration:
        st.write("- Alteration selected")
    if embroidery:
        st.write("- Embroidery selected")
    if express_delivery:
        st.write("- Express Delivery selected")

# Submission page
elif choice == "Submit":
    st.header("Submit Your Details")
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    
    # Confirm submission
    if st.button("Submit"):
        if name and phone and email:
            st.success(f"Thank you, {name}! Your details have been submitted. We'll contact you shortly.")
        else:
            st.error("Please fill in all fields before submitting.")

# Footer
st.sidebar.info("Developed by [Dijendra]")
