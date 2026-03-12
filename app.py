import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="محسن الأوامر Pro", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")
st.markdown("---")

# جلب المفتاح سراً من إعدادات الموقع
try:
    if "GEMINI_API_KEY" in st.secrets:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("⚠️ خطأ: المفتاح غير موجود في إعدادات Secrets.")
except Exception as e:
    st.error(f"❌ حدث خطأ في النظام: {e}")

user_input = st.text_area("📝 اكتب فكرتك البسيطة هنا:", height=150)

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري التحسين..."):
            try:
                prompt = f"أنت خبير في هندسة الأوامر، حسن هذا النص ليكون أمراً احترافياً ومفصلاً باللغة العربية: {user_input}"
                response = model.generate_content(prompt)
                st.success("✅ تم التحسين بنجاح!")
                st.code(response.text, language='markdown')
                st.balloons()
            except Exception as e:
                st.error(f"❌ حدث خطأ أثناء الاتصال بجوجل: {str(e)}")
    else:
        st.warning("⚠️ يرجى كتابة نص أولاً.")

st.markdown("---")
st.caption("تطوير وحش الشاومي 15 ألترا 🚀")
