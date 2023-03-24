import streamlit as st

# Indent Config Is Using Space Three Times

st.set_page_config(
   page_title="Learnst - Predict Student's Learning Style",
   page_icon="🎓",
   layout="wide",
   initial_sidebar_state="expanded")

st.title("🎓 welcome to learnst")
st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel. Mauris quam risus, tincidunt ac metus id, luctus condimentum odio. Aliquam erat volutpat. Integer et lobortis ligula. Fusce placerat dolor nec mi tempor vestibulum. Vestibulum neque libero, elementum in pulvinar non, luctus at sapien. Sed fermentum lorem in feugiat finibus. Sed sit amet convallis sem. Aliquam massa ex, tempus ac est vitae, porttitor feugiat dolor. Ut massa enim, ultricies sit amet porta eu, posuere quis nulla.", unsafe_allow_html=False)

st.subheader("How to work ?")
st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

code = '''def predict():
   """
   this is code
   for processing
   the machine learning
   """
   print("your learning style is {predict_result}")'''

st.code(code, language='python')
st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

st.subheader("# 01 - multiple choices answer")

with st.form("choices_form"):

   score = st.number_input("Skor")
   click_per_question = st.text_input("Klik Per Soal")
   total_click = st.number_input("Total Klik")
   duration_per_question = st.text_input("Durasi Per Soal")
   total_duration = st.number_input("Total Durasi")

   choices_checkbox = st.checkbox("Validation Test")

   # Every form must have a submit button.
   choices_submitted = st.form_submit_button("Predict Multiple Choices Learning Style", use_container_width=True)
   
   if choices_submitted:
	   st.session_state['multiple_choices_answer_state'] = str(choices_checkbox)

if 'multiple_choices_answer_state' not in st.session_state:
   st.warning("Please fill parameters above to see the prediction result !")

else:
   st.success("Your Multiple Choices Answer Learning Style Is " + str(choices_checkbox) )

st.subheader("# 02 - essay answer")

with st.form("essays_form"):
   st.code("COMING SOON")
   essays_checkbox = st.checkbox("Validation Test")
   
   # Every form must have a submit button.
   essays_submitted = st.form_submit_button("Predict Learning Style", use_container_width=True)
   
   if essays_submitted:
	   st.session_state['esssay_answer_state'] = str(essays_checkbox)

if 'esssay_answer_state' not in st.session_state:
   st.warning("Please fill parameters above to see the prediction result !")

else:
   st.success("Your Essays Answer Learning Style Is " + str(essays_checkbox) )

configurations = """
   <style>
	   #MainMenu {visibility: hidden;}
	   footer {visibility : hidden;}
	</style>"""

st.markdown(configurations, unsafe_allow_html=True)