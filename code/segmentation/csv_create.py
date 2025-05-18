file = "./data/acdc/acdc_spacing.csv"

text = ",d,h,w"
for i in range(100):
    text = text + f"\npatient{i+1:03},10.0,1.4843800067901611,1.4843800067901611"

with open(file, "w") as f:
    f.write(text)
