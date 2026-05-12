months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
    
    try:
        date = input("Date: ").strip()

        if "/" in date:
            m, d, y = date.split("/")
            
            m, d, y = int(m), int(d), int(y)
                           

        else:
            m, d, y = date.split(" ")
            
            if "," in d:
                d = d.replace(",", "")
            
            else:
                continue

            if m not in months:
                continue
            
            m = months.index(m) + 1
            d, y = int(d), int(y)

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04}-{m:02}-{d:02}")
            break

    except ValueError:
        pass

