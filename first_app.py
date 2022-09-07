import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

#Download dataframe
cartoon_df = pd.read_csv('cartoon_fys.csv')
cartoon_df = cartoon_df.drop('Unnamed: 0', axis=1)


options=['Find your show!','CM22 Studios', 'About']
selections=st.sidebar.selectbox('Menu', options)

# About the app

if selections == 'About':

    st.header("Cartoon Mania")
    st.markdown("Cartoons are the earliest form of art. Earliest in the sense it resonates best with those of us who have just started to                   experience art.")
    st.markdown("We try to keep the list updated so you can try have an idea of what the world thinks of your favorite show.")

# Search for a show and receive details such as premier year, genres and rating.

if selections == 'Find your show!':
    name=st.text_input('Cartoon', 'Yogi Bear') 
    
    st.subheader(name)
    
    if name in cartoon_df.cartoon_names.unique():
        st.dataframe(cartoon_df[cartoon_df['cartoon_names'].str.contains(name)])
        
# Predict rating after providing number of seasons and three genres
        
if selections == 'CM22 Studios':
    st.header('Pitch your own movie!')
    st.subheader('Get your review instantly!')
    st.markdown('Welcome to CM22 Studios, where we are passionate about talent!')
    st.write('Show us what you got!!')
    genres = ['Action', 'Adventure', 'Anime', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Short', 'Doc', 'Musical', 'SciFi','Talkshow']
    st.write('Pick your first genre!')
    genre1=st.selectbox('genre1', genres)

    
    st.write('Pick your second genre!')     
    genre2=st.selectbox('genre2', genres)
 
    
    st.write('Pick your third genre!')
    genre3= st.selectbox('genre3', genres)
    
    st.write('Pick number of seasons!')
    season = st.text_input('Number of Seasons', )
    
    import numpy as np
    try:
        det = {'runtime':[np.log(int(season))], 'Genre1_codes':[genre1], 'Genre2_codes':[genre2], 'Genre3_codes':[genre3]}
        df = pd.DataFrame(det)
    #convert genres to categorical datatype
        df['Genre1_codes'] = pd.Categorical(df['Genre1_codes'], categories=genres)
        df['Genre2_codes'] = pd.Categorical(df['Genre2_codes'], categories=genres)
        df['Genre3_codes'] = pd.Categorical(df['Genre3_codes'],categories=genres)
# Convert to numeric datatype to feed into model
        df['Genre1_codes'] = df['Genre1_codes'].cat.codes
        df['Genre2_codes'] = df['Genre2_codes'].cat.codes
        df['Genre3_codes'] = df['Genre3_codes'].cat.codes
 #        
        
        from joblib import load
        rf = load(filename = 'CARTOON-IMDB_Prediction')
        prediction = rf.predict(df)
        st.write('Your Prediction ' + str(prediction))
#         def review(prediction):
#              if prediction >= 1 and prediction < 2:
#                 review=print('Ridiculous')
#                 return review
            
#              elif prediction >= 2 and prediction < 3:
#                 review=print('Awful')
#                 return review
    
#              elif prediction >= 3 and prediction < 4:
#                 review=print('Bad')
#                 return review
        
#              elif prediction >= 4 and prediction < 5:
#                 review=print('ehh')
#                 return review
        
#              elif prediction >= 5 and prediction < 6:
#                 review=print('Average')
#                 return review
        
#              elif prediction >= 6 and prediction < 7:
#                 review=print('Good')
#                 return review
        
#              elif prediction >= 7 and prediction < 8:
#                 review=print('Good +')
#                 return review
        
#              elif prediction >= 8 and prediction < 9:
#                 review=print('Very Good')
#                 return review
    
#              elif prediction >=9 and prediction < 10:
#                 review=print('Excellent')
#                 return review
    
#              elif prediction >=10:
#                 review=print('Amazing')
#                 return review
        
        
#         reviews = review(prediction)
#         st.write(reviews) 
        
    except ValueError:
        pass


    
    
    
     
    


# footer_temp = """
# <!-- CSS  -->
# <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
# <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" 
# type="text/css" rel="stylesheet" media="screen,projection"/>
# <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
# <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" 
# integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
# <footer class="page-footer grey darken-4">
# <div class="container" id="aboutapp">
# <div class="row">
# <div class="col l6 s12">
# <h5 class="white-text">Retail Analysis App</h5>
# <h6 class="grey-text text-lighten-4">This is Africa Data School Streamlit Class practical.</h6>
# <p class="grey-text text-lighten-4">August 2021 Cohort</p>
# </div>
# <div class="col l3 s12">
# <h5 class="white-text">Connect With Us</h5>
# <ul>
# <a href="https://www.facebook.com/AfricaDataSchool/" target="_blank" class="white-text">
# <i class="fab fa-facebook fa-4x"></i>
# </a>
# <a href="https://www.linkedin.com/company/africa-data-school" target="_blank" class="white-text">
# <i class="fab fa-linkedin fa-4x"></i>
# </a>
# <a href="https://www.youtube.com/watch?v=ZRdlQwNTJ7o" target="_blank" class="white-text">
# <i class="fab fa-youtube-square fa-4x"></i>
# </a>
# <a href="https://github.com/Africa-Data-School" target="_blank" class="white-text">
# <i class="fab fa-github-square fa-4x"></i>
# </a>
# </ul>
# </div>
# </div>
# </div>
# <div class="footer-copyright">
# <div class="container">
# Made by <a class="white-text text-lighten-3" href="https://africadataschool.com/">Regan </a><br/>
# <a class="white-text text-lighten-3" href="https://africadataschool.com/"></a>
# </div>
# </div>
# </footer>
# """

# if selections == 'About':
#     st.header("About App")
#     components.html(footer_temp, height=500)
        
    
    
    
    