import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")

# التأكد من المفتاح
if "GEMINI_API_KEY" not in st.secrets:
    st.error("🚨 المفتاح مفقود في Secrets!")
    st.stop()

# إعداد الموديل مع إجبار الاتصال عبر REST
@st.cache_resource
def setup_genai():
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest') # أضفنا transport='rest' هنا
    return genai.GenerativeModel('gemini-1.5-flash')

model = setup_genai()

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري تحسين الأمر..."):
            try:
                # محاولة توليد المحتوى
                response = model.generate_content(
                    f"أنت خبير في هندسة الأوامر. حسن هذا النص ليكون أمراً احترافياً بالعربية: {user_input}"
                )
                st.success("✅ تم بنجاح!")
                st.code(response.text)
                st.balloons()
            except Exception as e:
                # إذا ظهر خطأ Location، سنعرف فوراً
                error_msg = str(e)
                if "location" in error_msg.lower():
                    st.error("🌍 عذراً، الخدمة غير متوفرة في موقع السيرفر الحالي. سنحاول حلاً بديلاً قريباً.")
                else:
                    st.error(f"❌ حدث خطأ: {error_msg}")
    else:
        st.warning("⚠️ اكتب نصاً أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
