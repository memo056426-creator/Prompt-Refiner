import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="محسن الأوامر Pro", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")
st.markdown("---")

# المفتاح الخاص بك
API_KEY = "AIzaSyAs9liEdvSQWU3M-8B8Zep6nTZSPbi2TCI"
genai.configure(api_key=API_KEY)

# دالة ذكية لتجربة الموديلات المتاحة لضمان التشغيل
def get_response(user_text):
    models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(f"أنت خبير في هندسة الأوامر، حسن هذا النص ليكون أمراً احترافياً ومفصلاً باللغة العربية: {user_text}")
            return response.text, model_name
        except:
            continue
    return None, None

user_input = st.text_area("📝 اكتب فكرتك البسيطة هنا:", height=150)

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري البحث عن أفضل موديل وتحسين الأمر..."):
            result, used_model = get_response(user_input)
            
            if result:
                st.success(f"✅ تم التحسين بنجاح!")
                st.markdown(f"**الموديل المستخدم:** `{used_model}`")
                st.code(result, language='markdown')
                st.balloons()
            else:
                st.error("❌ عذراً، يبدو أن هناك مشكلة في الاتصال بسيرفرات جوجل حالياً. جرب بعد دقيقة.")
    else:
        st.warning("⚠️ يرجى كتابة نص أولاً.")

st.markdown("---")
st.caption("تطوير وحش الشاومي 15 ألترا 🚀")
