import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")

# 1. فحص المفتاح
if "GEMINI_API_KEY" not in st.secrets:
    st.error("🚨 المفتاح غير موجود في Secrets!")
    st.stop()

# 2. إعداد الاتصال
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ فشل الإعداد: {e}")
    st.stop()

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري التواصل مع ذكاء جوجل..."):
            try:
                # التعديل هنا: أرسلنا النص مباشرة بدون تعقيدات الإعدادات
                response = model.generate_content(
                    f"أنت خبير في هندسة الأوامر، حسن هذا النص ليكون أمراً احترافياً ومفصلاً باللغة العربية: {user_input}"
                )
                st.success("✅ نجحنا!")
                st.code(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"❌ خطأ أثناء التحسين: {e}")
    else:
        st.warning("⚠️ اكتب شيئاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
