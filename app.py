import gspread
from google.oauth2 import service_account
import streamlit as st
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(credentials)

sheet = client.open_by_key('1nT9XdPnloGnd7zetMkk9QUUweCp5P4BRv6_16Ros0Vc').sheet1

data = sheet.get_all_records(value_render_option='UNFORMATTED_VALUE')

Cat = pd.DataFrame(data)

Link_Dynam_video = "https://youtu.be/ebLbUOP4Fxw"
Link_Static_video = "https://youtu.be/tOUJIJZPC0c"

# Отображаемый заголовок страницы

col1, col2, col3 = st.columns(3)
with col2:
    st.image("logo.jpg")

st.markdown("<h2 style='text-align: center;'>Группа Автоматизации ОИТ</h2>", unsafe_allow_html=True)
st.markdown("""<h5 style='text-align: center;'>Данный ресурс
был инициативно разработан в рамках работ по созданию Группы Автоматизации 
с целью ускорения рабочих процессов внутри КТ-2 ОИТ ПКГ</h5>""", unsafe_allow_html=True)

with st.expander("Пример работы параметрических подвесок"):
    tab1, tab2 = st.tabs(["Динамическая подвеска", "Статическая подвеска"])
    
    with tab1:
        
        link_Dynam_video_toclic = '[Динамическая подвеска](https://drive.google.com/file/d/1zTKpoM5lzU2X57U3BoQSPMVYhkV0Dia9)'
        st.markdown(link_Dynam_video_toclic, unsafe_allow_html=True)
        st.video(Link_Dynam_video)
        
    with tab2:
        
        link_Static_video_toclic = '[Статическая подвеска](https://drive.google.com/file/d/1zPCz3aTlSNoIJmzN3WSn0gQq4pKchv78)'
        st.markdown(link_Static_video_toclic, unsafe_allow_html=True)
        st.video(Link_Static_video)

with st.expander("Документация отдела"):
    tab3, tab4, tab5 = st.tabs(["Документация отдела", "Каталоги в формате PDF", "ОСТ и ГОСТ"])
    
    with tab3:
        
        link_gdoc_catkt2 = '[КАТАЛОГ-V2 EN Rev 1.15](https://docs.google.com/document/d/1kggsuWohlANXEBIN3wv5DjPjplPA8IEOb1mgRBnEUwU)'
        st.markdown(link_gdoc_catkt2, unsafe_allow_html=True)

        link_gtab_catkt2 = '[Каталог исполнений EN](https://docs.google.com/spreadsheets/d/1XXqpF812VpcDxl8vKbdoOdzEPRkntHr78UikhM3QBEE)'
        st.markdown(link_gtab_catkt2, unsafe_allow_html=True)
        
        link_gtab_classdb = '[База данных классификатора](https://docs.google.com/spreadsheets/d/1IuvKFnJiJrreNc7r1Z0raRZ_2Jldb9stRviL29npjPw)'
        st.markdown(link_gtab_classdb, unsafe_allow_html=True)
        
        link_gtab_plan = '[План разработки ОПС](https://docs.google.com/spreadsheets/d/11NcLnZtwZqvuYUy11FmEPRPfmbuHfK0R8AmW4WahaaU)'
        st.markdown(link_gtab_plan, unsafe_allow_html=True)
        
        link_gtab_sbor = '[Собираемость каталога EN](https://docs.google.com/spreadsheets/d/1tiS1vDSIksz-2bbnb0Iak7DS4h6hIoebu0_9jdqQ9xE)'
        st.markdown(link_gtab_sbor, unsafe_allow_html=True)
        
        link_gtab_svod = '[Сводная таблица гостов](https://docs.google.com/spreadsheets/d/1rSWC-QtGFNyhhlCqhJFHW8CPdGiPwbzRdjQkEHHVwwo)'
        st.markdown(link_gtab_svod, unsafe_allow_html=True)
        
    with tab4:
        
        link_pdf_ttt3 = '[Московский проектный институт. Типовые технические требования. 01.PA1.0.0.TM.TT.NSN082 Ревизия В03](https://drive.google.com/file/d/1ACf4viy5IXRDdU7Ok3Di2A-LVmqmJD54/view?usp=sharing)'
        st.markdown(link_pdf_ttt3, unsafe_allow_html=True)
        
        link_pdf_ttt4 = '[Московский проектный институт. Типовые технические требования. 01.PA1.0.0.TM.TT.NSN082 Ревизия В04](https://drive.google.com/file/d/1bm4inRO5oVe9uuA7pg813He4vAxAllhM/view?usp=sharing)'
        st.markdown(link_pdf_ttt4, unsafe_allow_html=True)
    
        link_pdf_Lisega2010iso = '[Lisega. Стандартные опоры 2010. ISO](https://drive.google.com/file/d/1MpFCm99Qvr5wzru7MvFrWaWHL-AlciHZ/view?usp=sharing)'
        st.markdown(link_pdf_Lisega2010iso, unsafe_allow_html=True)
    
        link_pdf_Lisega2010ost = '[Lisega. Стандартные опоры 2010. ОСТ](https://drive.google.com/file/d/14MpB56BfkJSchpWZllVL_vMHY2OZStYM/view?usp=sharing)'
        st.markdown(link_pdf_Lisega2010ost, unsafe_allow_html=True)
    
        link_pdf_Lisega2020iso = '[Lisega. Стандартные опоры 2020. ISO](https://drive.google.com/file/d/1X5zwYRjoh9qRU1o8PJdHALdGpGiIfYck/view?usp=sharing)'
        st.markdown(link_pdf_Lisega2020iso, unsafe_allow_html=True)
            
    with tab5:
        
        link_pdf_L8 = '[Энергомонтажпроект. Л8-508.000 + Л8-524.000](https://drive.google.com/file/d/1f6oJaNkER0JqVu2lQtnxg7_wHrR0RLv9/view?usp=sharing)'
        st.markdown(link_pdf_L8, unsafe_allow_html=True)
        
        link_pdf_ost24_125_127 = '[ОСТ 24.125.127 - Блоки хомутовые для вертикальных трубопроводов](https://drive.google.com/file/d/1XkZHXuB5MNkD5fYvYqE0IX2CinaV4NIQ/view?usp=sharing)'
        st.markdown(link_pdf_ost24_125_127, unsafe_allow_html=True)

with st.expander("Общая таблица соответствия"):
    st.write('Данная таблица включает в себя информацию по каталогу Аккую, Lisega, Л8, ЦКТИ и их соответствие элементам ОПС КТ-2. Пользуясь поисковым интерфейсом в нижней части окна можно найти требуемое изделие.')
    show_Cat = Cat
    show_Cat.rename(columns = {'KT2':'Каталог КТ2','Обозначение':'Обозначение чертежа', 'Наименование':'Наименование чертежа', 'Масса':'Масса, кг', 'Нагрузка':'Нагрузка, kN', 'Состояние':'Состояние документа'}, inplace = True)
    st.dataframe(data = show_Cat)
    title_AKU_EN = st.text_input('Поле ввода для поиска по столбцу Note', 'WS.1.010.C.F2')
    st.dataframe(show_Cat.loc[show_Cat['Note'] == title_AKU_EN])
    title_EN_AKU = st.text_input('Поле ввода для поиска по столбцу Каталог КТ2', 'EN-341-60-1')
    st.dataframe(show_Cat.loc[show_Cat['Каталог КТ2'] == title_EN_AKU])  
    
st.sidebar.header('Модуль классификации ведомостей ОПС')
st.sidebar.write("1. Загрузка ведомости опор осуществляется в формате таблиц excel с листа Sheet1")
st.sidebar.write("2. Нужно удалить две верхних строки и первые два скрытых столбца - таблица должна начинаться со столбца KKS Code (в ячейке A1)")
st.sidebar.write("3. Определяемый столбец дожен иметь название Note")

uploaded_file3 = st.sidebar.file_uploader("Область загрузки")
if uploaded_file3 is not None:
    st.write("Filename: ", uploaded_file3.name)
    С = pd.read_excel(uploaded_file3, sheet_name = "Sheet1", dtype = {'Note': str})
    final = pd.merge(С, Cat, how = 'left', on = ['Note'])
    final = final.round(1)
    st.write('Соответствие опор запрашиваемых в ведомости.',
             '**Развернуть** таблицу на весь экран можно кнопкой, находящейся **в правом верхнем углу** таблицы.')
    st.write(final)
    
    #Cкачиваем обработанную ведомость
    df_xlsx = to_excel(final)
    st.sidebar.download_button(label='📥 Скачать обработанную ведомость', data=df_xlsx, file_name=uploaded_file3.name)
    if st.sidebar.button('📥 Скачать ведомость отправочных марок'):
        st.sidebar.write('Мы тоже хотим чтобы это работало')
        st.balloons()