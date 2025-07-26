# توثيق واجهة برمجة التطبيقات (API) لأداة Sub

هذا المستند يوفر معلومات مفصلة حول كيفية استخدام أداة Sub كمكتبة في مشاريع بايثون أخرى.

## استيراد المكتبة

```python
from sub import SubTool
```

## إنشاء كائن SubTool

```python
tool = SubTool(
    target="example.com",       # الهدف المراد فحصه
    wordlist=None,             # مسار ملف قائمة الكلمات أو None لاستخدام القائمة الافتراضية
    threads=10,                # عدد مسارات التنفيذ المتزامنة
    output=None,               # مسار ملف الإخراج أو None إذا لم يتم تحديده
    verbose=False              # علم يشير إلى ما إذا كان يجب عرض معلومات تفصيلية
)
```

## الوظائف الرئيسية

### اكتشاف النطاقات الفرعية

```python
tool.discover_subdomains()
```

تقوم هذه الوظيفة باكتشاف النطاقات الفرعية للهدف باستخدام قائمة الكلمات. يتم تخزين النتائج في خاصية `subdomains`.

### اكتشاف المجلدات

```python
tool.discover_directories()
```

تقوم هذه الوظيفة باكتشاف المجلدات المخفية في الهدف باستخدام قائمة الكلمات. يتم تخزين النتائج في خاصية `directories`.

### اكتشاف الملفات

```python
tool.discover_files()
```

تقوم هذه الوظيفة باكتشاف الملفات المخفية في الهدف باستخدام قائمة الكلمات وامتدادات الملفات الشائعة. يتم تخزين النتائج في خاصية `files`.

### تشغيل جميع عمليات الاكتشاف

```python
tool.run()
```

تقوم هذه الوظيفة بتشغيل جميع عمليات الاكتشاف (النطاقات الفرعية والمجلدات والملفات) وعرض النتائج.

### حفظ النتائج

```python
tool.save_results()
```

تقوم هذه الوظيفة بحفظ النتائج في ملف إذا تم تحديد ملف الإخراج.

## الخصائص

### النطاقات الفرعية المكتشفة

```python
tool.subdomains  # مجموعة تحتوي على النطاقات الفرعية المكتشفة
```

### المجلدات المكتشفة

```python
tool.directories  # مجموعة تحتوي على المجلدات المكتشفة
```

### الملفات المكتشفة

```python
tool.files  # مجموعة تحتوي على الملفات المكتشفة
```

### جميع النتائج

```python
tool.results  # قائمة تحتوي على جميع النتائج مع معلومات إضافية
```

كل عنصر في قائمة `results` هو قاموس يحتوي على المعلومات التالية:

```python
{
    "url": "http://example.com/admin",  # عنوان URL الكامل
    "type": "directory",               # نوع النتيجة (subdomain, directory, file)
    "status_code": 200,               # رمز حالة HTTP (للمجلدات والملفات فقط)
    "content_length": 1234            # طول المحتوى بالبايت (للمجلدات والملفات فقط)
}
```

## أمثلة

### مثال 1: اكتشاف النطاقات الفرعية فقط

```python
from sub import SubTool

tool = SubTool(target="example.com")
tool.discover_subdomains()

print("النطاقات الفرعية المكتشفة:")
for subdomain in tool.subdomains:
    print(f"- {subdomain}")
```

### مثال 2: اكتشاف المجلدات والملفات باستخدام قائمة كلمات مخصصة

```python
from sub import SubTool

tool = SubTool(
    target="example.com",
    wordlist="wordlists/custom.txt",
    threads=20
)

tool.discover_directories()
tool.discover_files()

print("المجلدات المكتشفة:")
for directory in tool.directories:
    print(f"- {directory}")

print("\nالملفات المكتشفة:")
for file in tool.files:
    print(f"- {file}")
```

### مثال 3: تشغيل فحص كامل وحفظ النتائج

```python
from sub import SubTool

tool = SubTool(
    target="example.com",
    wordlist="wordlists/custom.txt",
    threads=30,
    output="results.txt",
    verbose=True
)

tool.run()
```

### مثال 4: الوصول إلى معلومات تفصيلية عن النتائج

```python
from sub import SubTool

tool = SubTool(target="example.com")
tool.run()

print("النتائج التفصيلية:")
for result in tool.results:
    if result["type"] == "subdomain":
        print(f"النطاق الفرعي: {result['url']}")
    elif result["type"] == "directory":
        print(f"المجلد: {result['url']} (الحالة: {result['status_code']}, الحجم: {result['content_length']})")
    elif result["type"] == "file":
        print(f"الملف: {result['url']} (الحالة: {result['status_code']}, الحجم: {result['content_length']})")
```

## ملاحظات

- يمكن استخدام الوظائف `discover_subdomains`، `discover_directories`، و `discover_files` بشكل منفصل أو مجتمعة باستخدام الوظيفة `run`.
- إذا تم تعيين `verbose` إلى `True`، سيتم عرض معلومات تفصيلية أثناء عملية الاكتشاف.
- إذا تم تعيين `output` إلى مسار ملف، سيتم حفظ النتائج في هذا الملف تلقائياً عند استدعاء الوظيفة `run` أو `save_results`.
- يمكن تعديل عدد مسارات التنفيذ المتزامنة باستخدام المعلمة `threads` لتحسين الأداء.