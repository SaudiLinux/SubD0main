#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
مثال لاستخدام أداة Sub برمجياً

هذا المثال يوضح كيفية استخدام أداة Sub كمكتبة في مشاريع بايثون أخرى

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import sys
import os

# إضافة المجلد الأب إلى مسار البحث عن الوحدات
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد أداة Sub
from sub import SubTool

def main():
    # إنشاء كائن من أداة Sub
    tool = SubTool(
        target="example.com",       # الهدف المراد فحصه
        wordlist=None,             # استخدام قائمة الكلمات الافتراضية
        threads=20,                # عدد مسارات التنفيذ المتزامنة
        output="results.txt",       # ملف لحفظ النتائج
        verbose=True               # عرض معلومات تفصيلية
    )
    
    # تشغيل عملية اكتشاف النطاقات الفرعية فقط
    tool.discover_subdomains()
    
    # طباعة النطاقات الفرعية المكتشفة
    print("\nالنطاقات الفرعية المكتشفة:")
    for subdomain in tool.subdomains:
        print(f"- {subdomain}")
    
    # يمكنك أيضاً تشغيل عمليات اكتشاف محددة فقط
    # tool.discover_directories()
    # tool.discover_files()
    
    # أو تشغيل جميع العمليات دفعة واحدة
    # tool.run()

if __name__ == "__main__":
    main()