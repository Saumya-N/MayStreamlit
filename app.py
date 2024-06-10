import streamlit as st

st.write("""
# Mathematical Calculation App
""")

def sqr(num):
    return num**2

def sqrt(num):
    return num**0.5

def pal(num):
    num_org = num
    s=0
    while num!=0:
        temp = num%10
        num=num//10
        s=s*10 + temp
    if s==num_org:
        return 'Yes, a palindrome'
    else:
        return 'No, not a palindrome'

number = st.slider("Pick a number", 0, 100)

col1, col2, col3 = st.columns(3)
if st.button("Calculate"):
    with col1:
        st.write("**Square**")
        result = sqr(number)
        st.text(result)
    with col2:
        st.write("**Square Root**")
        result = sqrt(number)
        st.text(result)
    with col3:
        st.write("**Palindrome**")
        result = pal(number)
        st.text(result)