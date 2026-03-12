import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="Prompt Refiner Pro", page_icon="🤖")

st.title("🤖 محسن الأوامر الذكي")

# 1. جلب وتنظيف المفتاح
if "GEMINI_API_KEY" in st.secrets:
    try:
        # .strip() هذي تحذف أي مسافات مخفية قد تسبب خطأ latin-1
        api_key = st.secrets["GEMINI_API_KEY"].strip()
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"خطأ في إعداد المفتاح: {e}")
else:
    st.error("🚨 المفتاح مفقود في Secrets!")
    st.stop()

user_input = st.text_area("📝 اكتب فكرتك هنا:")

if st.button("✨ ابدأ التحسين الآن"):
    if user_input:
        with st.spinner("⏳ جاري التحسين..."):
            try:
                # إرسال النص العربي مباشرة
                response = model.generate_content(
                    f"أنت خبير في هندسة الأوامر. أعد صياغة النص التالي ليكون أمراً (Prompt) احترافياً ومفصلاً باللغة العربية: {user_input}"
                )
                
                if response.text:
                    st.success("✅ تم التحسين بنجاح!")
                    st.code(response.text)
                    st.balloons()
            except Exception as e:
                # لإظهار الخطأ بوضوح إذا كان بسبب الموقع الجغرافي
                error_str = str(e)
                if "location" in error_str.lower():
                    st.error("🌍 السيرفر في منطقة غير مدعومة حالياً. جرب إعادة تشغيل التطبيق (Reboot).")
                else:
                    st.error(f"❌ حدث خطأ: {error_str}")
    else:
        st.warning("⚠️ يرجى كتابة نص أولاً.")

st.caption("برمجت بواسطة Xiaomi 15 Ultra 🚀")
 
