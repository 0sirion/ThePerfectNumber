import streamlit as st

st.header(":red[The Perfect Number]")
st.subheader(":blue[Give me a number, I'll tell you  if it is a perfect number]")
st.markdown('In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.')


# numero = 6



def main():
    numero = st.slider (label="slide to choose a number: ", min_value=0, max_value= 100) #on_change=check())
    st.markdown("As perfect numbers aren't common, you can also type here instead:")
    numero_input = st.number_input(label="Please enter an integer below:", step=1)
    
    

    def check_slider():
        partial = 0 
        for i in range(1, numero-1):
            if numero%i == 0:
                partial = partial + i
        if numero == partial and numero != 0:
            st.write(numero,"Is a perfect number!")
            # st.balloons()
            
        else:
            if numero !=partial and numero !=0:
                st.write("Ops!", numero, "is not a perfect number...")



    check_slider()

    def check_input():
        partial = 0
        for i in range(1, numero_input-1):
            if numero_input%i == 0:
                partial = partial + i
        if numero_input == partial and numero_input != 0:
            st.write(numero_input, "is a perfect number!")
            # st.balloons()
        else:
            if numero_input !=partial and numero_input !=0:
                st.write("Ops!", numero_input, "is not a perfect number...")
    check_input()




if __name__ == '__main__':
    main()