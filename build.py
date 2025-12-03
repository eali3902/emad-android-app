import os
import shutil
import subprocess

print("🚀 بدء بناء تطبيق أندرويد...")

# 1. تنظيف أي ملفات قديمة
if os.path.exists("platforms"):
    shutil.rmtree("platforms")

# 2. إنشاء هيكل مشروع Cordova
subprocess.run(["cordova", "create", "app", "com.emad.accounting", "EmadAccounting"], check=True)

# 3. الانتقال للمجلد
os.chdir("app")

# 4. إضافة منصة أندرويد
subprocess.run(["cordova", "platform", "add", "android"], check=True)

# 5. نسخ ملف index.html إلى www
if os.path.exists("../index.html"):
    shutil.copy("../index.html", "www/index.html")
    
# 6. نسخ أي ملفات أخرى (CSS, JS, صور)
if os.path.exists("../assets"):
    shutil.copytree("../assets", "www/assets", dirs_exist_ok=True)

# 7. بناء التطبيق
print("🔨 جاري بناء APK...")
subprocess.run(["cordova", "build", "android", "--release"], check=True)

# 8. نسخ الملف النهائي
apk_path = "platforms/android/app/build/outputs/apk/release/app-release-unsigned.apk"
if os.path.exists(apk_path):
    shutil.copy(apk_path, "../emad-accounting.apk")
    print("✅ تم بناء التطبيق: emad-accounting.apk")
else:
    print("❌ لم يتم العثور على ملف APK")
