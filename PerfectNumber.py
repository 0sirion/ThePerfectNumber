import streamlit as st

st.header(":red[The Perfect Number]")
st.subheader(":blue[Give me a number, I'll tell you  if it is a perfect number]")
st.markdown('In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.')

# numero = 6

partial = 0


def main():
    numero = st.slider (label="slide to choose a number: ", min_value=0, max_value= 100) #on_change=check())
    st.markdown("As perfect numbers aren't common, you can also typer here instead:")
    numero_input = st.number_input(label="Please enter an integer below:", step=1)
    
    def perfect():
        partial = 0 
        for i in range(1, numero-1):
            if numero%i == 0:
                partial = partial + i
        if numero == partial:
            st.write(numero,"Is a perfect number!")
    perfect()




if __name__ == '__main__':
    main()