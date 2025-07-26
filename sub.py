#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sub Tool - أداة Sub

أداة تقوم بإظهار الفروع المخفية للهدف واستخراج الملفات الخاصة والحقيقية للهدف

المبرمج: SayerLinux
البريد الإلكتروني: SaudiSayer@gmail.com
"""

import os
import sys
import argparse
import requests
import concurrent.futures
import socket
import dns.resolver
from urllib.parse import urlparse
from colorama import Fore, Style, init

# تهيئة colorama للألوان
init(autoreset=True)

# الشعار
BANNER = f"""
{Fore.GREEN}  _____       _     {Fore.RED} _____           _ 
{Fore.GREEN} / ____|     | |    {Fore.RED}|_   _|         | |
{Fore.GREEN}| (___  _   _| |__  {Fore.RED}  | |  ___   ___| |
{Fore.GREEN} \___ \| | | | '_ \ {Fore.RED}  | | / _ \ / _ \ |
{Fore.GREEN} ____) | |_| | |_) |{Fore.RED} _| || (_) |  __/ |
{Fore.GREEN}|_____/ \__,_|_.__/ {Fore.RED}|_____\___/ \___|_|
{Fore.YELLOW}                                         
{Fore.CYAN}  المبرمج: {Fore.WHITE}SayerLinux
{Fore.CYAN}  البريد الإلكتروني: {Fore.WHITE}SaudiSayer@gmail.com
{Style.RESET_ALL}"""

class SubTool:
    def __init__(self, target, wordlist=None, threads=10, output=None, verbose=False):
        self.target = self._format_target(target)
        self.base_url = self._get_base_url()
        self.wordlist = wordlist
        self.threads = threads
        self.output_file = output
        self.verbose = verbose
        self.subdomains = set()
        self.directories = set()
        self.files = set()
        self.results = []

    def _format_target(self, target):
        """تنسيق الهدف بشكل صحيح"""
        if not (target.startswith('http://') or target.startswith('https://')):
            target = 'http://' + target
        return target

    def _get_base_url(self):
        """الحصول على عنوان URL الأساسي"""
        parsed = urlparse(self.target)
        return f"{parsed.scheme}://{parsed.netloc}"

    def _load_wordlist(self):
        """تحميل قائمة الكلمات"""
        if not self.wordlist:
            # قائمة افتراضية صغيرة للاختبار
            return ["admin", "test", "dev", "api", "staging", "beta", "internal", 
                    "backup", "config", "private", "secret", "hidden", "portal", 
                    "login", "dashboard", "wp-admin", "cpanel", "phpmyadmin", 
                    "webmail", "mail", "remote", "intranet", "extranet", "secure"]
        
        try:
            with open(self.wordlist, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"{Fore.RED}[!] خطأ في قراءة ملف قائمة الكلمات: {e}{Style.RESET_ALL}")
            sys.exit(1)

    def discover_subdomains(self):
        """اكتشاف النطاقات الفرعية"""
        print(f"\n{Fore.CYAN}[*] جاري البحث عن النطاقات الفرعية...{Style.RESET_ALL}")
        
        wordlist = self._load_wordlist()
        parsed = urlparse(self.target)
        domain = parsed.netloc
        
        # إزالة www. إذا كانت موجودة
        if domain.startswith('www.'):
            domain = domain[4:]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for word in wordlist:
                subdomain = f"{word}.{domain}"
                futures.append(executor.submit(self._check_subdomain, subdomain))
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.subdomains.add(result)
                    self.results.append({"type": "subdomain", "value": result})
                    print(f"{Fore.GREEN}[+] تم العثور على نطاق فرعي: {result}{Style.RESET_ALL}")
    
    def _check_subdomain(self, subdomain):
        """التحقق من وجود نطاق فرعي"""
        try:
            dns.resolver.resolve(subdomain, 'A')
            return subdomain
        except:
            return None

    def discover_directories(self):
        """اكتشاف المجلدات"""
        print(f"\n{Fore.CYAN}[*] جاري البحث عن المجلدات...{Style.RESET_ALL}")
        
        wordlist = self._load_wordlist()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for word in wordlist:
                url = f"{self.base_url}/{word}/"
                futures.append(executor.submit(self._check_url, url, "directory"))
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.directories.add(result["value"])
                    self.results.append(result)
                    print(f"{Fore.GREEN}[+] تم العثور على مجلد: {result['value']}{Style.RESET_ALL}")

    def discover_files(self):
        """اكتشاف الملفات"""
        print(f"\n{Fore.CYAN}[*] جاري البحث عن الملفات...{Style.RESET_ALL}")
        
        # قائمة امتدادات الملفات الشائعة
        extensions = [".php", ".html", ".js", ".txt", ".xml", ".json", ".bak", ".old", ".backup", ".config"]
        wordlist = self._load_wordlist()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for word in wordlist:
                # التحقق من الملف بدون امتداد
                url = f"{self.base_url}/{word}"
                futures.append(executor.submit(self._check_url, url, "file"))
                
                # التحقق من الملفات مع امتدادات مختلفة
                for ext in extensions:
                    url = f"{self.base_url}/{word}{ext}"
                    futures.append(executor.submit(self._check_url, url, "file"))
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.files.add(result["value"])
                    self.results.append(result)
                    print(f"{Fore.GREEN}[+] تم العثور على ملف: {result['value']}{Style.RESET_ALL}")

    def _check_url(self, url, type_name):
        """التحقق من وجود URL"""
        try:
            response = requests.get(url, timeout=5, allow_redirects=False)
            
            # التحقق من الاستجابات الناجحة (2xx) أو إعادة التوجيه (3xx)
            if 200 <= response.status_code < 400:
                return {"type": type_name, "value": url, "status": response.status_code}
            elif self.verbose:
                print(f"{Fore.YELLOW}[-] {url} - {response.status_code}{Style.RESET_ALL}")
                
        except requests.exceptions.RequestException:
            pass
        
        return None

    def save_results(self):
        """حفظ النتائج في ملف"""
        if not self.output_file:
            return
            
        try:
            with open(self.output_file, 'w') as f:
                f.write(f"# نتائج فحص {self.target}\n\n")
                
                if self.subdomains:
                    f.write("## النطاقات الفرعية\n")
                    for subdomain in sorted(self.subdomains):
                        f.write(f"{subdomain}\n")
                    f.write("\n")
                
                if self.directories:
                    f.write("## المجلدات\n")
                    for directory in sorted(self.directories):
                        f.write(f"{directory}\n")
                    f.write("\n")
                
                if self.files:
                    f.write("## الملفات\n")
                    for file in sorted(self.files):
                        f.write(f"{file}\n")
            
            print(f"\n{Fore.GREEN}[+] تم حفظ النتائج في {self.output_file}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] خطأ في حفظ النتائج: {e}{Style.RESET_ALL}")

    def run(self):
        """تشغيل جميع عمليات الاكتشاف"""
        print(BANNER)
        print(f"{Fore.CYAN}[*] الهدف: {self.target}{Style.RESET_ALL}")
        
        self.discover_subdomains()
        self.discover_directories()
        self.discover_files()
        
        # طباعة ملخص النتائج
        print(f"\n{Fore.YELLOW}=== ملخص النتائج ==={Style.RESET_ALL}")
        print(f"{Fore.CYAN}النطاقات الفرعية: {Fore.GREEN}{len(self.subdomains)}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}المجلدات: {Fore.GREEN}{len(self.directories)}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}الملفات: {Fore.GREEN}{len(self.files)}{Style.RESET_ALL}")
        
        # حفظ النتائج إذا تم تحديد ملف الإخراج
        self.save_results()

def main():
    parser = argparse.ArgumentParser(description="أداة Sub - أداة لاكتشاف النطاقات الفرعية والمجلدات والملفات المخفية")
    parser.add_argument("target", help="الهدف المراد فحصه (مثال: example.com)")
    parser.add_argument("-w", "--wordlist", help="مسار ملف قائمة الكلمات")
    parser.add_argument("-t", "--threads", type=int, default=10, help="عدد مسارات التنفيذ المتزامنة (الافتراضي: 10)")
    parser.add_argument("-o", "--output", help="ملف لحفظ النتائج")
    parser.add_argument("-v", "--verbose", action="store_true", help="عرض معلومات تفصيلية أثناء الفحص")
    
    args = parser.parse_args()
    
    try:
        tool = SubTool(
            target=args.target,
            wordlist=args.wordlist,
            threads=args.threads,
            output=args.output,
            verbose=args.verbose
        )
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] تم إيقاف البرنامج بواسطة المستخدم{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}[!] حدث خطأ: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()