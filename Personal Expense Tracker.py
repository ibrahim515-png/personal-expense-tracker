# 1. قائمة المصروفات الرئيسية
expenses = []


# 2. تحميل البيانات من الملف عند بداية البرنامج
def load_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    amount, category, note = line.split("|")
                    expense = {
                        "amount": float(amount),
                        "category": category,
                        "note": note
                    }
                    expenses.append(expense)
    except FileNotFoundError:
        print("لا يوجد ملف سابق، سيتم إنشاء ملف جديد عند الحفظ.")


# 3. إضافة مصروف جديد
def add_expense():
    category = input("أدخل الفئة: ")
    amount = float(input("أدخل المبلغ: "))
    note = input("أدخل الملاحظة: ")

    if amount >= 500:
        print("تنبيه: المبلغ مرتفع!")
    else:
        print("المبلغ مناسب.")

    expense = {"amount": amount, "category": category, "note": note}
    expenses.append(expense)
    print("تمت إضافة المصروف بنجاح!")


# 4. عرض إجمالي المبالغ
def view_summary():
    print(f"\n[اختبار] عدد العناصر المسجلة حالياً: {len(expenses)}")

    if not expenses:
        print("لا يوجد أي مصروفات مسجلة حالياً!")
        return

    total = 0.0
    for item in expenses:
        total += item["amount"]

    print("\n" + "=" * 30)
    print(f"إجمالي المصروفات الكلي: {total} ج.م")
    print("=" * 30)


# 5. عرض المبالغ حسب الفئة
def view_by_category():
    if not expenses:
        print("\nلا يوجد أي مصروفات مسجلة حالياً!")
        return

    category_total = {}
    for item in expenses:
        cat = item["category"]
        amt = item["amount"]
        category_total[cat] = category_total.get(cat, 0.0) + amt

    print("\n--- المبالغ حسب الفئة ---")
    for cat, total in category_total.items():
        print(f"فئة ({cat}): {total} ج.م")
    print("------------------------")


# 6. حفظ البيانات في الملف
def save_expenses():
    with open("expenses.txt", "w", encoding="utf-8") as f:
        for item in expenses:
            f.write(f"{item['amount']}|{item['category']}|{item['note']}\n")
    print("تم حفظ البيانات بنجاح!")


# --- تشغيل البرنامج والقائمة الرئيسية ---
load_expenses()

while True:
    print("\n=== برنامج إدارة المصروفات ===")
    print("1. إضافة مصروف جديد")
    print("2. عرض إجمالي المصروفات")
    print("3. عرض المصروفات حسب الفئة")
    print("4. حفظ وخروج")

    choice = input("اختر رقم الخيار: ")

    if choice == "1":
        add_expense()
        input("\nاضغط Enter للمتابعة...")
    elif choice == "2":
        view_summary()
        input("\nاضغط Enter للمتابعة...")
    elif choice == "3":
        view_by_category()
        input("\nاضغط Enter للمتابعة...")
    elif choice == "4":
        save_expenses()
        print("شكراً لاستخدامك البرنامج!")
        break
    else:
        print("خيار غير صحيح، حاول مرة أخرى.")