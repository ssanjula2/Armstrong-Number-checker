import streamlit as st

# Title
st.title("Armstrong Number Checker")

# User input
number = st.number_input("Enter a number:", min_value=0, step=1, format="%d")

# When button is clicked
if st.button("Check Armstrong Number"):
    # Function to check Armstrong number
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)

    # Show calculation
    calculation_steps = " + ".join([f"{d}^{power}" for d in num_str])
    calculation_result = f"{calculation_steps} = {total}"

    # Display calculation
    st.write(f"### Calculation:")
    st.write(calculation_result)

    # Final result
    if total == number:
        st.success(f"✅ {number} is an Armstrong Number!")
    else:
        st.error(f"❌ {number} is NOT an Armstrong Number.")
