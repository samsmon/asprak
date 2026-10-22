# A2. Kelulusan Ujian
uts = int(input())
uas = int(input())
rata = (uts + uas) / 2
print(f"Rata-rata: {rata:.1f}")
if rata >= 60:
    print("Status: LULUS")
else:
    print("Status: TIDAK LULUS")
