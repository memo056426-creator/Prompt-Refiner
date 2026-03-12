import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")

# 1. التأكد من وجود المفتاح في Secrets
if "GEMINI_API_KEY" not in st.secrets:
    st.error("🚨 المفتاح غير موجود! تأكد أنك أضفته في Secrets باسم GEMINI_API_KEY")
    st.stop()

# 2. إعداد الاتصال
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    # نستخدم فلاش لأنه الأخف والأسرع
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ فشل في إعداد الاتصال: {e}")
    st.stop()

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري التواصل مع ذكاء جوجل..."):
            try:
                # تجربة بسيطة جداً للتأكد من الاتصال
                response = model.generate_content(f"حسن هذا النص ليكون أمراً احترافياً: {user_input}", 
                                                 generation_config={"timeout": 20}) # مهلة 20 ثانية
                st.success("✅ نجحنا!")
                st.code(response.text)
                st.balloons()
            except Exception as e:
                if "location" in str(e).lower():
                    st.error("🌍 عذراً، سيرفرات Streamlit في هذه المنطقة لا تدعم خدمة Gemini حالياً.")
                else:
                    st.error(f"❌ خطأ أثناء التحسين: {e}")
    else:
        st.warning("⚠️ اكتب شيئاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
 
