
from random import choices

import pandas as pd
import numpy as np
import streamlit as st
st.set_page_config(layout="wide")


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def main():
	"""Welcome to E-Hospital"""
	import streamlit as st
	

	menu = ["Home","Login","SignUp","contact","Model","Dashboard","types","EDA - Profiling","Data"]
	choice = st.sidebar.selectbox("Menu",menu)
	menu = ["Home","Login","SignUp","contact","Model"]
	if choice == "Home":
		
		st.title("Welcome to MSBA's e-Hospital")
		html_string3 ='<a href="https://im.ge/i/ujJwLL"><img src="https://i.im.ge/2022/07/06/ujJwLL.webp" alt="ujJwLL.webp" border="0"></a>'
		st.markdown(html_string3, unsafe_allow_html= True)
		st.markdown("<h1 style='text-align: left; color: Red;'>You have Reached the Stroke Web Pannel</h1>", unsafe_allow_html=True)

		st.write("Please Login or Signup if New!This web application is restricted to certain individuals only due to the confidentiality of the data and thus would require access permission.")


	








	if choice == "contact":

		st.markdown("<h1 style='text-align: center; color: green;'>Save Yourself While You can!</h1>", unsafe_allow_html=True)
		contact_form = """<form action="https://formsubmit.co/mad58@mail.aub.edu" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
     <textarea name="message" placeholder="Please Book an appointment if your entries returned 1"></textarea>
     <button type="submit">Send</button>
</form>"""
		st.markdown(contact_form, unsafe_allow_html= True)
		def local_css(file_name):
			with open(file_name) as f:
				st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

		local_css("style.css")
        


	if choice =="Data":
		import pandas as pd
		

		import streamlit as st

		uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
		if uploaded_data:
			st.markdown("<h1 style='text-align: center; color: red;'>A look into the data</h1>", unsafe_allow_html=True)
			df= pd.read_csv(uploaded_data)

			with open('style1.css') as f:
				st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

			Kpi1, Kpi2, Kpi3, Kpi4 =st.columns(4)

			col = df.columns
			Kpi1.metric(label ="Number of Columns", value = len(col))

			Kpi2.metric(label="Number of rows", value = len(df))

			Kpi3.metric(label="Null values", value = df.isnull().sum().sum())

			Kpi4.metric(label="Duplicates", value =df.duplicated().sum().sum())


			st.markdown("<h1 style='text-align: center; color: green;'>Health references and Risk factors</h1>", unsafe_allow_html=True)

			b1, b2, b3, b4 = st.columns(4)

			with st.container():
				b1.metric("BMI healthy Range","18.5 - 24.9")
			b2.metric("Normal glucose Level","Below 140")
			b3.metric("Women","More deadly")
			b4.metric("Men","More likely")

			st.sidebar.header("filter through")
			gender=st.sidebar.multiselect("select Gender:",options=df["gender"].unique(),default= df["gender"].unique())
			Marriage=st.sidebar.multiselect("select Marital Status:",options=df["ever_married"].unique(),default= df["ever_married"].unique())
			Smoking=st.sidebar.multiselect("select Smoking status:",options=df["smoking_status"].unique(),default= df["smoking_status"].unique())

			df_selection = df.query("gender == @gender & ever_married == @Marriage & smoking_status ==@Smoking")
			st.dataframe(df_selection,width=1200, height=300)
	







	if choice =="EDA - Profiling":
		import pandas as pd
		import streamlit as st

		import pandas_profiling

		from pandas_profiling import ProfileReport

		from streamlit_pandas_profiling import st_profile_report

		uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
		if uploaded_data:
			df=pd.read_csv(uploaded_data)
			profile = ProfileReport(df,explorative= True)
			st_profile_report(profile)









	if choice == "types":
		import pandas as pd
		import streamlit as st

		from streamlit_option_menu import option_menu

		selected= option_menu(menu_title="Stroke types", options=["Ischemic Stroke","Hemorrhagic Stroke",'TIA (Transient Ischemic Attack)','Cryptogenic Stroke']
		,icons=['heart','heart','heart','heart'],orientation='horizontal')

		if selected =='Ischemic Stroke':
			st.markdown("<h1 style='text-align: center; color: Red;'>Ischemic Stroke (Clots)</h1>", unsafe_allow_html=True)
			html_string5 ='<a href="https://im.ge/i/uA49uq"><img src="https://i.im.ge/2022/07/06/uA49uq.jpg" alt="uA49uq.jpg" border="0"></a>'
			st.markdown(html_string5,unsafe_allow_html=True)

			st.write("When the blood flow to a portion of the brain is blocked or diminished, brain tissue cannot receive oxygen and nutrients, which results in an ischemic stroke. In minutes, brain cells start to degenerate.")

		if selected == 'Hemorrhagic Stroke':
			st.markdown("<h1 style='text-align: center; color: Red;'>Hemorrhagic Stroke (Bleeds)</h1>", unsafe_allow_html=True)
			html_string6 ='<a href="https://im.ge/i/uABnZc"><img src="https://i.im.ge/2022/07/06/uABnZc.png" alt="uABnZc.png" border="0"></a>'
			st.markdown(html_string6, unsafe_allow_html= True)
			st.write("When blood from an artery suddenly starts bleeding into the brain, it results in a hemorrhagic stroke. As a result, the portion of the body that the damaged section of the brain controls cannot function normally.Hemorrhagic stroke can occur in two major ways:When there is bleeding inside the brain, it is known as an intracranial hemorrhage.Subarachnoid hemorrhages are when there is bleeding between the membranes covering the brain.")


		if selected =='TIA (Transient Ischemic Attack)':
			st.markdown("<h1 style='text-align: center; color: Red;'>TIA (Transient Ischemic Attack)</h1>", unsafe_allow_html=True)
			html_string7 ='<a href="https://im.ge/i/uAGxcG"><img src="https://i.im.ge/2022/07/06/uAGxcG.jpg" alt="uAGxcG.jpg" border="0"></a>'
			st.markdown(html_string7, unsafe_allow_html= True)

			st.write("An episode of transient ischemic attack (TIA), which has symptoms resembling those of a stroke, occurs suddenly. A TIA typically lasts only a few minutes and has no lasting effects.A TIA, often known as a ministroke, may be an alert. A stroke will eventually occur in roughly 1 in 3 TIA patients, with about half happening within a year after the TIA.It can act as both a stroke warning sign and a window of opportunity to stop one.")

		if selected =='Cryptogenic Stroke':
			st.markdown("<h1 style='text-align: center; color: Red;'>Cryptogenic Stroke</h1>", unsafe_allow_html=True)
			html_string8 ='<a href="https://im.ge/i/uCrtXS"><img src="https://i.im.ge/2022/07/06/uCrtXS.jpg" alt="uCrtXS.jpg" border="0"></a>'
			st.markdown(html_string8, unsafe_allow_html=True)

			st.write("The majority of the time, a blood clot that prevents blood flow to the brain is what causes a stroke. However, sometimes the cause cannot be identified despite testing. Strokes that are cryptogenic are those having an unknown cause.")
			st.write(" Potential hidden causes could be: Irregular heartbeat, heart structure problems, hardening of the arteries, blood clotting disorder")






	if choice == "Dashboard":

		import pandas as pd
		import streamlit as st
		from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
		import plotly.express as px
		import plotly.graph_objects as go
		from streamlit_option_menu import option_menu

		st.markdown("<h1 style='text-align: center; color: Blue;'>Dashboard</h1>", unsafe_allow_html=True)
		uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
		df = pd.read_csv(uploaded_data)

		if uploaded_data:
			selected= option_menu(menu_title=None, options=["Overview","Dataset specific",'General','General 2'],icons=['book','book','book','book'],orientation='horizontal')
			if selected == "Overview":
				st.sidebar.header("filter through")
				gender=st.sidebar.multiselect("select Gender:",options=df["gender"].unique(),default= df["gender"].unique())
				Marriage=st.sidebar.multiselect("select Marital Status:",options=df["ever_married"].unique(),default= df["ever_married"].unique())
				Smoking=st.sidebar.multiselect("select Smoking status:",options=df["smoking_status"].unique(),default= df["smoking_status"].unique())
				df_selection = df.query("gender == @gender & ever_married == @Marriage & smoking_status ==@Smoking")

				col1, col2, col3, col4 = st.columns(4)
				with col1:
					st.metric(label='Patients with heart disease',value=df_selection[df_selection['heart_disease']==1].value_counts().sum())
					st.markdown("""
        <style>
    div[data-testid="metric-container"] {
    background-color: rgba(95, 204, 218, 0.8);
    border: 1px solid rgba(95, 204, 218, 0.8);
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
    color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
</style>
"""
, unsafe_allow_html=True)
				with col2:
					st.metric(label='Patients with hypertension', value=df_selection[df_selection['hypertension']==1].value_counts().sum())

				with col3:
					st.metric(label='smokers',value=df_selection[df_selection['smoking_status']=='smokes'].value_counts().sum())
				
				with col4:
					st.metric(label='Married',value=df_selection[df_selection['ever_married']=='Yes'].value_counts().sum())

				b1, b2  = st.columns(2)

				with b1:
					df_stroke=df_selection.groupby('stroke')['id'].count().reset_index(name='count')
					fig88 = px.pie(df_stroke, values='count',names='stroke', height = 350, width = 400,title='Stroke Count')
					fig88=go.Figure(fig88)

					b1.plotly_chart(fig88)

				with b2:
					df_gender = df_selection.groupby('gender')['id'].count().reset_index(name='count')
					fig18 = px.pie(df_gender, values='count',names='gender', height = 350, width = 400, title='Gender count')
					fig18=go.Figure(fig18)

					b2.plotly_chart(fig18)

				c1, c2, c3 =st.columns(3)
				with c1:
					fig00= px.bar(df_selection, x='gender',y='stroke', height=400, width=400)
					fig00= go.Figure(fig00)

					c1.plotly_chart(fig00)

				with c2:
					fig01= px.bar(df_selection, x='gender',y='heart_disease', height=400, width=400)
					fig01= go.Figure(fig01)

					c2.plotly_chart(fig01)

				with c3:
					fig06 = px.bar(df_selection, x='smoking_status',y='stroke', color='gender',barmode='group', height=400, width=400)
					fig06 = go.Figure(fig06)

					c3.plotly_chart(fig06)

			
			if selected == "Dataset specific":
				met1, met2, met3, met4 = st.columns(4)
				st.markdown("""
        <style>
    div[data-testid="metric-container"] {
    background-color: rgba(95, 204, 218, 0.8);
    border: 1px solid rgba(95, 204, 218, 0.8);
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
    color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
</style>
"""
, unsafe_allow_html=True)
				with met1:
					st.metric(label='Strokes Patients below 18', value=len(df[(df['stroke']==1) & (df['age']<18)]))
				
				with met2:
					st.metric(label='Strokes Patients ages (18-30)', value=len(df[(df['stroke']==1) & (df['age']>18) & (df['age']<30)]))

				with met3:
					st.metric(label='Strokes Patients ages (30-60)', value=len(df[(df['stroke']==1) & (df['age']>30) & (df['age']<60)]))
				
				with met4:
					st.metric(label='Strokes Patients Above 60', value=len(df[(df['stroke']==1) & (df['age']>60)]))

				con1, con2 = st.columns(2)
				with con1:
					fig09 = px.sunburst(df, path=['gender','Residence_type','smoking_status'], values='stroke', color='gender', height=400, width=600)
					fig09=go.Figure(fig09)
					st.plotly_chart(fig09)

				
				with con2:
					fig099 = px.sunburst(df, path=['gender','ever_married','work_type'], values='stroke', color='gender',height=400, width=600)
					fig099=go.Figure(fig099)
					st.plotly_chart(fig099)

				m1, m2 = st.columns(2)
				with m1:
					df_smoking1 = df[df['stroke']==1].groupby(['smoking_status']).size().reset_index(name="counts of stroke")
					fig45 = px.violin(df_smoking1,x='smoking_status', y='counts of stroke')
					fig45 = go.Figure(fig45)
					st.plotly_chart(fig45)

				with m2:
					df_working = df[df['stroke']==1].groupby(['work_type']).size().reset_index(name="counts of stroke")
					fig46 = px.violin(df_working,x='work_type', y='counts of stroke')
					fig46 = go.Figure(fig46)
					st.plotly_chart(fig46)

				g1, g2 = st.columns(2)
				with g1:
					df_aging = df[df['stroke']==1].groupby(['age']).size().reset_index(name="counts of stroke")
					fig645 = px.scatter(df_aging, x='age', y='counts of stroke')
					fig645 = go.Figure(fig645)
					fig645.update_traces(marker=dict(color='red'))
					st.plotly_chart(fig645)

				with g2:
					fig74 = px.violin(df,x='work_type', y='bmi', height=400, width=600)
					fig74 = go.Figure(fig74,layout_yaxis_range =[5,50])
					fig74.update_traces(marker=dict(color='red'))
					st.plotly_chart(fig74)

			if selected == 'General 2':
				kol1, kol2 =st.columns(2)
				with kol1:
					html_string = '<iframe src="https://ourworldindata.org/grapher/annual-number-of-deaths-by-cause?time=latest" loading="lazy" style="width: 100%; height: 500px; border: 0px none;"></iframe>'
					st.markdown(html_string, unsafe_allow_html=True)

				with kol2:
					html_string2 = '<iframe src="https://ourworldindata.org/grapher/total-number-of-deaths-by-cause?stackMode=relative&country=~OWID_WRL" loading="lazy" style="width: 100%; height: 500px; border: 0px none;"></iframe>'
					st.markdown(html_string2, unsafe_allow_html= True)

			if selected == 'General':

				html_string3 = '<iframe src="https://ourworldindata.org/grapher/stroke-death-rates?country=MAR~NGA~LBR" loading="lazy" style="width: 100%; height: 600px; border: 0px none;"></iframe>'
				st.markdown(html_string3, unsafe_allow_html= True)

            		








	elif choice == "Model":
		import pandas as pd
		import streamlit as st
		import plotly.express as px
		import random
		from sklearn.ensemble import RandomForestClassifier
		from sklearn.metrics import accuracy_score
		from sklearn.model_selection import train_test_split as tts
		uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')

		df = pd.read_csv(uploaded_data)
		if uploaded_data:
			del df["id"]
			df = df.dropna()
			df = df[df['age'] >= 2]
			df = df[df['gender'] != 'Other']

			df2 = df
			df2['stroke'] = df2['stroke'].replace([0],'No')
			df2['stroke'] = df2['stroke'].replace([1],'Yes')
			df2['Count'] = 1

			df2 = df2.sort_values(
			by=['stroke'],
			ascending=False).iloc[0:len(df2[df2['stroke']=='Yes'])*2]

			cleanup_vals = {"gender": {"Male": 0, "Female": 1},
                    "ever_married": {"No": 0, "Yes": 1},
                    "work_type": {"Never_worked": 0, "children": 1, "Self-employed": 2, "Private": 3, "Govt_job": 4},
                    "Residence_type" : {"Urban": 0, "Rural": 1},
                    "smoking_status": {"Unknown": 0, "never smoked": 1, "formerly smoked": 2, "smokes": 3}}

			df = df.replace(cleanup_vals)
			df = df.drop(columns=['Count'], axis=1)
			y=df['stroke']
			x=df.drop('stroke',axis=1)


			x_train,x_test,y_train,y_test=tts(x,y,test_size=0.25)
			rf = RandomForestClassifier(n_estimators=25, random_state=0)
			rf.fit(x_train, y_train)

			def user_report():
				st.write("""Male =0 , Female = 1""")
				gender =st.radio('Sex:',options=[0,1])
				st.write("""Type your age""")
				age=st.text_input('Age:', max_chars=3, value=0)
				st.write("""No hypertension = 0, otherwise 1""")
				hypertension=st.select_slider('Hypertension',options=[0,1])
				st.write("""No heart disease = 0, otherwise 1""")
				heart_disease=st.select_slider('Heart Disease: (0 for no Heart Disease, 1 for Heart Disease)',options=[0,1])
				st.write("""Yes=1, 0 otherwise""")
				ever_married=st.radio('Ever Married:', options=[0,1])
				st.write("Never_worked: 0, children: 1, Self-employed: 2, Private: 3, Govt_job: 4")
				work_type=st.select_slider('Work Type:', options=[0,1,2,3,4])
				st.write("Urban: 0, Rural: 1")
				Residence_type=st.radio('Residence Type:', options=[0,1])
				st.write("please type your average glucose level")
				avg_glucose_level=st.text_input('Average Glucose Level:', max_chars=6, value=0)
				st.write("please type your BMI")
				bmi=st.text_input('BMI:', max_chars=4, value=0)
				st.write("Unknown: 0, never smoked: 1, formerly smoked: 2, smokes: 3")
				smoking_status=st.select_slider('Smoking Status:', options=[0,1,2,3])

				user_report_data = {
				
				'gender':gender,
				'age':age,
				'hypertension':hypertension,
				'heart_disease':heart_disease,
				'ever_married':ever_married,
				'work_type':work_type,
				'Residence_type':Residence_type,
				'avg_glucose_level':avg_glucose_level,
				'bmi':bmi,
				'smoking_status':smoking_status
				}
				
				report_data =pd.DataFrame(user_report_data, index = [0])
				return report_data
			
			user_data = user_report()
			st.subheader('Prediction')
			st.write(user_data)

			outcome = (rf.predict(user_data))
			st.subheader('Stroke Prediction')
			st.subheader(outcome)
			st.title("please head to the contact page if the stroke prediction returned Yes")






        
        
        

	elif choice == "Login":
        
		st.subheader("Login Section")
        

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Welcome you're logged in as {}".format(username))

				Select = st.selectbox("Selection",["upload data","Data Exploration","Registered Users"])
				if Select == "upload data":
					import pandas as pd
					uploaded_data = st.file_uploader('Upload dataset', type='csv')
					if uploaded_data:
						import pandas as pd
						import streamlit as st
						df= pd.read_csv(uploaded_data)
						st.markdown("<h1 style='text-align: center; color: red;'>Introduction</h1>", unsafe_allow_html=True)
						st.write("""Stroke is one of the leading causes of death worldwide. It can lead to long term disabilities if not a short-termm death. Therefore, managing Stroke's leading risk factors and trying to predict a stroke before happening is paramount.This web application will aims to provide a closer look at stroke in general, identify risk factors correlations and insights sing various data sources and help in the prediction of a potential stroke in favor of preventing it.""")
						
    					
						
    					


				elif Select == "Data Exploration":
					uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
					if uploaded_data:
						df=pd.read_csv(uploaded_data)
						st.sidebar.header("filter Through")
						gender=st.sidebar.multiselect("select Gender:",options=df["gender"].unique(),default= df["gender"].unique())
						Marriage=st.sidebar.multiselect("select Marital Status:",options=df["ever_married"].unique(),default= df["ever_married"].unique())
						Smoking=st.sidebar.multiselect("select Smoking status:",options=df["smoking_status"].unique(),default= df["smoking_status"].unique())

						df_selection =df.query("gender == @gender & ever_married == @Marriage & smoking_status ==@Smoking")

						st.dataframe(df_selection)
    					


				elif Select == "Registered Users":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
                    
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		st.title("""Please sign in to request access""")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")


	


if __name__ == '__main__':
	main()










#menu = ["Login","signup"]
#choice = st.sidebar.selectbox("Menu",menu)

#if choice == "Login":
    #st.subheader("Login Section")

    #username = st.sidebar.text_input("Username")
    #password = st.sidebar.text_input("password", type="password")
    #if st.sidebar.button("Login"):
        #st.success("Logged in as {}".format(username))

        #st.markdown("""Mohamad""")

        #st.title("Dbouking")