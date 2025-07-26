# دليل تثبيت أداة Sub

هذا الدليل يوضح كيفية تثبيت أداة Sub على أنظمة التشغيل المختلفة.

## المتطلبات

- بايثون 3.6 أو أحدث
- مدير الحزم pip

## تثبيت بايثون

### نظام ويندوز

1. قم بتنزيل أحدث إصدار من بايثون من [الموقع الرسمي](https://www.python.org/downloads/windows/).
2. قم بتشغيل المثبت وتأكد من تحديد خيار "Add Python to PATH" أثناء التثبيت.
3. تحقق من التثبيت بفتح موجه الأوامر وكتابة:
   ```
   python --version
   pip --version
   ```

### نظام لينكس

1. قم بتثبيت بايثون باستخدام مدير الحزم الخاص بالتوزيعة:

   **Ubuntu/Debian**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

   **Fedora**:
   ```bash
   sudo dnf install python3 python3-pip
   ```

   **Arch Linux**:
   ```bash
   sudo pacman -S python python-pip
   ```

2. تحقق من التثبيت:
   ```bash
   python3 --version
   pip3 --version
   ```

### نظام ماك

1. قم بتثبيت Homebrew إذا لم يكن مثبتاً:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. قم بتثبيت بايثون:
   ```bash
   brew install python
   ```

3. تحقق من التثبيت:
   ```bash
   python3 --version
   pip3 --version
   ```

## تثبيت أداة Sub

### الطريقة 1: التنزيل المباشر

1. قم بتنزيل أو استنساخ المستودع:
   ```bash
   git clone https://github.com/SayerLinux/Sub.git
   ```
   أو قم بتنزيل الأرشيف وفك ضغطه.

2. انتقل إلى مجلد الأداة:
   ```bash
   cd Sub
   ```

3. قم بتثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```
   
   في أنظمة لينكس وماك، قد تحتاج إلى استخدام `pip3` بدلاً من `pip`:
   ```bash
   pip3 install -r requirements.txt
   ```

### الطريقة 2: التثبيت من المصدر

1. قم بتنزيل أو استنساخ المستودع:
   ```bash
   git clone https://github.com/SayerLinux/Sub.git
   ```

2. انتقل إلى مجلد الأداة:
   ```bash
   cd Sub
   ```

3. قم بتثبيت الأداة:
   ```bash
   pip install .
   ```
   
   في أنظمة لينكس وماك، قد تحتاج إلى استخدام `pip3` بدلاً من `pip`:
   ```bash
   pip3 install .
   ```

## التحقق من التثبيت

بعد التثبيت، يمكنك التحقق من أن الأداة تعمل بشكل صحيح عن طريق تشغيل:

```bash
python sub.py -h
```

أو إذا قمت بالتثبيت من المصدر:

```bash
sub -h
```

يجب أن ترى رسالة المساعدة التي توضح خيارات الأداة.

## إنشاء بيئة افتراضية (اختياري)

يُنصح بإنشاء بيئة افتراضية لتجنب تعارض المكتبات مع المشاريع الأخرى:

### نظام ويندوز

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### نظام لينكس وماك

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## استكشاف الأخطاء وإصلاحها

### مشكلة: خطأ في تثبيت المتطلبات

إذا واجهت مشاكل في تثبيت المتطلبات، حاول تحديث pip أولاً:

```bash
python -m pip install --upgrade pip
```

ثم أعد تثبيت المتطلبات.

### مشكلة: خطأ "ModuleNotFoundError"

إذا ظهر خطأ "ModuleNotFoundError" عند تشغيل الأداة، تأكد من تثبيت جميع المتطلبات:

```bash
pip install -r requirements.txt
```

### مشكلة: خطأ في الأذونات (لينكس وماك)

إذا واجهت مشاكل في الأذونات عند تشغيل الأداة، قم بتغيير أذونات الملف:

```bash
chmod +x sub.py
```

## المزيد من المساعدة

إذا كنت بحاجة إلى مزيد من المساعدة، يمكنك:

- مراجعة ملف [README.md](README.md) للحصول على معلومات حول استخدام الأداة.
- مراجعة ملف [FAQ.md](FAQ.md) للحصول على إجابات للأسئلة الشائعة.
- التواصل مع المطور عبر البريد الإلكتروني: SaudiSayer@gmail.com