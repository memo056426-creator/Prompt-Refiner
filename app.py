import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="محسن الأوامر Pro", page_icon="🤖")

# واجهة فخمة
st.title("🤖 محسن الأوامر الذكي")
st.info("نعمل الآن بنظام Gemini 1.5 Flash الأسرع")

# المفتاح
API_KEY = "AIzaSyAs9liEdvSQWU3M-8B8Zep6nTZSPbi2TCI"
genai.configure(api_key=API_KEY)

# استخدام الموديل الأحدث
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_area("📝 اكتب فكرتك هنا:", height=150)

if st.button("✨ تحسين الأمر الآن"):
    if user_input:
        with st.spinner("⏳ جاري الذكاء..."):
            try:
                prompt = f"أنت خبير في هندسة الأوامر، حسن هذا النص ليكون أمراً احترافياً بالعربية: {user_input}"
                response = model.generate_content(prompt)
                st.success("✅ النتيجة:")
                st.code(response.text)
                st.balloons()
            except Exception as e:
                # هنا سيخبرنا الموقع بالخطأ الحقيقي بدلاً من رسالة عامة
                st.error(f"❌ حدث خطأ تقني: {e}")
    else:
        st.warning("يرجى إدخال نص.")

st.markdown("---")
st.caption("تطوير وحش الشاومي 15 ألترا 🚀")
