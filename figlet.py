import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # بررسی تعداد پارامترهای ورودی
    if len(sys.argv) == 1:
        # حالت بدون پارامتر ورودی: انتخاب فونت تصادفی
        font = figlet.getFonts()[0]  # انتخاب اولین فونت به عنوان مثال
    elif len(sys.argv) == 3:
        # حالت با 2 پارامتر ورودی
        param1 = sys.argv[1]
        param2 = sys.argv[2]

        # بررسی پارامتر اول
        if param1 not in ['-f', '--font']:
            print("Error: First parameter must be '-f' or '--font'")
            sys.exit(1)

        # بررسی فونت
        if param2 not in figlet.getFonts():
            print(f"Error: Font '{param2}' is not a valid font.")
            sys.exit(1)

        # تنظیم فونت
        font = param2
    else:
        print("Usage: script.py [-f | --font] font_name")
        sys.exit(1)

    # دریافت رشته کاراکتر از کاربر
    user_input = input("Enter the text to convert: ")

    # تنظیم فونت و تبدیل متن
    figlet.setFont(font=font)
    rendered_text = figlet.renderText(user_input)

    # نمایش متن تبدیل شده
    print(rendered_text)

if __name__ == "__main__":
    main()
