import streamlit as st

# Title and Header
st.title("Retail Business Dashboard")
st.header("Manager Input Section")


# Instruction
st.write("Please enter the monthly sales target and select the region")



# Number input for sales target
sales = st.number_input("Enter monthly sales target (In USD):",
                      min_value=0,
                      max_value=1000000,
                      value=10000)



# Dropdown for region selection
region = st.selectbox("Choose your select region:",
                      ["North", "Asian", "EU", "USA"])



# Submit button
if st.button("Submitted"):
    st.write("Button clicked!")
    # Display entered values
st.write(f"Your monthly salary is {sales}")
st.write(f"Your selected region is: {region}")


    # Success message
st.success("Operation completed successfully!")


    # Extra message for ambitious target



