import streamlit as st

st.header(":red[The Perfect Number]")
st.subheader(":blue[Give me a number, I'll tell you  if it is perfect number]")
st.markdown('In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.')

# numero = 6

partial = 0


def main():
    numero = st.slider (label="slide to choose a number: ", min_value=0, max_value= 100) #on_change=check())

    def check():
        st.write(numero)
    
    check()




if __name__ == '__main__':
    main()