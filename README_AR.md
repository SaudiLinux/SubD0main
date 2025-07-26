# أداة Sub

أداة بايثون للكشف عن الفروع المخفية واستخراج الملفات المحددة من الهدف.

**المطور**: SayerLinux (SaudiSayer@gmail.com)

## الميزات

- **اكتشاف النطاقات الفرعية**: البحث عن النطاقات الفرعية المرتبطة بالهدف.
- **اكتشاف المجلدات المخفية**: البحث عن المجلدات المخفية في الهدف.
- **اكتشاف الملفات**: البحث عن الملفات المخفية في الهدف.
- **التنفيذ المتوازي**: تسريع عمليات الفحص باستخدام التنفيذ المتوازي.
- **دعم قوائم الكلمات المخصصة**: استخدام قوائم كلمات مخصصة للبحث.
- **حفظ النتائج**: حفظ نتائج الفحص في ملف نصي.

## التثبيت

### المتطلبات

- بايثون 3.6 أو أحدث
- المكتبات المطلوبة: requests، dnspython، colorama، argparse

### تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

## الاستخدام الأساسي

```bash
python sub.py -t example.com
```

## خيارات سطر الأوامر

```
الاستخدام: sub.py [-h] -t TARGET [-w WORDLIST] [-o OUTPUT] [-v] [-th THREADS]

خيارات:
  -h, --help            عرض رسالة المساعدة هذه والخروج
  -t TARGET, --target TARGET
                        الهدف المراد فحصه (مثال: example.com)
  -w WORDLIST, --wordlist WORDLIST
                        مسار ملف قائمة الكلمات (اختياري)
  -o OUTPUT, --output OUTPUT
                        ملف لحفظ النتائج (اختياري)
  -v, --verbose         عرض معلومات تفصيلية
  -th THREADS, --threads THREADS
                        عدد مسارات التنفيذ المتزامنة (افتراضي: 10)
```

## أمثلة

### فحص أساسي

```bash
python sub.py -t example.com
```

### استخدام قائمة كلمات مخصصة

```bash
python sub.py -t example.com -w wordlists/custom.txt
```

### تسريع الفحص باستخدام المزيد من مسارات التنفيذ

```bash
python sub.py -t example.com -th 50
```

### حفظ النتائج في ملف

```bash
python sub.py -t example.com -o results.txt
```

### فحص تفصيلي

```bash
python sub.py -t example.com -w wordlists/custom.txt -th 30 -o results.txt -v
```

## الاستخدام كمكتبة

يمكن استخدام أداة Sub كمكتبة في مشاريع بايثون أخرى. راجع ملف `examples/example_scan.py` للحصول على مثال.

## الترخيص

راجع ملف [LICENSE](LICENSE) للحصول على معلومات الترخيص.

## المساهمة

راجع ملف [CONTRIBUTING.md](CONTRIBUTING.md) للحصول على إرشادات المساهمة.

## التغييرات

راجع ملف [CHANGELOG.md](CHANGELOG.md) للحصول على سجل التغييرات.

## الأسئلة الشائعة

راجع ملف [FAQ.md](FAQ.md) للحصول على إجابات للأسئلة الشائعة.

## التوثيق التقني

راجع ملف [TECHNICAL.md](TECHNICAL.md) للحصول على معلومات تقنية مفصلة حول كيفية عمل الأداة.