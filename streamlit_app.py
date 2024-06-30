import streamlit as st

# Function to convert frequency to ARFCN
def freq_to_arfcn(frequency, network_type):
    if network_type == '2G':
        if 935 <= frequency <= 960:
            return int((frequency - 935) / 0.2) + 128
        elif 1805 <= frequency <= 1880:
            return int((frequency - 1805) / 0.2) + 512
    elif network_type == '3G':
        if 2110 <= frequency <= 2170:
            return int((frequency - 2110) / 0.2) + 10562
    elif network_type == '4G':
        if 2110 <= frequency <= 2200:
            return int((frequency - 2110) / 0.1)
    return None

# Main function to run the app
def main():
    st.title("Frequency to ARFCN Converter")

    # Sidebar inputs
    st.sidebar.header("Input Parameters")
    frequency = st.sidebar.number_input("Frequency (MHz)", min_value=0.0, max_value=6000.0, value=900.0, step=0.1)
    network_type = st.sidebar.selectbox("Network Type", options=['2G', '3G', '4G'])

    # Conversion and result display
    if st.sidebar.button("Convert"):
        arfcn = freq_to_arfcn(frequency, network_type)
        if arfcn is not None:
            st.success(f"The ARFCN for {frequency} MHz in {network_type} is: {arfcn}")
        else:
            st.error("Invalid frequency or network type selected.")

if __name__ == "__main__":
    main()
