import streamlit as st
import pandas as pd
import pickle
import time
from streamlit_option_menu import option_menu
from PIL import Image
import webbrowser
from bokeh.models.widgets import Div

# IMPORTANT : indent config is using spacebar three times

# set streamlit page config
st.set_page_config(
   page_title="Learnst - Predict Student's Learning Style",
   page_icon="🎓",
   layout="wide",
   initial_sidebar_state="auto")

# declare variable
current_url = st.experimental_get_query_params()
direct_menu = int(current_url["redirect"][0]) if "redirect" in current_url else 0
titl_effect ="""
   <div class="contaienr">
      <div class="tilt-box-wrap">
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <span class="t_over"></span>
         <div class="tilt-box">
            <img src="https://ciknuk.site:443/media/e72bc3f961cefcbb111d0262b1449aa23ba4ae15f9059037c25195db.jpg" alt="0" style="max-width: 100%;">
         </div>
      </div>
   </div>
   <br>"""

# sidebar menu
with st.sidebar:

   # banner
   st.markdown(titl_effect, unsafe_allow_html=True)

   menu = option_menu(None, ["Documentations", "Exams Prediction", "Essays Prediction", "GitHub Repository", "Explore Dataset"],
   icons =["journal-text", "ui-checks", "receipt", "github", "link-45deg"],
   default_index=int(direct_menu),
   styles={
   "container": {"padding": "0px !important", "padding-right" : "2px", "background-color": "white"},
   "nav-item": {"background" : "white"},
   "nav-link": {"font-size" : "13px", "text-align": "left", "margin-top":"5px", "margin-bottom":"5px", "--hover-color": "#F8F9FB", "background-color" : "#F8F9FB"},
   "nav-link-selected": {"background-color": "#E8B840"}
   })

if menu == "Documentations":

   # declare variable
   code = '''def predict():
      """
      this is code
      for processing
      the machine learning
      """
      print(f"your learning style is {predict_result}")'''
   
   # title and caption
   st.title("🎓 welcome to learnst")
   st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel. Mauris quam risus, tincidunt ac metus id, luctus condimentum odio. Aliquam erat volutpat. Integer et lobortis ligula. Fusce placerat dolor nec mi tempor vestibulum. Vestibulum neque libero, elementum in pulvinar non, luctus at sapien. Sed fermentum lorem in feugiat finibus. Sed sit amet convallis sem. Aliquam massa ex, tempus ac est vitae, porttitor feugiat dolor. Ut massa enim, ultricies sit amet porta eu, posuere quis nulla.", unsafe_allow_html=False)

   # sub header and caption
   st.subheader("About datasets")
   st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

   # sub header and caption
   st.subheader("How to work")
   st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

   # diplay text as code format and caption
   st.code(code, language="python")
   st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

elif menu == "Exams Prediction":
   
   # declare variable
   default_exam_template = [{
         "exam_score" : "100",
         "click_per_question" : "1,1,1,1,1",
         "total_click" : "5",
         "duration_per_question" : "1,1,1,1,1",
         "total_duration" : "5"}]
   score_value = int(current_url["exam_score"][0]) if "exam_score" in current_url else 0
   click_per_question_value = current_url["click_per_question"][0] if "click_per_question" in current_url else "0"
   total_click_value = int(current_url["total_click"][0]) if "total_click" in current_url else 0
   duration_per_question_value = current_url["duration_per_question"][0] if "duration_per_question" in current_url else "0"
   total_duration_value = int(current_url["total_duration"][0]) if "total_duration" in current_url else 0

   # sub header and caption
   st.subheader("Exam default template")
   st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

   default_exam_df = pd.DataFrame(default_exam_template)
   st.dataframe(default_exam_df, use_container_width=True)

   st.caption(":blue[exam_score] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[click_per_question] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[total_click] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[duration_per_question] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[total_duration] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)

   # category one : predict multiple choices answer
   st.subheader("Multiple choices answer prediction")

   # predict form category one
   with st.form(key="choices_form"):
      
      score = st.number_input("Skor", value=score_value, min_value=0, max_value=100)
      c1, c2 = st.columns(2)
      c3, c4 = st.columns(2)

      with c1:
         click_per_question = st.text_input("Klik Per Soal", value=click_per_question_value)
      
      with c2:
         total_click = st.number_input("Total Klik", value=total_click_value, min_value=0)
      
      with c3:
         duration_per_question = st.text_input("Durasi Per Soal", value=duration_per_question_value)
      
      with c4:
         total_duration = st.number_input("Total Durasi", value=total_duration_value, min_value=0)

      progress_text = "STATUS : IDLE"
      progress_bar = st.progress(0, text=progress_text)

      choices_submitted = st.form_submit_button("Predict Multiple Choices Learning Style", use_container_width=True)

      data = [{
         "exam_score" : score,
         "click_per_question" : click_per_question,
         "total_click" : total_click,
         "duration_per_question" : duration_per_question,
         "total_duration" : total_duration
      }]

      encoded_data = [{
         "exam_score" : score,
         "click_per_question" : click_per_question.replace(",", "") if "," in click_per_question else click_per_question,
         "total_click" : total_click,
         "duration_per_question" : duration_per_question.replace(",", "") if "," in duration_per_question else duration_per_question,
         "total_duration" : total_duration
      }]
      
      if choices_submitted:
         st.session_state["multiple_choices_answer_state"] = data

   # 
   clusters = pickle.load(open("learnst_model.pickle", "rb"))

   # save result as state
   if "multiple_choices_answer_state" not in st.session_state:
      st.info("Please fill parameters above and submit predict to see the result !")

   # execute
   else:

      # handle error
      try:

         if choices_submitted:
            for percent_complete in range(100):
               df_predict = pd.DataFrame(data)
               encoded_df = pd.DataFrame(encoded_data, columns=df_predict.columns)
               predictions = clusters.predict(encoded_df)
               if df_predict is not None and percent_complete == 20:
                  progress_bar.progress(percent_complete + 1, text="STATUS : GATHERING DATASET")
                  time.sleep(2)
                  st.dataframe(df_predict, use_container_width=True)
               if encoded_df is not None and percent_complete == 40:
                  progress_bar.progress(percent_complete + 1, text="STATUS : PREPROCESSING DATA")
                  time.sleep(2)
                  st.dataframe(encoded_df, use_container_width=True)
               if predictions is not None and percent_complete == 80:
                  progress_bar.progress(percent_complete + 1, text="STATUS : PREDICTING DATA")
                  time.sleep(2)
                  st.dataframe(predictions, use_container_width=True)
            progress_bar.progress(percent_complete + 1, text="STATUS : PREDICTION COMPLETE")
            if predictions == 0:
               st.success("Your Student Performance Is " + "Bad")
            elif predictions == 1:
               st.success("Your Student Performance Is " + "Balance")
            else:
               st.success("Your Student Performance Is " + "Good")
      except:
         st.error("Invalid parameters, please [follow](#default-template) default template above !")

elif menu == "Essays Prediction":

   # declare variable
   default_essay_template = [{
         "exam_score" : "100",
         "click_per_question" : "1,1,1,1,1",
         "total_click" : "5",
         "duration_per_question" : "1,1,1,1,1",
         "total_duration" : "5"}]
   
   # sub header and caption
   st.subheader("Essay default template")
   st.caption("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis quis risus dui. Fusce a finibus libero. Vivamus consequat elit orci, non gravida enim vehicula vel.", unsafe_allow_html=False)

   default_essay_df = pd.DataFrame(default_essay_template)
   st.dataframe(default_essay_df, use_container_width=True)

   st.caption(":blue[exam_score] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[click_per_question] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[total_click] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[duration_per_question] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)
   st.caption(":blue[total_duration] = Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=False)

   # category two : predict essays answer
   st.subheader("Essays answer prediction")

   # predict form category two
   with st.form("essays_form"):
      
      st.code("COMING SOON")
      essays_checkbox = st.checkbox("Validation Test")
      
      essays_submitted = st.form_submit_button("Predict Learning Style", use_container_width=True)
      
      if essays_submitted:
         st.session_state["esssay_answer_state"] = str(essays_checkbox)

   # save result as state
   if "esssay_answer_state" not in st.session_state:
      st.info("Please fill parameters above and submit predict to see the result !")

   else:
      if essays_checkbox:
         st.success("Your Essays Answer Learning Style Is " + str(essays_checkbox))
      else:
         st.error("Your Essays Answer Learning Style Is " + str(essays_checkbox))

elif menu == "GitHub Repository":

   github_link = "window.open('https://github.com/rasvanjaya21/learnst')"
   github_html = '<img src onerror="{}">'.format(github_link)
   github_div = Div(text=github_html)
   
   st.bokeh_chart(github_div)

elif menu == "Explore Dataset":
   
   dataset_link = "window.open('https://www.kaggle.com/datasets/rasvanjaya21/learnst-student-exam-interaction-dataset')"
   dataset_html = '<img src onerror="{}">'.format(dataset_link)
   dataset_div = Div(text=dataset_html)
   
   st.bokeh_chart(dataset_div)

# set streamlite config
configurations = """
   <style>
      #MainMenu {
         visibility: hidden;
      }
      footer {
         visibility: hidden;
      }
      .stApp {
         top: 3px !important;
      }
      section[data-testid="stSidebar"] {
         box-shadow: none !important;
         border-right: inset;
         background-color: white !important;
         width: 300px !important;
      }
      *,*:after,*:before{
         -webkit-box-sizing: border-box;
         -moz-box-sizing: border-box;
         -ms-box-sizing: border-box;
         box-sizing: border-box;
      }
      .tilt-box-wrap{
         width: auto;
         height: auto;
         position: relative;
         transition: all 0.6s ease-out;
         perspective: 1000px
      }
      .tilt-box-wrap:hover{
         transition: all 0.3s linear;
         transform: scale(1);
      }
      .tilt-box{
         width: auto;
         height: auto;
         position: relative;
         display: flex;
         align-items: center;
         text-align: center;
         color: #fff;
         font-size: 90px;
         font-weight: 700;
         text-transform: uppercase;
         transition: all 0.6s ease-out;
         transform:rotateX(0deg) rotateY(0deg);
         perspective: 1000px;
         transform-style: preserve-3d;
      }
      .t_over{
         width: 33.333%;
         height: 33.333%;
         position: absolute;
         z-index: 1;
      }

      .t_over:nth-child(1){ left: 0; top: 0; }
      .t_over:nth-child(2){ left: 33.333%; top: 0; }
      .t_over:nth-child(3){ left: 66.666%; top: 0; }
      .t_over:nth-child(4){ left: 0; top: 33.333%; }
      .t_over:nth-child(5){ left: 33.333%; top: 33.333%; }
      .t_over:nth-child(6){ left: 66.666%; top: 33.333%; }
      .t_over:nth-child(7){ left: 0; top: 66.666%; }
      .t_over:nth-child(8){ left: 33.333%; top: 66.666%; }
      .t_over:nth-child(9){ left: 66.666%; top: 66.666%; }
      .t_over:nth-child(1):hover ~ .tilt-box{transform:rotateX(-20deg) rotateY(20deg);}
      .t_over:nth-child(2):hover ~ .tilt-box{transform: rotateX(-20deg) rotateY(0deg)}
      .t_over:nth-child(3):hover ~ .tilt-box{transform: rotateX(-20deg) rotateY(-20deg)}
      .t_over:nth-child(4):hover ~ .tilt-box{transform: rotateX(0deg) rotateY(20deg)}
      .t_over:nth-child(5):hover ~ .tilt-box{transform: rotateX(0deg) rotateY(0deg)}
      .t_over:nth-child(6):hover ~ .tilt-box{transform: rotateX(0deg) rotateY(-20deg)}
      .t_over:nth-child(7):hover ~ .tilt-box{transform:rotateX(20deg) rotateY(20deg);}
      .t_over:nth-child(8):hover ~ .tilt-box{transform: rotateX(20deg) rotateY(0deg)}
      .t_over:nth-child(9):hover ~ .tilt-box{transform: rotateX(20deg) rotateY(-20deg)}
   </style>"""

# hide footer
st.markdown(configurations, unsafe_allow_html=True)