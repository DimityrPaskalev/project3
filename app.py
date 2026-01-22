import streamlit as st

st.title("📝 Анкета")
name = st.text_input("Въведи име:")
age = st.number_input(
    "Въведи възраст:",
    min_value=1,
    max_value=120,
    step=1
)
rating = st.selectbox(
    "Дай оценка:",
    [2, 3, 4, 5, 6]
)
if st.button("Изпрати анкетата"):
    if name.strip() == "":
        st.error("Моля, въведи име!")
    else:
        st.success("Анкетата е изпратена успешно!")
        st.write("### Резултат:")
        st.write(f"**Име:** {name}")
        st.write(f"**Възраст:** {age}")
        st.write(f"**Оценка:** {rating}/6")
