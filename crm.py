
import pandas as pd
import streamlit as st
from PIL import Image
def main():
# إنشاء قائمة منسدلة للتنقل بين الصفحات
    pages = ["الصفحة الرئيسية", "Visits"]
    page = st.sidebar.selectbox("الصفحات", pages)
    # عرض الصفحة المختارة
    if page == "الصفحة الرئيسية":
        st.header('Welcom To Alba Pharma Crm Rep Module')
        image = Image.open(r'C:\Users\dell\Desktop\unnamed.jpg')
        st.image(image, caption='My Image', use_column_width=True)   
    elif page == "Visits":
        st.sidebar.header('Chosen Input Data')
        regions = ["Cairo", "Alex", "Delta", "Upper"]
        selected_region = st.sidebar.selectbox("***Governate***", regions)
        if selected_region == "Cairo":
            choices = [' ',"Shubra", "Hilioplis", "Cairo East","Maadi","Nasr City"]
        elif selected_region == "Alex":
            choices = [' ',"Kafr Elshikh", "Alex Center", "Alex East","El Behera"]
        elif selected_region == "Delta":
            choices = [' ',"El Gharbia", "El Dakahlia2", "El Menofia","El Sharkia","El Dakahlia 1"]
        else:
            choices = [' ',"Sohag", "Menia", "Asiut","Qena"]
        # عرض القائمة المنسدلة الثانية
        BD=st.sidebar.selectbox("***Area***", choices)
        if BD == "El Gharbia":
            bre = [' ',"السنطه", "بسيون", "زفتي","سمنود","طنطا","قطور","كفر الزيات"]
        elif BD == "El Dakahlia2":
            bre = [' ',"الجمالية", "المنزلة", "المنصوره","بني عبيد","دكرنس","شربين","منية النصر","ميت سلسيل","ميت فارس"]   
        elif BD == "Hilioplis":
            bre = [' ',"الشروق", "العاشر", "العبور","هليوبوليس"]     
        elif BD == "Cairo East":
            bre = [' ',"ابو زعبل", "الخانكة", "الخصوص","السلام","القلج","المرج","المطريه","حدائق الزيتون","حلمية الزيتون","عزبة النخل","عين شمس"] 
        elif BD == "El Dakahlia 1":
            bre = [' ',"اجا", "السنبلاوين", "المنصوره","بلقاس","ميت غمر"] 
        elif BD == "El Behera":
            bre = ["ابو المطامير","ابو حمص",'ادكو',"ايتاى البارود","حوش عيسى","دلنجات","دمنهور","رشيد","كفر الدوار","كوم حماده","محموديه"] 
        elif BD == "Kafr Elshikh":
            bre = [' ',"الحامول","الرياض","بلطيم","بيلا","دسوق","سيدي سالم","فوه","قلين","كفر الشيخ","مطوبس"] 
        elif BD == "Menia":
            bre = [' ',"ابوقرقاص", "المنيا", "بني مزار","سمالوط","مغاغه","ملوي"] 
        elif BD == "El Menofia":
            bre = [' ',"الباجور", "الشهداء", "بركه السبع","تلا","شبين","شبين الكوم","قوسنا","قويسنا"] 
        elif BD == "Maadi":
            bre = [' ',"حدائق حلوان", "حلوان", "معادى","تبين","ثكنات المعادى","طره","كوتسكا"]    
        elif BD == "Qena":
            bre = [' ',"الاقصر", "دشنا", "قنا","قوص","نجع حمادي","نقادة"]
        elif BD == "El Sharkia":
            bre = [' ',"ابوحماد", "ابوكبير", "الابراهيميه","الزقازيق","ديرب نجم","فاقوس","كفر صقر","ههيا","ولاد صقر"]
        elif BD == "Shubra":
            bre = [' ',"ابو الهنا", "الاميريه", "الخلفاوي","الزاويه","الضاهر","المرور","الموسسه","الوايلى",
                "ام بيومي","اول شبرا","بيجام","جزيرة بدران","حدائق القبه","روض الفرج","سانت تريزا",
                "شارع الترعه","شارع شبرا","عرابي","فيكتوريا","قهوة شرف","مسره","مسطرد"]
        elif BD == "Alex Center":
            bre = [' ',"الابراهيمية", "البيطاش", "الحضرة","الهانوفيل","بحري","سبورتنج","سموحه","سيدي جابر",
                    "كامب شيزار","كليوباترا","محرم بك","محطة الرمل"]
        elif BD == "Alex East":
            bre = [' ',"الأقبال", "السيوف", "العصافره","الفلكي","المندره","بوكلا","جليم","چناكليس","رشدي","زيزنيا",
                "سانستيفانو","سيدي بشر","فليمنج","فيكتوريا","كفر عبده","ميامي"]
        elif BD == "Asiut":
            bre = [' ',"ابنوب", "ابو تيج", "اسيوط","القوصيه","ديروط","ساحل سليم","منفلوط"]    
        elif BD == "Sohag":
            bre = [' ',"اخميم", "البلينا", "المراغه","المنشاه","جرجا","دار السلام","ساقلته","سوهاج سنتر",
                "طما","طهطا"]  
        else:
            bre=[1,2]                              
        brick=st.sidebar.selectbox("Bricks", bre)
        Action1=st.sidebar.button("عرض العملاء")

        data=pd.read_excel(r"E:\Medical Rep Data Base\Data Program.xlsx")
        values = data.loc[data['Bricks'] == brick]
        while Action1==True:
            st.write(values)
            Area_Name=st.write(BD)
            break

        Client=st.multiselect("Clients",values['Client Name'])
        Date=st.date_input("Date")
        Comment=st.text_input("Comment")
        sav=st.button('Submit')
        if sav==True:
            New_data={"Bricks":brick,"Client":Client,"Date":Date,"Comment":Comment}
            new_df=pd.DataFrame(New_data)
            new_df.to_csv('TEST1')
            existing_df =pd.read_csv(r"C:\Users\dell\TEST1") 
            existing_df = existing_df.append(new_df)  
            existing_df.to_csv("TEST1")
            st.write("تم التسجيل بنجاح")    
if __name__=='__main__':
    main()   


       
        

