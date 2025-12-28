import psutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



print("✅ NumPy  Pandas")
print(f"version NumPy: {np.__version__}")



# ایجاد داده‌های نمونه
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
    
    # رسم نمودار
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'b-o', linewidth=2, markersize=8)
plt.title('test plot $y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, alpha=0.3)
plt.show()
print("✅ test plot")

# تست سلول‌های تعاملی
#print("\n" + "="*50)
#print("تست ورودی تعاملی:")
#name = input("نام شما چیست؟ ")
#print(f"سلام {name}! نوت‌بوک شما آماده کار است.")

# بررسی منابع سیستم

print(f"\n💾 memory  : {psutil.virtual_memory().percent}%")
print(f"💿  disk : {psutil.disk_usage('/').free / 1e9:.1f} GB")