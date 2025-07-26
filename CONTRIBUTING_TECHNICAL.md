# دليل المساهمة التقني

هذا الدليل مخصص للمطورين الذين يرغبون في المساهمة في تطوير أداة Sub. يوفر معلومات تقنية مفصلة حول بنية الكود وكيفية إضافة ميزات جديدة أو إصلاح الأخطاء.

## بنية المشروع

```
Sub/
├── sub.py                 # الملف الرئيسي للأداة
├── requirements.txt       # متطلبات بايثون
├── README.md              # توثيق المشروع
├── README_AR.md           # توثيق المشروع باللغة العربية
├── LICENSE                # ملف الترخيص
├── CONTRIBUTING.md        # دليل المساهمة
├── CONTRIBUTING_TECHNICAL.md # دليل المساهمة التقني
├── CHANGELOG.md           # سجل التغييرات
├── FAQ.md                 # الأسئلة الشائعة
├── TECHNICAL.md           # التوثيق التقني
├── API.md                 # توثيق واجهة برمجة التطبيقات
├── INSTALL.md             # دليل التثبيت
├── SECURITY.md            # سياسة الأمان
├── examples/              # أمثلة على استخدام الأداة
│   └── example_scan.py    # مثال على استخدام الأداة برمجياً
└── wordlists/             # قوائم الكلمات
    ├── common.txt         # قائمة كلمات للمجلدات والملفات الشائعة
    ├── extensions.txt     # قائمة امتدادات الملفات الشائعة
    └── subdomains.txt     # قائمة النطاقات الفرعية الشائعة
```

## بنية الكود

### الفئة الرئيسية: SubTool

الفئة `SubTool` هي الفئة الرئيسية في الأداة وتحتوي على جميع الوظائف الأساسية:

```python
class SubTool:
    def __init__(self, target, wordlist=None, threads=10, output=None, verbose=False):
        # تهيئة الخصائص
        
    def _format_target(self, target):
        # تنسيق الهدف
        
    def _get_base_url(self):
        # استخراج عنوان URL الأساسي
        
    def _load_wordlist(self):
        # تحميل قائمة الكلمات
        
    def discover_subdomains(self):
        # اكتشاف النطاقات الفرعية
        
    def _check_subdomain(self, subdomain):
        # التحقق من وجود نطاق فرعي
        
    def discover_directories(self):
        # اكتشاف المجلدات
        
    def discover_files(self):
        # اكتشاف الملفات
        
    def _check_url(self, url, type_name):
        # التحقق من وجود URL
        
    def save_results(self):
        # حفظ النتائج
        
    def run(self):
        # تشغيل جميع عمليات الاكتشاف
```

### الوظيفة الرئيسية: main

الوظيفة `main` هي نقطة الدخول للأداة عند تشغيلها من سطر الأوامر:

```python
def main():
    # تحليل المعلمات من سطر الأوامر
    # إنشاء كائن SubTool
    # تشغيل الأداة
    # معالجة الأخطاء والمقاطعات
```

## إضافة ميزات جديدة

### إضافة وظيفة اكتشاف جديدة

لإضافة وظيفة اكتشاف جديدة، اتبع الخطوات التالية:

1. أضف وظيفة جديدة إلى فئة `SubTool`:

```python
def discover_new_feature(self):
    print(f"\n[*] اكتشاف الميزة الجديدة لـ {self.target}...")
    
    # إضافة خاصية جديدة لتخزين النتائج
    self.new_feature_results = set()
    
    # تنفيذ عملية الاكتشاف
    # ...
    
    print(f"[+] تم اكتشاف {len(self.new_feature_results)} نتيجة.")
```

2. قم بتحديث وظيفة `run` لتشمل الوظيفة الجديدة:

```python
def run(self):
    # ...
    self.discover_subdomains()
    self.discover_directories()
    self.discover_files()
    self.discover_new_feature()  # إضافة الوظيفة الجديدة
    # ...
```

3. قم بتحديث وظيفة `save_results` لحفظ نتائج الميزة الجديدة:

```python
def save_results(self):
    # ...
    if self.output_file:
        with open(self.output_file, "w") as f:
            # ...
            f.write("\n--- الميزة الجديدة ---\n")
            for result in self.new_feature_results:
                f.write(f"{result}\n")
```

### إضافة معلمة جديدة

لإضافة معلمة جديدة إلى الأداة، اتبع الخطوات التالية:

1. قم بتحديث وظيفة `__init__` في فئة `SubTool`:

```python
def __init__(self, target, wordlist=None, threads=10, output=None, verbose=False, new_param=None):
    # ...
    self.new_param = new_param
```

2. قم بتحديث وظيفة `main` لتحليل المعلمة الجديدة من سطر الأوامر:

```python
def main():
    parser = argparse.ArgumentParser(description="أداة للكشف عن الفروع المخفية واستخراج الملفات المحددة من الهدف.")
    # ...
    parser.add_argument("--new-param", help="وصف المعلمة الجديدة")
    # ...
    
    tool = SubTool(
        target=args.target,
        wordlist=args.wordlist,
        threads=args.threads,
        output=args.output,
        verbose=args.verbose,
        new_param=args.new_param
    )
```

## إصلاح الأخطاء

### إضافة اختبارات

لإضافة اختبارات للأداة، يمكنك إنشاء ملف `tests.py` في المجلد الرئيسي:

```python
import unittest
from sub import SubTool

class TestSubTool(unittest.TestCase):
    def setUp(self):
        self.tool = SubTool(target="example.com")
    
    def test_format_target(self):
        self.assertEqual(self.tool._format_target("example.com"), "http://example.com")
        self.assertEqual(self.tool._format_target("http://example.com"), "http://example.com")
        self.assertEqual(self.tool._format_target("https://example.com"), "https://example.com")
    
    # المزيد من الاختبارات...

if __name__ == "__main__":
    unittest.main()
```

### تصحيح الأخطاء

عند تصحيح الأخطاء، اتبع الخطوات التالية:

1. قم بتحديد مصدر الخطأ باستخدام الاختبارات أو التصحيح اليدوي.
2. قم بإصلاح الخطأ في الكود.
3. قم بإضافة اختبار للتأكد من أن الخطأ لن يتكرر في المستقبل.
4. قم بتحديث سجل التغييرات (`CHANGELOG.md`) لتوثيق الإصلاح.

## تحسين الأداء

### تحسين التنفيذ المتوازي

يمكن تحسين التنفيذ المتوازي عن طريق تعديل وظائف الاكتشاف لاستخدام `ThreadPoolExecutor` بشكل أكثر كفاءة:

```python
def discover_directories(self):
    print(f"\n[*] اكتشاف المجلدات المخفية لـ {self.target}...")
    
    self.directories = set()
    wordlist = self._load_wordlist()
    
    with ThreadPoolExecutor(max_workers=self.threads) as executor:
        # استخدام map بدلاً من submit لتحسين الأداء
        results = list(executor.map(
            lambda word: self._check_url(f"{self.base_url}/{word}/", "directory"),
            wordlist
        ))
        
        # معالجة النتائج
        for result in results:
            if result:
                self.directories.add(result["url"])
                self.results.append(result)
    
    print(f"[+] تم اكتشاف {len(self.directories)} مجلد.")
```

### تحسين استخدام الذاكرة

يمكن تحسين استخدام الذاكرة عن طريق تعديل وظيفة `_load_wordlist` لاستخدام مولد بدلاً من قائمة:

```python
def _load_wordlist(self):
    if self.wordlist:
        try:
            with open(self.wordlist, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        yield line
        except Exception as e:
            print(f"[!] خطأ في تحميل قائمة الكلمات: {e}")
            return self._get_default_wordlist()
    else:
        return self._get_default_wordlist()

def _get_default_wordlist(self):
    default_words = ["admin", "login", "wp-admin", "dashboard", "wp-content", "upload", "uploads", "backup", "backups", "wp-includes", "include", "includes", "tmp", "temp", "images", "image", "img", "css", "js", "fonts", "font", "assets", "static", "media", "video", "videos", "audio", "download", "downloads", "file", "files"]
    for word in default_words:
        yield word
```

## إرشادات أسلوب الكود

- اتبع معيار PEP 8 لأسلوب كود بايثون.
- استخدم التعليقات لشرح الأجزاء المعقدة من الكود.
- استخدم أسماء وصفية للمتغيرات والوظائف.
- قم بتوثيق جميع الوظائف والفئات باستخدام سلاسل التوثيق (docstrings).
- استخدم الاستثناءات بشكل مناسب لمعالجة الأخطاء.

## إرشادات الالتزام

عند إرسال التزام (commit)، اتبع الإرشادات التالية:

- استخدم رسائل التزام وصفية تشرح التغييرات بوضوح.
- قم بتضمين رقم المشكلة (issue) في رسالة الالتزام إذا كان ذلك مناسباً.
- قم بتقسيم التغييرات الكبيرة إلى التزامات أصغر ومنطقية.
- تأكد من أن جميع الاختبارات تمر قبل إرسال الالتزام.

## إرشادات طلب السحب

عند إرسال طلب سحب (pull request)، اتبع الإرشادات التالية:

- قم بوصف التغييرات بوضوح في عنوان ووصف طلب السحب.
- قم بتضمين أي معلومات ذات صلة، مثل المشكلات التي تم حلها أو الميزات التي تمت إضافتها.
- قم بتضمين اختبارات للتغييرات إذا كان ذلك مناسباً.
- تأكد من أن جميع الاختبارات تمر قبل إرسال طلب السحب.
- قم بتحديث التوثيق ذي الصلة، مثل `README.md` و `CHANGELOG.md`.

## الاتصال

إذا كان لديك أي أسئلة أو استفسارات حول المساهمة في المشروع، يرجى التواصل مع المطور عبر البريد الإلكتروني: SaudiSayer@gmail.com