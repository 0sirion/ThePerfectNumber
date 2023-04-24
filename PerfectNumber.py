import streamlit as st

st.header(":red[The Perfect Number]")
st.subheader(":blue[Give me a number, I'll tell you  if it is perfect number]")
st.markdown('In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.')

numero = st.slider(label="slide to choose a number:",min_value=0, max_value=100)
# numero = 6

partial = 0


def main():
    perfect(numero)
    def perfect(numero): 
        for i in range(1, numero-1):
            if numero%i == 0:
                partial = partial + i
        
    

if numero == partial:
    st.write(numero,"Is a perfect number")




if __name__ == '__main__':
    main()