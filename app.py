import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="محسن الأوامر الذكي", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")
st.markdown("### حوّل أفكارك البسيطة إلى أوامر احترافية")

# المفتاح الخاص بك
API_KEY = "AIzaSyAs9liEdvSQWU3M-8B8Zep6nTZSPbi2TCI"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# واجهة المستخدم
user_input = st.text_area("📝 اكتب فكرتك البسيطة هنا:", placeholder="مثال: فكرة تطبيق، نصيحة طبية، قصة...")

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري هندسة الأمر بصورة احترافية..."):
            try:
                prompt = f"أنت خبير محترف في هندسة الأوامر. أعد صياغة النص التالي ليكون أمراً (Prompt) مفصلاً، واضحاً، وموجهاً للحصول على أفضل نتيجة من الذكاء الاصطناعي. اجعل النتيجة باللغة العربية: \n\n{user_input}"
                response = model.generate_content(prompt)
                
                st.success("✅ إليك الأمر المحسن:")
                st.code(response.text, language='markdown')
                st.balloons()
            except Exception as e:
                st.error("❌ عذراً، حدث خطأ في الاتصال.")
    else:
        st.warning("⚠️ يرجى كتابة نص أولاً.")

st.sidebar.info("هذا الموقع يعمل بذكاء Gemini ومبرمج عبر Xiaomi 15 Ultra")
