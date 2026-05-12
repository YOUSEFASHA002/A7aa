import streamlit as st
import os
import subprocess
import pyautogui
from datetime import datetime

# إعدادات واجهة الموقع
st.set_page_config(page_title="Windows Skills Cloud AI", layout="wide")

# تصميم رأس الصفحة
st.title("🌐 لوحة تحكم Cloud AI الشاملة")
st.subheader("تنفيذ مهارات امتحان الميد (صوت، صورة، وأتمتة)")

# تقسيم الشاشة إلى أعمدة لتنظيم المهارات
col1, col2 = st.columns(2)

with col1:
    st.header("📂 إدارة ملفات الويندوز")
    
    if st.button("📁 إنشاء مجلد الامتحان"):
        path = os.path.join(os.path.expanduser("~\\Desktop"), "MidExam_Project")
        os.makedirs(path, exist_ok=True)
        st.success(f"تم إنشاء المجلد بنجاح في: {path}")

    if st.button("🔍 إظهار امتدادات الملفات"):
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v HideFileExt /t REG_DWORD /d 0 /f')
        st.info("تم تفعيل إظهار امتدادات الملفات بنجاح.")

    if st.button("⚙️ فتح MSConfig"):
        subprocess.Popen("msconfig")
        st.toast("جاري فتح إعدادات النظام...")

with col2:
    st.header("📸 أدوات النظام والتصوير")
    
    if st.button("📸 التقاط الشاشة (Screenshot)"):
        save_path = os.path.join(os.path.expanduser("~\\Pictures"), f"ExamShot_{datetime.now().strftime('%H%M%S')}.png")
        pyautogui.screenshot(save_path)
        st.success(f"تم حفظ اللقطة في مجلد الصور: {save_path}")

    if st.button("⌨️ إظهار الكيبورد الافتراضي"):
        os.system("start osk")

    if st.button("📝 فتح Microsoft Word"):
        try:
            os.startfile("winword.exe")
            st.success("تم تشغيل الوورد. تذكر ضبط المحاذاة والخط الغامق.")
        except:
            st.error("لم يتم العثور على Word.")

# قسم الشرح التعليمي (نظري)
st.divider()
st.header("💡 دليل تنفيذ المهارات يدوياً")
with st.expander("اضغط لرؤية شرح المهارات"):
    st.write("""
    - **نقطة الاستعادة:** ابحث عن 'Create a restore point' في قائمة Start.
    - **إظهار سطح المكتب:** اضغط في أقصى الزاوية اليمنى السفلية من شريط المهام.
    - **حذف السلة:** اضغط يمين على Recycle Bin واختر Empty.
    - **تغيير كلمة السر:** من Settings > Accounts > Sign-in options.
    """)
